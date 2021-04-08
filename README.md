# Data Mining Project

## Get started

Clone the project from his github repository

```sh
git clone https://github.com/ilies-bel/datamining-project.git
cd datamining-project
```

Lauch the docker-compose which will run the postgres database

```sh
docker-compose up --build
```
Finally, you can start the python project

```sh
python3 ./src/main.py
```

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
## Recommendation

Recommendation is based on a combination metadata and semantic information through a random tree algorithme.  

To test it. Choose a user id (ex: 1) after starting the main. The recommendation is more precise and pertinent as the amount of data (number of history entries) is rich. 


## Visualization

The visualization of the data of our appication is made out of two tables and two graphs so far :

- user_history(user_id) : Display a table of the information about a user given in paramater (user_id)
- users_dashboard() :  Display a table of the information about all users
- paintings_through_time() : Building a dataframe from paintings through time
- likes_by_artist() : Building a dataframe from likes group by artist

## Tests

Getting the recommendation result, we used functional testing to evaluate the relevancy of the recommendation system.

## Improvements

A lot of this project functionalities could and should be improved such as follow :

- Have a dynamic user profile creation
- Define tags for the user and give it a more effective weight for the recommendation algorithm
- A user should not see once again a painting already seen
- Have new visualization tools such as the accuracy of the recommendation algoritm based on a test set

## Contributors

[Beldjilali Iliès](https://github.com/ilies-bel) & [Folléas Brice](https://github.com/AmazingBrice)
