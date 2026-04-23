# README

An app to manage food at home including a meal randomizer, recipe database, and can give meal options given ingredients

# Design and Spec

TODO: Store all foods in DB, what is the schema? What does it look like? Recipe? Ingredients?

id | food_name | recipe | ingredients | picture_link

It will randomly choose a food for the day 

> TODO: Random food selection 

Add on: Randomly choose a food based on ingredients we have 

> TODO: Add Ingredients somehow into the DB design 

Display picture and recipe on a Web interface for user, with a randomizer screen 

> TODO: Maybe a template would be good. A template for rendering with -> picture, ingredients list, recipe (these need to be in the DB)

> TODO: Meal Adder Tool: Tool that you can add new meals with, ingredients and recipe there to be filled in and then saved to DB

# Technologies 

Backend: Python, API: FASTAPI SQLAlchemy?
Local toolchain: venv, ruff (linting), pytest, MyPy (typing), Pre-commit (commit hooks)

DB: PostGRES 
Frontend: React + TypeScript, HTML CSS

Infra: Dockerized, Microservices?






