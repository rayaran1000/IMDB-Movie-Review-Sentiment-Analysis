#Importing necessary libraries
import sys
import os
from dataclasses import dataclass


#Importing logger,exception and utils
from scr.logger import logging
from scr.exceptions import CustomException
from scr.utils import save_object

#Importing Textblob
from textblob import TextBlob

#Importing sklearn library and modules for building Custom Pipeline for Data Cleaning
from sklearn.pipeline import Pipeline,FunctionTransformer
from sklearn.base import BaseEstimator, TransformerMixin

@dataclass
class ModelPredictorConfig:

    model_predictor_data_path : str = os.path.join('artifacts','model.pkl') # Model pickle file path

class ModelPredictor:

    def __init__(self):

        self.model_predictor_config = ModelPredictorConfig()
        self.model_predictor_transformer = ModelPredictorTransformer()

    def initiate_model_prediction(self,text_series): # Function to initiate model prediction

        polarity , subjectivity , model_prediction_pipeline = self.model_predictor_transformer.transform(text_series) # Applying model prediction transformer to lemmatized data

        sentiment = [] # List initialization for sentiment
        factuality = [] # List initialization for factuality

        for i in range(len(text_series)): # Loop to segregate positive and negetive sentiments using polarity
            if list(polarity)[i] > 0:
                sentiment.append('Positive')
            elif list(polarity)[i] < 0:
                sentiment.append('Negetive')
            else:
                sentiment.append('Neutral')

        for i in range(len(text_series)): # Loop to segregate Factual and User Opinion reviews using Subjectivity
            if list(subjectivity)[i] > 0.5:
                factuality.append('Factual Review')
            elif list(polarity)[i] < 0.5:
                factuality.append('User Opinion Review')
            else:
                factuality.append('Balanced Review')

        save_object (

            file_path = self.model_predictor_config.model_predictor_data_path,
            obj= model_prediction_pipeline

        )

        return (

            polarity,
            subjectivity,
            sentiment,
            factuality

        )

    
class ModelPredictorFunctions: # Class to define functions for mode prediction

    def model_predictor(self,text_series):

        return (
            
            text_series.apply(lambda x: TextBlob(x).sentiment[0]), #Polarity

            text_series.apply(lambda x: TextBlob(x).sentiment[1])  #Subjectivity

        )
    

class ModelPredictorTransformer(BaseEstimator,TransformerMixin):  # Custom transformer to predict in a pipeline

    def __init__(self):

        self.model_predictor_functions = ModelPredictorFunctions()

    def fit(self,X,y=None):
        
        return self
    
    def transform(self,X): # Model Prediction Pipeline
        
        model_prediction_pipeline = Pipeline(
            steps = [

                ('model_prediction',FunctionTransformer(self.model_predictor_functions.model_predictor))

            ]
        )

        polarity , subjectivity = model_prediction_pipeline.fit_transform(X)
        logging.info("Model Prediction Pipeline ran successfully")

        return(

            polarity,
            subjectivity,
            model_prediction_pipeline

        )

    