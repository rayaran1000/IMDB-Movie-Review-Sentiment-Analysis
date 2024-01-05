from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from scr.pipelines.prediction_pipeline import PredictionPipeline

application = Flask(__name__)

app=application

#Route for home page

@app.route('/')
def index():
    return render_template('index.html') # Defining the Index Html Page

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html') # Home.html will contain fields for getting out Input fields
    else:
        urlInput = request.form.get('urlInput') # Here we are getting all the Input values from the webpage
        print(urlInput)

        # Calling the PredictPipeline
        predict_pipeline=PredictionPipeline()
        result_df , movie_name = predict_pipeline.predict(urlInput) # Here we are sending the dataframe we created in earlier step for preprocessing and model prediction
        print(result_df)
        return render_template('home.html',results_1=result_df['reviews'],results_2=result_df['sentiment'],results_3=result_df['factuality'],movie_name = movie_name,results_df=result_df) #Since results will be in list format
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True) # Maps with 127.0.0.1