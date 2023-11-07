from fastapi import APIRouter, HTTPException
from bson import ObjectId
from models.user import User
from config.db import conn
from schemas.user import serializeList, serializeDict

user = APIRouter()

@user.get('/')
async def find_all_users():
    return serializeList(conn.desenvolvimento.user.find())

@user.get('/{name}')
async def find_user(name):
    return serializeList(conn.desenvolvimento.user.find_one({"name": name}))

@user.post('/')
async def create_user(user: User):
    existing_user = conn.desenvolvimento.user.find_one({"name": user.name})
    if existing_user is None:
        conn.desenvolvimento.user.insert_one(dict(user))
    else:
        return "User already exists"
    return serializeList(conn.desenvolvimento.user.find())

@user.put('/{id}')
async def update_user(id, user: User):
    conn.desenvolvimento.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return serializeDict(conn.desenvolvimento.user.find_one({"_id": ObjectId(id)}))

@user.delete('/{id}')
async def delete_user_by_id(id):
    return serializeDict(conn.desenvolvimento.user.find_one_and_delete({"_id": ObjectId(id)}))

@user.post('/login')
async def login_user(username: str,password:str):
    user = conn.desenvolvimento.user.find_one({"name": username})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    elif user['password'] != password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    else:
        return serializeDict(user)
