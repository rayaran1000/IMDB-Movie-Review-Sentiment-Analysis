#Importing Necessery libraries
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass

#Importing Requests
import requests

#Importing BeautifulSoup 
from bs4 import BeautifulSoup

#Importing Logger and Exceptions
from scr.logger import logging
from scr.exceptions import CustomException

@dataclass
class DataIngestionConfig:

    raw_data_path : str = os.path.join('artifacts', 'raw_data.csv') # Raw data file path which contains the data

class DataIngestion:

    def __init__(self):

        self.data_ingestion_config = DataIngestionConfig() 

    def initiate_data_ingestion(self): # Add URL here , but now we are hardcoding the value for initial development

        try:

            # Getting the response from the URL
            response = requests.get("https://www.imdb.com/title/tt4154796/reviews/?ref_=ttexr_ql_2")
            logging.info("Got response from URL")

            #Calling Beautiful Soup to scrape the response content
            soup = BeautifulSoup(response.content,'html.parser')
            
            review_data = soup.findAll(class_="review-container")

            reviews = self.fetching_data(review_data)
            logging.info("Fetching of Reviews completed")

            df = pd.DataFrame(np.array(reviews),columns=['reviews'])

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True) #Creating the 'Aritifacts' folder 

            df.to_csv(self.data_ingestion_config.raw_data_path,index=False) # Saving the Reviews data scraped from the website
            logging.info("Review data saved to csv file from dataframe")

            return (

                    df,
                    self.data_ingestion_config.raw_data_path

                    )

        except Exception as e:
            raise CustomException(e,sys)
        
    def fetching_data(self,data): # Used to fetch the text data from the review container( Will change if other websites are used rather than IMDB User Reviews)

        reviews = [] # List initialization for the reviews data

        for review in data: # Finding the review data after inspecting the HTML element of the webpage

            reviews_content = review.find('div',class_='lister-item-content')
            
            reviews_text = reviews_content.find('div',class_="content")
            
            reviews.append(reviews_text.find('div',class_="text show-more__control").text)

        return reviews


    
