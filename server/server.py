#http://127.0.0.1:5000/predict_home_price?location=1st Phase JP Nagar&total_sqft=1000&bhk=3&bath=3
from flask import Flask, request, jsonify
from werkzeug.datastructures import MultiDict
import util

app = Flask(__name__)


# @app.route("/favicon.ico")
# def favicon():
#     return "", 200


@app.route("/hello")
def hello():
    return "Hii"


@app.route('/get_location_names', methods=['GET', 'POST'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-control-Allow-Origin', '*')
    print(response)
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    # location = (request.form['location'])
    # print("location is:", location)
    # total_sqft = float(request.form['total_sqft'])
    # bhk = (request.form['bhk'])
    # bath = (request.form['bath'])

    location = (request.form.get('location'))
    print(location)
    total_sqft = (request.form.get('total_sqft'))
    print(total_sqft)
    bath = (request.form.get('bath'))
    print(bath)
    bhk = (request.form.get('bhk'))
    print(bhk)

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bath, bhk)
    })
    response.headers.add('Access-control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting python flask server for Home Price Prediction....")
    app.run(port=5000, debug=True)
