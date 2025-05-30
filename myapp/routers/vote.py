from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from .. import schemas, models, oauth2, database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first() #check if the post exists

    if not post: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {vote.post_id} does not exist"
        )
    
    vote_query = db.query(models.Vote).filter(
            models.Vote.post_id == vote.post_id,
            models.Vote.user_id == current_user.id
        )
    #vote_query checks that specific user has already voted on a specific post

    found_vote = vote_query.first() #if the user has already voted on the post, it will return the vote object, otherwise it will return None

    if vote.dir == 1:
        
        if found_vote: # if the user has already voted on the post he cannot vote again
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User {current_user.id} has already voted on post {vote.post_id}"
            )
        new_vote = models.Vote(
            post_id=vote.post_id,
            user_id=current_user.id
        )

        db.add(new_vote)
        db.commit()
        return {"message": "Vote added successfully"}
        
    elif vote.dir == 0: #vote==0 meant delete the vote
        if not found_vote: #cannot remove a vote if it does not exist
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Vote not found for user {current_user.id} on post {vote.post_id}"
            )
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Vote removed successfully"}