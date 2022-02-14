# pyforge-2-quantori

## First steps:

- Install [Python 3.8](https://www.python.org/downloads/) or upper
- Install [Docker](https://www.docker.com/)
- Open terminal
- Clone the [repository](https://github.com/kuzaster/pyforge-2-quantori.git)
- Go to the main directory of the project `/pyforge-2-quantori`

## Run project in development mode

Uses the default Flask development server.

- Build the images and run the containers:

    `docker-compose up -d --build`

- Test it out at http://localhost:5000. 

## Run project in production mode

Uses gunicorn + nginx.

- If you ran the project in development mode before, run command:

  `docker-compose down -v`


- Build the images and run the containers:

  `docker-compose -f docker-compose.prod.yml up -d --build`

- Create database schema: 

  `docker-compose exec web python manage.py create_db`

- Fill database by default data: 
  
  `docker-compose exec web python manage.py seed_db`

- Test it out at http://localhost:1337