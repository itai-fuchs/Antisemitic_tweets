import  pandas as pd
from Loader import Loader
import numpy as np
class DataAnalyzer:
    """
    Data analysis of Twitter tweets
    with an emphasis on anti-Semitic tweets
    """
    def __init__(self,table):

        self.table =table
        self.antisemitic =(self.table [self.table["Biased"]==1])
        self.non_antisemitic =(self.table[self.table["Biased"] == 0])


    def total_tweets(self):
        """
        Count the number of tweets by classification
        """
        total= self.table.shape[0]

        return {"antisemitic":self.antisemitic.shape[0],
                "non_antisemitic":self.non_antisemitic.shape[0],
                "unspecified":total-self.antisemitic.shape[0]-self.non_antisemitic.shape[0],
                "total":total}

    def average_length(self):
        """
        Calculate average length of tweets by classification
        """
        antisemitic_word=self.antisemitic["Text"].str.split()
        antisemitic_avg=sum(antisemitic_word.str.len())/self.antisemitic.shape[0]

        non_antisemitic_word=self.non_antisemitic["Text"].str.split()
        non_antisemitic_avg=sum(non_antisemitic_word.str.len()) / self.non_antisemitic.shape[0]

        total_word=self.table["Text"].str.split()
        total_avg=sum(total_word.str.len()/self.table.shape[0])
        return {
        "antisemitic": antisemitic_avg,
        "non_antisemitic":non_antisemitic_avg,
        "total":total_avg
        }

    def longest_3_tweets(self):
        """"
        Calculates the 3 longest tweets
        """
        longest_text_index = (self.antisemitic["Text"]).str.len().idxmax()
        total = self.table["Text"][longest_text_index]
        return len(total)


    def common_words(self):
        """"
        Finds the 10 most common words in tweets
        """
        return

    def uppercase_words(self):
        """"
        Finds the number of words in uppercase letters by classification
        """
        return

# a=Loader("C:/Users/itai/PycharmProjects/Antisemitic_tweets/Data/tweets_dataset.csv").table
# b=DataAnalyzer(a).table
#
# # t=b["Text"].str.len().sort_values(ascending=False,ignore_index=True)
# # x=b["Text"][0]
# print(b["Text"][len(b["Text"])==924])
