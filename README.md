# Xpiri's Data Science Portfolio

Welcome to my portfolio of data science projects! I finally decided to post here some of the stuff I have worked on over the past couple of months. After all, **done > perfect**! This page will be populated quite slowly, as I can only work on these kind of projects on the weekends. 



Everyone loves well-made plots! At least I do, that's why every project on this overview page has its own data visualization :eyes: highlight.

All the different **datasets** used for these projects are **properly documented** both in the respective section of this readme file and inside the notebooks themselves. 

The necessary packages can be downloaded via the requirements.txt file. I made sure not to use any (soon-to-be) deprecated functions, so hopefully there will be no reproducibility issues! 

# Contents 

* :computer: **Machine and Deep Learning projects**

  * NLP: :newspaper: [Fake news detection](FakeNewsClassification) model with ~99% accuracy
    * Exploratory data analysis
    * Model built with tensorflow's functional API
    * Joint modeling of text (GRU, BERT) and categorical features 
    * Transfer learning: fine-tuning a pre-trained BERT model from the hugging face library
    * Data: fake news competition (https://www.kaggle.com/competitions/fake-news/data)

<p align="center">
  <img src="/Plots/fn_model.png" width="800">
</p>

  * NLP: :e-mail: [Spam detection](SMS_spam_classification) with 98% accuracy
    * Exploratory data analysis 
    * Baseline ML methods (Naive Bayes, SVM)
    * Sequential LSTM and GRU models
    * Data: SMS spam collection dataset(https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
<p align="center">
  <img src="/Plots/spam_cm_lstm.png" width="400">
</p>

* :bar_chart: **Data Visualization and Analyses**
  * NLP and time series: :chart_with_downwards_trend: [Sentiment analysis of twitter data](https://github.com/Xpiri/Xpiri-Data-Science-Portfolio/tree/main/Sentiment%20analysis%20of%20twitter%20data) about Ukraine and Russia over Dec. 2021 - Mar. 2022
    * Time series analysis of the evolution of tweets sentiment before and after the Russian invasion of Ukraine
    * Data: see the twitter-scraper notebook! Note: only a subset of the total tweets (2500/day) were used!
 
<p align="center">
  <img src="/Plots/sent_rus_ukr_plot.png" width="800">
</p>
 
 * Data visualization: :world_map: [A map of tweets](Map_of_Ukraine_tweets) about Ukraine
    * Maps of tweets mentioning Ukraine before and after the Russian invasion 
    * Data: see the twitter-scraper notebook!
 <p align="center">
  <img src="/Plots/tweet_map.png" width="1000">
</p>
:e-mail: If you're interested in knowing more about any of the above projects, **shoot me an email** at *federicopanero15@gmail.com* ! 
