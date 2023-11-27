import os
import pandas
import xlwings as xw


# Check if there is a file called unique_data
if os.path.isfile("training_data/unique_data.csv") is False:
    # This was for Excel.
    df = pandas.read_csv("training_data/whole_dataset.csv")
    unique_df = df.drop_duplicates()

    to_CSV = unique_df
    to_CSV.to_csv("training_data/unique_data.csv", index=False)

# Following goal was to predict specific values that were given in Excel.
# Works here just fine but when this script is run/executed from Excel ->
# It does not insert the value to the colum

# Get data from excel
ws = xw.Book("Excel/bank_marketing.xlsx").sheets['Dashboard']
#wb = xw.Book.caller()
# Selecting data from the Excel
v1 = ws.range("A44:M44").value
ws["A51"].value = v1[0]


