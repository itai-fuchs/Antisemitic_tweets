from Cleaner import Cleaner
import pandas as pd
from Loader import Loader
from DataAnalyzer import DataAnalyzer
import json

class Export:
    """
    export analyze json file and filtered csv file.
    """
    def __init__(self,table,filtered_table):
        self.table=table
        self.filtered_table=filtered_table

    def export_filtered_table_to_csv(self):
        self.filtered_table.to_csv("C:/Users/itai/PycharmProjects/Antisemitic_tweets/results/tweets_dataset_cleaned.csv")


    def export_analyze_to_json(self,total_tweets,average_length,common_words,longest_3_tweets,uppercase_words):
        json_path="C:/Users/itai/PycharmProjects/Antisemitic_tweets/results/results.json"
        json_data={"total tweets":total_tweets,
           "average length":average_length,
           "common_words":common_words,
           "longest 3 tweets":longest_3_tweets,
           "uppercase_words":uppercase_words
           }

        with open(json_path,"w") as file:
           json.dump(json_data,file)






