# README

An app to manage food at home including a meal randomizer, recipe database, and can give meal options given ingredients

# Design and Spec

TODO: Store all foods in DB, what is the schema? What does it look like? Recipe? Ingredients?

SOLVED: See database_design.png

It will randomly choose a food for the day 

> TODO: Random food selection

Will select a random meal from the Recipes table

> TODO: Add on: Randomly choose a food based on ingredients we have 

> TODO: Add Ingredients somehow into the DB design SOLVED

> TODO: Display picture and recipe on a Web interface for user, with a randomizer screen 

> TODO: Maybe a template would be good. A template for rendering with -> picture, ingredients list, recipe (these need to be in the DB)

> TODO: Meal Adder Tool: Tool that you can add new meals with, ingredients and recipe there to be filled in and then saved to DB

> TODO: A "Shopping List" feature that adds up all the ingredients you need for the week

# Technologies 

Backend: Python, API: FASTAPI SQLAlchemy Pydantic?
Local toolchain: venv, ruff (linting), pytest, MyPy (typing), Pre-commit (commit hooks)

DB: PostGRES 
Frontend: React + TypeScript, HTML CSS

Infra: Dockerized, Microservices?






