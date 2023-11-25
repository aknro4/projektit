import pandas
import xlwings as xw

# df = pandas.read_csv("training_data/whole_dataset.csv")
# unique_df = df.drop_duplicates()

# to_CSV = unique_df
# to_CSV.to_csv("training_data/unique_data.csv", index=False)


def get_data_from_excel():
    # Get data from excel
    ws = xw.Book("Excel/bank_marketing.xlsx").sheets['Dashboard']

    # Selecting data from the Excel
    v1 = ws.range("A44:M44").value

    return v1
