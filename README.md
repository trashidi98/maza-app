# README

An app to manage food at home including a meal randomizer, recipe database, and can give meal options given ingredients

# Design and Spec

TODO: Store all foods in DB, what is the schema? What does it look like? Recipe? Ingredients?

It will randomly choose a food for the day 

> TODO: Random food selection 

Add on: Randomly choose a food based on ingredients we have 

> TODO: Add Ingredients somehow into the DB design 

Display picture and recipe on a Web interface for user, with a randomizer screen 

Displaying picture will need some kind of store for the images either on disk or on a remote server (usually S3 or a CDN), but the local path to the image (e.g. /username\_id\_) or url of the image will be stored in the main DB

> TODO: Maybe a template would be good. A template for rendering with -> picture, ingredients list, recipe (these need to be in the DB)

> TODO: Meal Adder Tool: Tool that you can add new meals with, ingredients and recipe there to be filled in and then saved to DB



# Technologies 

Backend: Python, API: FASTAPI SQLAlchemy?
DB: PostGRES 
Frontend: React + TypeScript, HTML CSS

Infra: Dockerized, Microservices?






