from flask import Flask, render_template, request
import pandas as pd

app=Flask(__name__)
car=pd.read_csv("cleaned-car.csv")

@app.route('/')
def index():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique(), reverse=True)
    fuel_type=car['fuel_type'].unique()
    return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_types=fuel_type)

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    company=request.form.get('company')
    car_model=request.form.get('car_model')
    year=int(request.form.get('year'))
    fuel_type=request.form.get('fuel_type')
    kms_driven=int(request.form.get('kilo_driven'))
    print (company, year, fuel_type, kms_driven, car_model)
    return ""
    

if __name__=="__main__":
    app.run(debug=True)