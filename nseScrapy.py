############### import libraries/packages ###############
import os.path
from datetime import date, datetime
import datetime
from nsepy import get_history
import csv

############### fetch DateTime ###############
currentDT = datetime.datetime.now()

############### fetchData ###############
# symbolCode = input("enter the symbol code")
# symbolCode = 'reliance'
# stockData = get_history(symbol=symbolCode, start=date(2019,3,1), end=date(currentDT.year,currentDT.month,currentDT.day))

# print(stockData.columns)

# print(stockData['Open'])
# print(stockData.tail())
# stockData[['Close']].plot()

############### store historicla data into csv file ###############


def getData(symbolCode):
    stockData = get_history(symbol=symbolCode, start=date(1957, 3, 1),
                            end=date(currentDT.year, currentDT.month, currentDT.day))
    prefix = 'dataOf_'
    suffix = '.csv'
    fileName = prefix + symbolCode + suffix
    # print(fileName)
    with open(os.path.join('dataFiles', fileName), "w") as cFile:
        stockWriter = csv.writer(cFile)
        stockWriter.writerow(stockData.columns)
        for row in stockData.values:
            print(row)
            stockWriter.writerow(row)
    cFile.close()