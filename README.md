# Data Mining Project

Beldjilali Iliès & Folléas Brice

## Get started

Clone the project from his github repository

``
git clone https://github.com/ilies-bel/datamining-project.git
cd datamining-project
``

Lauch the docker-compose which will run the postgres database

``
docker-compose up --build
``
Finally, you can start the python project

``
python3 ./src/main.py
``

In the main.py, you have to enter the number of images to download and the number of rows to create in history table for recommendation.

## Getting report

```
├── _ datamining-project
│   ├── lib
│   │   ...
│   └── src
├── _Assets
└── reports_files
```

## User profile

At first users have generated directly from the postgresql database's docker container's creation with a script inserting a set of users. Then, the idea of using a seed function like we have done for the creation of the history of the paintings seen by users came to our mind.
The users' information are standard information such as username, email, password and also preferences of the user such as the favorite color, orientation or size.
The main goal of the users' information is to be observable during visualization through a graph.

## Tests

Getting the recommandation result, we used functional testing to evaluate the relevancy of the recommandation system.
