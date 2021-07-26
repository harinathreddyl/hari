# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
from pickle import load

app = Flask(__name__)

Cat_Boost = load(open('finalized_house.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

    city =request.form.get('city')
    type_of_house = request.form.get('type_of_house')
    status_of_house = request.form.get('Status_of_house')
    type_of_area = request.form.get('type_of_area')
    resale = request.form.get('resale')
    registration = request.form.get('registration')
    bedrooms = request.form.get('bedrooms')
    bathrooms = request.form.get('bathrooms')   
    area_sqft = request.form.get('area_sq.ft')

    bedrooms  = int(bedrooms)
    bathrooms = int(bathrooms) 
    area_sqft = int(area_sqft)
    area_sqft = np.log(area_sqft)
    print(city )
    print(type_of_house)
    print(status_of_house)
    print(type_of_area)
    print(resale)
    print(registration)
    print(bedrooms)
    print(bathrooms)
    print(area_sqft)          
    predictions = Cat_Boost.predict([ city,type_of_house,status_of_house,type_of_area,resale,registration,bedrooms,bathrooms,area_sqft])
    
    predictions = np.exp(predictions)
    

    prediction_text = 'house price is predicted to be :  '+str(predictions)+'cr'


    return render_template('index.html', prediction_text=prediction_text)


# Allow the Flask app to launch from the command line
if __name__ == "__main__":
    app.run(debug=True)
