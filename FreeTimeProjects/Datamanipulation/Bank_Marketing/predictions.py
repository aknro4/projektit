import pandas
import xlwings as xw

# df = pandas.read_csv("training_data/whole_dataset.csv")
# unique_df = df.drop_duplicates()

# to_CSV = unique_df
# to_CSV.to_csv("training_data/unique_data.csv", index=False)

# Get data from excel
ws = xw.Book("Excel/bank_marketing.xlsx").sheets['Dashboard']
#wb = xw.Book.caller()
# Selecting data from the Excel
v1 = ws.range("A44:M44").value
ws["A51"].value = v1[0]


