from fastapi import FastAPI

print("Hello from maza-app!")
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: int):
    return {"recipe_id": recipe_id}