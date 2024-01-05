#Importing Numpy and Pandas
import numpy as np
import pandas as pd

#Importing logger,exception and utils
from scr.logger import logging
from scr.exceptions import CustomException
from scr.utils import save_object

#Importing other necessary libraries
import sys
import os
import string
from dataclasses import dataclass


#Importing and Downloading nltk library and corpus
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

#Importing sklearn library and modules for building Custom Pipeline for Data Cleaning
from sklearn.pipeline import Pipeline,FunctionTransformer
from sklearn.base import BaseEstimator, TransformerMixin

@dataclass
class DataCleaningConfig:

    data_cleaner_data_path : str = os.path.join('artifacts', 'cleaner.pkl') # Cleaner pickle file path

class DataCleaning:

    def __init__(self):

        self.data_cleaner_config = DataCleaningConfig()
        self.data_cleaning_transformer = DataCleaningTransformer()
 
    def initiate_data_cleaning(self,text_series): # Function to initiate data cleaning

        try:
            
            
            cleaned_data , cleaner_object = self.data_cleaning_transformer.transform(text_series) # Applying cleaner transformer to lemmatize data

            save_object(
            
                file_path=self.data_cleaner_config.data_cleaner_data_path,
                obj=cleaner_object

            )

            return cleaned_data
        
        except Exception as e:
            raise CustomException(e,sys)
    
class DataCleanerFunctions: # Class to define functions for cleaning data

    def lower_case_converter(self,text_series): # Function to convert series to lower case

        return text_series.apply(lambda x: " ".join(word.lower() for word in x.split()))

    def punctuation_remover(self,text_series): # Function to remove punctuations from text

        translator = str.maketrans('', '', string.punctuation)
        return text_series.translate(translator)

    def stopword_remover(self,text_series):# Function to remove stopwords from series

        stop_words = stopwords.words('english')
        return text_series.apply(lambda x: " ".join(word for word in x.split() if word not in stop_words))


class DataCleaningTransformer(BaseEstimator, TransformerMixin): # Custom transformer to clean data in a pipeline

    def __init__(self):
        
        self.data_cleaner_function = DataCleanerFunctions()
        
    def fit(self, X, y=None):
        return self

    def transform(self, X): # Cleaning pipeline
        
        cleaning_pipeline = Pipeline( 
            steps=[

                ('lower_casing', FunctionTransformer(self.data_cleaner_function.lower_case_converter)), # Lower casing data
                ('remove_punctuations', FunctionTransformer(lambda x: x.apply(self.data_cleaner_function.punctuation_remover))), # Applied to each word , since the function cant be applied to the series as whole
                ('remove_stopwords', FunctionTransformer(self.data_cleaner_function.stopword_remover)) # Stopword removing from data
                
            ]
        )

        cleaned_data = cleaning_pipeline.fit_transform(X)
        logging.info("Data cleaning pipeline ran successfully")


        return (
            
            cleaned_data,
            cleaning_pipeline

        ) 
    











