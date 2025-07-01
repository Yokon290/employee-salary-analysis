import pandas as pd

df = pd.read_csv("employees_dirty.csv")

df = df.drop_duplicates()

df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

df["Name"] = df["Name"].str.title()
df["Department"] = df["Department"].str.upper()

df = df.dropna(subset=["Name", "Salary"])

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df = df.dropna(subset=["Salary"])

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"], errors="coerce")

df.to_csv("employees_clean.csv", index=False)

print("✅ Cleaned data saved to employees_clean.csv")