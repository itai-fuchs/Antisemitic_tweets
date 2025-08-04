import pandas as pd
from Loader import Loader
import re


class Cleaner:
    """
           clean table class
    """
    def __init__(self,table):
        self.filtered_table=table[["Text", "Biased"]].copy()


    def remove_punctuation(self):
        """
            remove_punctuation from text
        """
        self.filtered_table["Text"] = self.filtered_table["Text"].str.replace(",", "", regex=False)

    def to_lower(self):
        """
        convert_letter to lower in text
        """
        self.filtered_table["Text"] = self.filtered_table["Text"].str.lower()

    def remove_uncategorized_tweets(self):
        """
            remove_uncategorized_tweets
        """
        self.filtered_table = self.filtered_table[
            self.filtered_table["Biased"].isin([0, 1])
        ]


