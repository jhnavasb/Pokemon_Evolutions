# Pokemon_Evolutions
Django application to retrive information related to Pokemon evolutions

## First steps
Clone the git
Install python requirements:
```sh
cd .\Pokemon_Evolutions\
pip install -r requirements.txt .
```
Run the db/model initializer:
```sh
.\initialize.bat
```

## Application
Run the server
```sh
python manage.py runserver 8080
```
Access "http://127.0.0.1:8080/pokemon-name", where "pokemon-name" is whichever pokemon available on the PokeApi
Example: "http://127.0.0.1:8080/eevee"

If you want to fetch and store the data from the PokeApi using the evolution chain id, use the following command
```sh
python manage.py evo id
```
If you want to fill the database with all the available ids, use the following command
```sh
python manage.py fill
```




