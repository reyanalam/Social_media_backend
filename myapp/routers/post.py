from .. import models, schemas, utils
from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from .. database import get_db
from .. schemas import UserCreate, UserOut, CreatePost, UpdatePost, Response, postout
from .. import oauth2
from typing import Optional
from sqlalchemy import func

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get('/', response_model=list[postout])
def get_posts(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user),limit:int=10,skip:int=0,search: Optional[str] = ""):
    #cursor.execute("""SELECT * FROM post""")
    #posts = cursor.fetchall()
    posts = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.owner_id == user_id.id, models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No posts found")
    return posts

@router.post('/',status_code=status.HTTP_201_CREATED, response_model=Response)
def create_posts(post: CreatePost,db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    print(user_id)
    new_post = models.Post(title=post.title, content=post.content, published=post.published, owner_id=user_id.id)  #owner_id is the id of the user who created the post
    db.add(new_post) #add the new post to the database
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get('/{id}')  #{id} is a path parameter
def get_post(id :int,db: Session = Depends(get_db),user_id: int = Depends(oauth2.get_current_user)):
    #cursor.execute("""SELECT * FROM post WHERE id = %s""", (id,))
    #post = cursor.fetchone()
    
    post = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db),user_id: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post:
        if post.owner_id != user_id.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this post")
        db.delete(post)
        db.commit()
        return {'message':'post deleted successfully'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    

@router.put('/{id}')
def update_post(id: int, update: UpdatePost,db: Session = Depends(get_db),user_id: int = Depends(oauth2.get_current_user)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    if post:
        if post.owner_id != user_id.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this post")
        post_query.update(update.dict(), synchronize_session=False)

        db.commit()

    return post_query.first()