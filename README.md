
# Dependencies

psycopg, django, djangorestframework:

    $ python3 -m pip install psycopg
    $ python3 -m pip install django
    $ python3 -m pip install djangorestframework


# Preview
Main page:
![API Searching page preview](https://i.imgur.com/CMLHVZM.png)
Park details page:
![API Park details preview](https://i.imgur.com/Y3S4Go3.png)

# Usage
Before begin specify your PostgreSQL parameters in `config.py` file.

## Starting Opendata Parks table parser

	$ python3 main.py

## Starting Django API server

	$ cd parks-api
	
	$ python3 manage.py migrate
	$ python3 manage.py runserver
