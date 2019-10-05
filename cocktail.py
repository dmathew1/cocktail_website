import flask
import pandas as pd
import numpy as np
import re
from loggers import logger


class Cocktails:

    base = "C:\\Users\\denze\\Desktop\\test\\cocktails_data.csv"

    def __init__(self):
        self.csv = self.readCsv(self.base)
        self.csv = self.splitIngredients()


    def readCsv(self,path):
        self.csv = pd.read_csv(path)
        return self.csv

    def splitIngredients(self):
        for index,row in self.csv.iterrows():
            row['Ingredients'] = row['Ingredients'].split(',')
        return self.csv

    def getDrinkBasedOnIngr(self,reqList):
        ingrSeries = self.csv['Ingredients']
        drinkFrame = pd.DataFrame()
        drinkList = []
        missingList = []
        df = pd.DataFrame()
        for index,ingrList in ingrSeries.items():
            items = set()
            for ingr in ingrList:
                for word in ingr.split():
                    for x in reqList:
                        if x in word:
                            items.add(x)
                            break
            if len(reqList) == len(items):
                df = self.csv.iloc[[index]]
                if not True in [df.equals(x) for x in drinkList]:
                    drinkList.append(df)
                else:
                    missingList.append(ingr)
            df = self.csv.iloc[[index]]
            df['Missing'] = pd.Series(missingList)
        if(len(drinkList) > 0):
            return drinkFrame.append(drinkList)
        return drinkFrame

    def identifyLiquorInEach(self):
        regex = "([A-Z])\w+\s(.*)"
        ingrList = []
        ingrSeries = self.csv['Ingredients']
        for index,value in ingrSeries.items():
            for i in value:
                match = re.search(regex,i)
                if match:
                    ingr = match.group()
                    if ingr not in ingrList:
                        ingrList.append(ingr)
        return ingrList

if __name__ == '__main__':
    limit = 100
    file = "hotaling_cocktails - Cocktails.self.csv"
    self.csv = readCsv(file)
    self.csv = splitIngredients(self.csv.head(limit))
    liquorDict = identifyLiquorInEach(self.csv.head(limit))

    #given ingrList, find drinks that satisfy this, highlighting ingr not listed
    ingrList = ["Lime","Mezcal"]
    drinks = getDrinkBasedOnIngr(ingrList,self.csv)
    print(drinks['Cocktail Name'])
