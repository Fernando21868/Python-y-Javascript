import os
import census2010

population=0

for state in census2010.allData:
    for county in census2010.allData[state]:
        population+=census2010.allData[state][county]['pop']

print(population)