import geocoder
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False


@app.route('/',  methods=['GET', 'POST'])
def hello_world():  # put application's code here
    if request.method == 'POST':
        city = request.form.get("city")
        street = request.form.get("street")
        house = request.form.get("house")
        address = dict(geocoder.osm(f'{house},{street},{city}').json)
        return render_template("main.html", message=f'address = {address["address"]}, x = {address["lat"]}, y = {address["lng"]}')
    return render_template("main.html")


@app.route('/api/<city>')
def get_street(city):
    address = geocoder.osm(f'{city}').json
    return jsonify(adress=address["address"], x=address["lat"], y=address["lng"])


@app.route('/api/<city>/<street>')
def get_city_street(city, street):
    address = dict(geocoder.osm(f'{street},{city}').json)
    return jsonify(adress=address["address"], x=address["lat"], y=address["lng"])


@app.route('/api/<city>/<street>/<house>')
def get_city_street_house(city, street, house):
    address = dict(geocoder.osm(f'{house},{street},{city}').json)
    return jsonify(adress=address["address"], x=address["lat"], y=address["lng"])


if __name__ == '__main__':
    app.run()
