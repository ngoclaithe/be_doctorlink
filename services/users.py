from sqlalchemy.orm import Session
from app.models.users import User  
from app.schemas.users import UserCreate, UserUpdate
from passlib.context import CryptContext

class UsersService:
    def __init__(self, db: Session):
        self.db = db
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_user_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(User).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreate):
        hashed_password = self.get_password_hash(user.password)
        db_user = User(
            username=user.username,
            email=user.email,
            password=hashed_password,
            role=user.role
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user_id: int, user: UserUpdate):
        db_user = self.get_user(user_id)
        if not db_user:
            return None
        if user.username is not None:
            db_user.username = user.username
        if user.email is not None:
            db_user.email = user.email
        if user.role is not None:
            db_user.role = user.role
        if user.password is not None:
            db_user.password = self.get_password_hash(user.password)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        db_user = self.get_user(user_id)
        if not db_user:
            return None
        self.db.delete(db_user)
        self.db.commit()
        return db_user

    def authenticate_user(self, username: str, password: str):
        user = self.get_user_by_username(username)
        if not user:
            return False
        if not self.verify_password(password, user.password):
            return False
        return user
    
    def get_user_details(self, user):
        if not user:
            return None
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        }