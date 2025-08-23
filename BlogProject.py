from fastapi import FastAPI
from typing import List, Dict, Any
from pydantic import BaseModel

app = FastAPI()

class PostModel(BaseModel):
    title: str
    content: str

DB_POSTS: List[Dict[str, Any]] = [
    {"id": 1, "title": "Introduction to FastAPI", "content": "Learning FastAPI is awesome..."},
    {"id": 2, "title": "Understanding Pydantic", "content": "Data validation is so easy..."},
]


@app.get("/")
async def root():
    return {"message": "Welcome to the Simple Blog API!"}

@app.get("/posts")
async def get_posts():
    return {"posts": DB_POSTS}

@app.get("/posts/{post_id}")
async def get_post_by_id(post_id: int):
    
    for post in DB_POSTS:
        if post["id"] == post_id:
            return {"post": post}
    
    return {"error": "Post not found."}


@app.post("/posts")
async def create_post(new_post: PostModel):

    new_id = max(post["id"] for post in DB_POSTS) + 1 if DB_POSTS else 1
    
    post_dict = new_post.dict()
    post_dict["id"] = new_id
    
    DB_POSTS.append(post_dict)
    
    return {"message": "Post created successfully.", "data": post_dict}
