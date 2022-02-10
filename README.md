# pyforge-2-quantori

## To run project in development mode:

- Install [Python 3.8](https://www.python.org/downloads/) or upper
- Install [Docker](https://www.docker.com/)
- Open terminal
- Clone the [repository](https://github.com/kuzaster/pyforge-2-quantori.git)
- Go to the web service directory of the project `/pyforge-2-quantori/services/web/`
- Create virtual environment and activate it
- Install packages from requirements `pip install -r requirements.txt`
- Back to the main directory of the project `/pyforge-2-quantori`
- Run `docker-compose up -d --build` (it will build images, create containers and run them)
- Open up your web browser and enter (http://localhost:5000/) in the address field to see the working app