# Yelp Dataset Challenge Alexa Skill

## Description
This skill allows Alexa users to receive simple information & reviews about local restaurants and businesses, using [Yelp's dataset challenge data](https://www.yelp.com/dataset_challenge). We used the [nltk](http://www.nltk.org/) library to extract the most important keywords from a review of each business, and wrote the results into a csv file that we then accessed using our AWS lambda function. Responds to the following commands:

Alexa, ask yelp about the rating of {Restaurant}   
Alexa, ask yelp about {Restaurant}   
Alexa, ask yelp about how people feel about {Restaurant}  
Alexa, ask yelp about the rating of the restaurant  
Alexa, ask yelp about the restaurant  
Alexa, ask yelp about people feel about the restaurant
  
## Credits

This skill was created by Akshay Mahajan, Kevin Tan, and Preston Wong at Teradata's Machine Learning & Cognitive Computing Hackathon.
