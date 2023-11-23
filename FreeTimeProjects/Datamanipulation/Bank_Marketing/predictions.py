import pandas

df = pandas.read_csv("training_data/whole_dataset.csv")
unique_df = df.drop_duplicates()

to_CSV = unique_df
to_CSV.to_csv("training_data/unique_data.csv", index=False)


print(unique_df)