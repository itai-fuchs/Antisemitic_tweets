import pandas as pd
from Loader import Loader
import re


class Cleaner:

    def __init__(self,table):
        self.filtered_table=table[["Text", "Biased"]].copy()



    def Removing_punctuation(self):
        self.filtered_table["Text"] = self.filtered_table["Text"].str.replace(",", "", regex=False)

    def to_lower(self):
        self.filtered_table["Text"] = self.filtered_table["Text"].str.lower()

    def Remov_uncategorized_tweets(self):
        self.filtered_table = self.filtered_table[
            self.filtered_table["Biased"].isin([0, 1])
        ]


a=Loader("C:/Users/itai/PycharmProjects/Antisemitic_tweets/Data/tweets_dataset.csv").table
b=Cleaner(a)
b.Remov_uncategorized_tweets()
b.Removing_punctuation()
b.to_lower()
print(b.filtered_table["Text"].head())
