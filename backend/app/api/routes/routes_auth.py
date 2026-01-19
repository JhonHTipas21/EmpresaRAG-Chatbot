from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import UserCreate, Token, UserLogin
from app.core.security import verify_password, get_password_hash, create_access_token

router = APIRouter(prefix="/api/auth", tags=["auth"])

# Base de datos en memoria (en producción usa DB real)
fake_users_db = {}

@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
    """Registra nuevo usuario"""
    if user.username in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario ya existe"
        )
    
    hashed_password = get_password_hash(user.password)
    fake_users_db[user.username] = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password
    }
    
    access_token = create_access_token(data={"sub": user.username, "email": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login de usuario"""
    user = fake_users_db.get(form_data.username)
    
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user["username"], "email": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}
