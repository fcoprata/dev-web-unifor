from bson import ObjectId
from fastapi import APIRouter, HTTPException
from src.verify_password import verify_password,pwd_context
from models.user import User
from config.db import conn
from schemas.user import serializeList, serializeDict

user = APIRouter()

@user.get('/users')
async def find_all_users():
    return serializeList(conn.desenvolvimento.user.find())

@user.get('/user/{id}')
async def find_user_by_id(id):
    return serializeDict(conn.desenvolvimento.user.find_one({"_id": ObjectId(id)}))

@user.get('/name/{name}')
async def find_user_by_name(name):
    return serializeDict(conn.desenvolvimento.user.find_one({"name": name}))

@user.get('/email/{email}')
async def find_user_by_email(email):
    return serializeDict(conn.desenvolvimento.user.find_one({"email": email}))

@user.post('/user/create')
async def create_user(user: User):
    existing_user = conn.desenvolvimento.user.find_one({"name": user.name})
    user.password = pwd_context.hash(user.password)
    if existing_user is None:
        conn.desenvolvimento.user.insert_one(dict(user))
    else:
        return "User already exists"
    return serializeList(conn.desenvolvimento.user.find())

@user.put('/user/update/{id}')
async def update_user(id, user: User):
    conn.desenvolvimento.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return serializeDict(conn.desenvolvimento.user.find_one({"_id": ObjectId(id)}))

@user.delete('/user/delete/{id}')
async def delete_user_by_id(id):
    return serializeDict(conn.desenvolvimento.user.find_one_and_delete({"_id": ObjectId(id)}))

@user.post('/login')
async def login_user(username: str,password:str):
    user = conn.desenvolvimento.user.find_one({"name": username})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Incorrect password")
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return serializeDict(user)
