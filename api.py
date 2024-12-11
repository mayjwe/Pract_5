import uvicorn
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from config import DBSettings  # Assuming your DBSettings is defined properly
from path import User, Role  # Assuming your User model is correctly defined
from response_models import UserCreate

app = FastAPI(
    title="User API",
    description="An API for managing users",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/users/select/{user_id}")
def get_user(user_id: int):
    try:
        with DBSettings.get_session() as conn:
            user = conn.query(User).filter(User.id == user_id).first()
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
@app.post("/users/add", response_model= UserCreate)
async def add_users(user_name:str, user_role:str):
    user = UserCreate(name=user_name, role=user_role)
    with DBSettings.get_session() as conn:
        roleDB = conn.query(Role).filter(Role.name == user.role).first()
        if (roleDB == None):
            raise HTTPException(status_code=404, detail="We haven't this role")
        else:
            new_user = User(name = user.name, role_id = roleDB.id)
            conn.add(new_user)
            conn.commit()
            print("Успешно")
            return(user)


@app.put("/users/update/{user_id}", response_model=UserCreate)
async def update_user(user_id: int, user_name: str = None, user_role: str = None):
    try:
        with DBSettings.get_session() as conn:
            user = conn.query(User).filter(User.id == user_id).first()
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")

            # Обновление имени пользователя, если передано новое значение
            if user_name:
                user.name = user_name

            # Обновление роли пользователя, если передано новое значение
            if user_role:
                roleDB = conn.query(Role).filter(Role.name == user_role).first()
                if roleDB is None:
                    raise HTTPException(status_code=404, detail="Role not found")
                user.role_id = roleDB.id

            # Коммитим изменения в базе данных
            conn.commit()
            return UserCreate(name=user.name, role=user_role if user_role else roleDB.name)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# DELETE запрос для удаления пользователя
@app.delete("/users/delete/{user_id}", status_code=204)
async def delete_user(user_id: int):
    try:
        with DBSettings.get_session() as conn:
            user = conn.query(User).filter(User.id == user_id).first()
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")

            # Удаляем пользователя из базы данных
            conn.delete(user)
            conn.commit()
            return {"detail": f"User with id {user_id} has been deleted"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)