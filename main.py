
from fastapi import FastAPI, HTTPException
from . import models, schemas
from .database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get("/posts", response_model=list[schemas.Post])
def read_root(offset: int = 0, limit: int = 3):
    session = SessionLocal()
    posts = session.query(models.Post).offset(offset).limit(limit).all()
    session.close()

    return posts


@app.get("/posts/{post_id}", response_model=schemas.Post)
def read_post(post_id: int):
    session = SessionLocal()
    db_post = session.query(models.Post).filter(models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post does not exists")
    session.close()

    return db_post


@app.put("/posts/{post_id}")
def update_post(post_id: int, post: schemas.PostCreate):
    session = SessionLocal()
    db_post = session.query(models.Post).filter(models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post does not exists")
    db_post_same_title = session.query(models.Post).filter(models.Post.title == post.title).first()
    if db_post_same_title:
        raise HTTPException(status_code=400, detail="Title already exists")
    
    db_post.title = post.title
    db_post.text = post.text
    session.commit()
    session.close()

    return db_post

@app.post("/posts", response_model=schemas.Post)
def create_post(post: schemas.PostCreate):
    session = SessionLocal()
    db_post = session.query(models.Post).filter(models.Post.title == post.title).first()
    if db_post:
        raise HTTPException(status_code=400, detail="Title already exists")
    
    db_post = models.Post(title=post.title, text=post.text)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    session.close()

    return db_post


@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    session = SessionLocal()
    db_post = session.query(models.Post).filter(models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post does not exists")
    
    session.delete(db_post)
    session.commit()
    session.close()

    return {}
