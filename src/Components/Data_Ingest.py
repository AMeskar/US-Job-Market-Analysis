from abc import ABC, abstractmethod
import pandas as pd
import os

class DataIngest(ABC):

    def DataIngestFunction(folder_path) -> str:

        abstractmethod

        '''
         abstract class

        '''

        pass

class ListData(DataIngest) :

    def DataIngestFunction(folder_path) -> list:

        abstractmethod

        '''
         Take the folder path and list the files

        '''

        List_file = [f for f in os.listdir(folder_path)]

        return List_file

class ListtoFDataFrame(DataIngest):

    def DataIngestFunction(folder_path) -> list:

        abstractmethod

        '''
         Take the list file and transform it into one data frame

        '''

        list_file = ListData.DataIngestFunction(folder_path)

        df =pd.concat([pd.read_csv(folder_path + '/' +f, low_memory= False, encoding='cp1252') for f in list_file], ignore_index= True) 

        return df

"""if __name__=='__main__':

    folder_path = '/Users/meskara/Desktop/Github/Job_Market/src/Notebook/Data'

    df = ListtoFDataFrame.DataIngestFunction(folder_path= folder_path)

    print(df)"""

