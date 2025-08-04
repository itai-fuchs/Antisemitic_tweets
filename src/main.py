from Loader import Loader
from Cleaner import Cleaner
from Export import Export
from DataAnalyzer import DataAnalyzer




table=Loader("C:/Users/itai/PycharmProjects/Antisemitic_tweets/Data/tweets_dataset.csv").table
filtered_table=Cleaner(table).filtered_table
analyze=DataAnalyzer(table)
export=Export(table,filtered_table)

export.export_filtered_table_to_csv()
export.export_analyze_to_json(analyze.total_tweets(),analyze.average_length(),analyze.common_words(),analyze.longest_3_tweets(),analyze.uppercase_words())
