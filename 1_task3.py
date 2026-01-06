import pandas as p

df = p.read_csv(r"C:\Users\sad\.vscode\Python VScode\TASKS\Task1\data.csv")
df["city"]=df["city"].fillna(df["city"].mode()[0])
df = df.fillna(df.mean(numeric_only=True))

print("\nData after filling missing values with mean:")
print(df)

