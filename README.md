
# IMDB Movie User Review Sentiment Analysis

### Primary objective
1. Web Scraping User Reviews: Extract user reviews from the IMDB website efficiently and accurately.
2. Tabular Format Generation: Organize the scraped reviews into a structured tabular format for easy analysis and presentation.

### Secondary objective
1. Sentiment Analysis: Determine the sentiment of each user review, categorizing them as either positive or negative.
2. Factuality Classification: Differentiate between reviews based on factual information and those expressing subjective opinions.
3. Accuracy and Precision: Ensure high accuracy in scraping reviews and classifying sentiment and factuality to enhance the reliability of the generated data.
4. Scalability: Design the solution to handle a large volume of reviews effectively for future scalability.
5. User-Friendly Output: Present the tabular format in a user-friendly manner, making it easy for stakeholders to interpret and analyze the data.
6. Automation: Implement automation in the web scraping process to facilitate regular and efficient updates to the review dataset.


## Directory Structure 

```plaintext
/project
│   README.md
│   requirements.txt
|   exceptions.py
|   logger.py
|   utils.py
|   application.py
|   setup.py
|   Webpage
└───artifacts
|   └───model.pkl
|   └───lemmatizer.pkl
|   └───cleaner.pkl
|   └───raw_data.csv
└───logs
└───notebook
|       Data Scraping , Analysis, Cleaning and Model Training.ipynb   
└───scr
|   └───components
|       └───data_ingestion.py
|       └───data_cleaner.py
|       └───data_transformation.py
|       └───model_predictor.py
|   └───pipelines
|       └───prediction_pipeline.py
└───templates
|   └───home.html
|   └───index.html

```
## Installation

For Installing the necessery libraries required 

```bash
  pip install -r requirements.txt
```
    
## Deployment

To deploy this project run

1. To start the prediction pipeline 

```bash
  python scr/pipelines/prediction_pipeline.py
```

2. Once the model is trained, to run the Flask application

```bash
  python application.py
```

3. Go to 127.0.0.1/predictdata to get the webpage

4. Go to IMDB website and the respective page for your Movie and copy the URL and place it in the placeholder of the webpage

5. Use Ctrl + C in terminal to stop the server 

## Steps to get the Movie Review URL

1. Open the IMDB Website

![IMDB Webpage](https://github.com/rayaran1000/Movie-Review-Sentiment-Analysis/assets/122597408/2e372e82-1db4-4374-b49e-b1f36a42f346)


2. Search the Movie you want your reviews on :

![Searchbar](https://github.com/rayaran1000/Movie-Review-Sentiment-Analysis/assets/122597408/bed1500f-0471-4107-8e1b-2683b9cd7f73)


3. Go to the user review section of the movie highlighted below

![User Review](https://github.com/rayaran1000/Movie-Review-Sentiment-Analysis/assets/122597408/99da8b73-4fe3-4d65-acd3-8e1e5630d928)


4. Copy the URL of the User Review section page of the movie

![URL](https://github.com/rayaran1000/Movie-Review-Sentiment-Analysis/assets/122597408/b1c192e6-058a-47f8-b35f-9d167aa55be2)

## Exploratory Data Analysis Path followed:


> 1. Scrapping the data from the website ( Movie Name and User Reviews)

> 2. Converting the data into a dataframe

> 3. Get Word count of each review

> 4. Get character count of each review

> 5. Calculate average length of a word for each review

> 6. Calculate stopword count and rate for each review


## Review Data Cleaning

> 1. Converting reviews to lower case

> 2. Removing Punctuations

> 3. Removing stopwords

> 4. Removing Recurring words that don't contribute any real meaning

## Model Prediction

> 1. Performed Lemmatization using Word function of TextBlob

> 2. Calculating Polarity and Subjectivity using TextBlob

## Acknowledgements

I would like to express my gratitude to the following individuals and resources that contributed to the successful completion of this Salees Forecasting project:

- **[IMDB]**: Special thanks to IMDB for providing access to the user reviews and valuable insights into the industry challenges.

- **Open Source Libraries**: The project heavily relied on the contributions of the open-source community. A special mention to libraries such as nltk, pandas, and TextBlob, which facilitated data analysis, model development, and visualization.

- **Online Communities**: I am grateful for the support and knowledge shared by the data science and machine learning communities on platforms like Stack Overflow, GitHub, and Reddit.

This project was a collaborative effort, and I am grateful for the support received from all these sources.


