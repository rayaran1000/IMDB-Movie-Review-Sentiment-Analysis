#Importing necessary libraries
import sys
import os
from dataclasses import dataclass


#Importing logger,exception and utils
from scr.logger import logging
from scr.exceptions import CustomException
from scr.utils import save_object

#Importing and Downloading nltk library and corpus
import nltk
nltk.download('wordnet')

#Importing Textblob
from textblob import Word

#Importing sklearn library and modules for building Custom Pipeline for Data Cleaning
from sklearn.pipeline import Pipeline,FunctionTransformer
from sklearn.base import BaseEstimator, TransformerMixin


@dataclass
class DataLemmatizerConfig:

    data_lemmatizer_data_path : str = os.path.join('artifacts', 'lemmatizer.pkl') # Lemmatizer pickle file path

class DataLemmatizer:

    def __init__(self):

        self.data_lemmatizer_config = DataLemmatizerConfig() 
        self.data_lemmatizing_transformer = DataLemmatizerTransformer()

    def initiate_data_lemmatizing(self,text_series): # Function to initiate data lemmatization

        lemmatized_data , lemmatizer_object = self.data_lemmatizing_transformer.transform(text_series) # Applying lemmatizer transformer to lemmatize data

        save_object( # Saving the lemmatizer object
            
            file_path=self.data_lemmatizer_config.data_lemmatizer_data_path,
            obj=lemmatizer_object

        )

        return lemmatized_data

class DataLemmatizerFunctions: # Class to define function for lemmatizing data

    def data_lemmatizer(self,text_series):

        return text_series.apply(lambda x: " ".join(Word(word).lemmatize() for word in x.split()))

class DataLemmatizerTransformer(BaseEstimator, TransformerMixin): # Custom transformer to lemmatize data in a pipeline

    def __init__(self):
        
        self.data_lemmatizer_function = DataLemmatizerFunctions()
        
    def fit(self, X, y=None):
        return self

    def transform(self, X): # Lemmatizing pipeline
        
        lemmatizing_pipeline = Pipeline(
            steps=[

                ('lemmatizing', FunctionTransformer(self.data_lemmatizer_function.data_lemmatizer)) #Lemmatizing data
                
            ]
        )

        lemmatized_data = lemmatizing_pipeline.fit_transform(X)
        logging.info("Data lemmatizing pipeline ran successfully")


        return (
            
            lemmatized_data,
            lemmatizing_pipeline

        ) 
