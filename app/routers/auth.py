from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, models, oauth2, schemas, utils

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):

    user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_FORBIDDEN, detail=f"Invalid credentials"
        )

    if not utils.verify_Password(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_FORBIDDEN, detail=f"Invalid credentials "
        )

    # create token for authentication
    acces_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": acces_token, "token_type": "bearer"}
