import pandas as p

file = p.read_csv("data.csv")
file= file.fillna(0)
file.to_csv("cleaned_file.csv", index=False)
print("Summary Exported")

