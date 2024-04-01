# the fast api offline template

## Configuration of Environment On Line
1. install the requirements by `pip install -r requirements`


## Configuration of Environment Off Line
1. collection requirements: `pip freeze > requirements.txt`
2. download offline packages : `pip download -r requirements.txt -d ./offline`
3. install requirements offline : `pip install --no-index --find-links=./offline -r requirements.txt ` 

## Set the DbModel with DbFirst
if you use DbFirst you may need auto generate the model code for sqlarchemy.
so you can use this command line: `sqlacodegen mysql+mysqlconnector://username:password@localhost/dbname`

## start your dev
write the data layer and logic layer
include the service and export with webapi

you can run server with : `uvicorn main:app --reload`
