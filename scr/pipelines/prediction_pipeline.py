#Importing Logger and Exceptions
from scr.logger import logging
from scr.exceptions import CustomException

#Importing data ingestion , data cleaner , data transformation and model predictor modules
from scr.components.data_ingestion import DataIngestion
from scr.components.data_cleaner import DataCleaning
from scr.components.data_transformation import DataLemmatizer
from scr.components.model_predictor import ModelPredictor

class PredictionPipeline:

    def __init__(self):
        pass

    def predict(self,URL):
        
        data_ingestion = DataIngestion()
        
        review_dataframe,movie_name = data_ingestion.initiate_data_ingestion(URL)
        
        data_cleaning = DataCleaning()
        
        cleaned_reviews = data_cleaning.initiate_data_cleaning(review_dataframe['reviews'])
        
        data_lemmatizing = DataLemmatizer()
        
        lemmatized_reviews = data_lemmatizing.initiate_data_lemmatizing(cleaned_reviews)

        model_predictor = ModelPredictor()

        polarity , subjectivity , sentiment , factuality = model_predictor.initiate_model_prediction(lemmatized_reviews)

        review_dataframe['polarity'] = polarity
        review_dataframe['sentiment'] = sentiment
        review_dataframe['subjectivity'] = subjectivity
        review_dataframe['factuality'] = factuality

        return(
            
            review_dataframe,
            movie_name
            
            )

if __name__ == '__main__':

    predict_pipeline = PredictionPipeline()

    df = predict_pipeline.predict(URL="https://www.imdb.com/title/tt1375666/reviews/?ref_=tt_ql_2")

    print(df)