import pandas as pd
import os



class Loader:
    """
    A class to convert various file formats into df.
    """

    def __init__(self, file_path):

        self.file = file_path
        self.extension = os.path.splitext(file_path)[-1].lower()
        self.table = self.load_file()


    def load_file(self):
        """
        Detect the file type and load it as a pandas DataFrame.
        """

        if self.extension == ".csv":
            df = pd.read_csv(self.file)
        elif self.extension == ".json":
            df = pd.read_json(self.file)
        elif self.extension in [".xls", ".xlsx"]:
            df = pd.read_excel(self.file)
        elif self.extension == ".txt":
            df = pd.read_csv(self.file, delimiter="\t")
        elif self.extension == ".html":
            df = pd.read_html(self.file)[0]

        return df


a=Loader("../Data/tweets_dataset.csv")
print(a.table)