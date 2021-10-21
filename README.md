# Get coordinates from your address

## Getting started

1. To setup this project, simply run the following command:
```bash
$ pip3 install -r requirements.txt
```

It should download and setup the dependencies and you're good to go! :)

2. All the routes are setup inside `routes/routes.py`. Most of your code should go there.
s
3. To start the project, simply run the following command:
```bash
$ python3 app.py
```
## Api
* Coordinates city:
    * GET http://127.0.0.1:5000/api/yourcity
* Coordinates streetin the city :
    * GET http://127.0.0.1:5000/api/yourcity/yourstreet
* Coordinates house in the street:
    * GET http://127.0.0.1:5000/api/yourcity/yourstreet/yourhouse
