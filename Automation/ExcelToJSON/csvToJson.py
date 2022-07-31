import json,csv

with open ("sample.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({"segment":row[0],
                     "country":row[1],
                     "product":row[2]})

with open ("sample.json","w") as f:
    json.dump(data,f,indent=4)

# import pandas as pd
# filePath = r"/Users/virajsabhaya/Library/CloudStorage/OneDrive-UniversityofTexasatArlington/Documents/MyPersonalProject/PyChallenges/Automation/ExcelToJSON/FinancialSample.xlsx"
# df = pd.read_excel(filePath)
# segment = df.Segment
# country = df.Country
# product = df.Product
# discount = df.DiscountBand
# unitsSold = df.UnitsSold
# jsonContainer = {}
# x = 0
# while x < len(segment):
#     jsonContainer[segment[x]] = [
#         {"segment: ": segment[x], },
#         {"country: ": country[x], },
#         {"product: ": product[x], },
#         {"discount: ": discount[x], },
#         {"unitsSold: ": unitsSold[x]}
#     ]
#     x = x+1
# dF = pd.DataFrame(jsonContainer)
# print(dF)


# from excel2json import convert_from_file
# xlFile = '/Users/virajsabhaya/Library/CloudStorage/OneDrive-UniversityofTexasatArlington/Documents/MyPersonalProject/PyChallenges/Automation/ExcelToJSON/FinancialSample.xlsx'
# convert_from_file(xlFile)