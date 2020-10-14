# TedTalkAnalyzer
Predicting trends derived by analysis of 3000 TED Talks
Approach

•	Collecting, preprocessing and loading TED Talks dataset.
•	Analyzing dataset for speaker information of a Talk.
•	Mining data for fetching most popular tags in recent years.
•	Filtering data to display it in graphical form based on factors like published year, ratings and tags.
•	Creating K-Nearest Neighbor Algorithm based on the dataset to find is the TED Talk will give positive feedback or negative feedback. 
•	Using Twitter APIs to fetch trending tweets related to TED Talks.
•	Recommending the TED Talks based on KNN algorithm created and pairing it with user inputs.

Libraries Used
•	Pandas (Data frame analysis and manipulation)

•	Seaborn (Statistical data visualization)

•	Sklearn (Machine learning)

•	Numpy (Preprocessing)

•	Matplotlib (Graphs Visualization)

•	tkinter (GUI)


•	Twitter (Twitter Data)

Collection and Preprocessing of Data

The dataset regarding the TED Talk was fetched from CSV file to data frames with help of Pandas library. The dataset contained Published Date and Filmed Data of TED Talks on special format. Available columns from the data were

comments : The number of first level comments made on the talk
description : A blurb of what the talk is about
duration : The duration of the talk in seconds
event : The TED/TEDx event where the talk took place
film_date : The Unix timestamp of the filming
languages : The number of languages in which the talk is available
main_speaker : The first named speaker of the talk
name : The official name of the TED Talk. Includes the title and the speaker.
num_speaker : The number of speakers in the talk
published_date : The Unix timestamp for the publication of the talk on TED.com
ratings : A stringified dictionary of the various ratings given to the talk (inspiring, fascinating, jaw dropping, etc.)
related_talks : A list of dictionaries of recommended talks to watch next
speaker_occupation : The occupation of the main speaker
tags : The themes associated with the talk
title : The title of the talk
url : The URL of the talk
views : The number of views on the talk

To make the mining and analysis of data, the dataset was preprocessed, and it was converted to DD-MM-YY format. For any video to be popular, one of the basic indicators is the number of views it has achieved. We sorted the dataset in decreasing order of the views of TED Talk. Once this was done, we went through dataset about selecting all the parameters of interest that could potentially be important for deriving crucial information from the dataset.
