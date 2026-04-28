from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


app = FastAPI()

engine = create_engine(
    "sqlite:///maza_database.db", connect_args={"check_same_thread": False}
)

LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


class Base(DeclarativeBase):
    pass


class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)


Base.metadata.create_all(engine)


class IngredientCreate(BaseModel):
    name: str


class IngredientResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


get_db()


@app.get("/ingredients/{ingredient_id}", response_model=IngredientResponse)
def get_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()

    if not ingredient:
        raise HTTPException

    return ingredient


@app.post("/ingredients/", response_model=IngredientResponse)
def create_ingredient(ingredient: IngredientCreate, db: Session = Depends(get_db)):
    if (
        ingredient
        == db.query(Ingredient).filter(Ingredient.name == ingredient.name).first()
    ):
        raise HTTPException

    new_ingredient = Ingredient(**ingredient.model_dump())
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)

    return new_ingredient


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: int):
    return {"recipe_id": recipe_id}
