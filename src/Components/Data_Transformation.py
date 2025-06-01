from abc import ABC, abstractmethod
import pandas as pd

class DataTransformation(ABC):

    def DataInspection(df):

        """
        
        """

        pass

class DuplicateData(DataTransformation):

    def DataInspection(df):

        """
        
        """

        df = df.drop_duplicates().sort_index()

        return df

class LowercasseData(DataTransformation):

    def DataInspection(df):

        """
        
        """

        for col in df.columns:

            if df[col].dtype == 'object':

                df[col] = df[col].str.lower()

        return df

class DataFrame:

    def Ingest(df):

        df_new = LowercasseData.DataInspection(DuplicateData.DataInspection(df))

        return df_new
    

"""if __name__=='__main__':

    data_analyst = pd.read_csv('/Users/meskara/Desktop/Github/Job_Market/src/Notebook/Data/CSVdataAnalyst.csv', encoding='cp1252')
    
    df_new = DataFrame.Ingest(data_analyst)

    print(df_new)"""