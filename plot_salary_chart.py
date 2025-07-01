import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("department_salary_report.csv")

plt.figure(figsize=(8, 5))
plt.bar(df["Department"], df["average_salary"])

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary ($)")
plt.tight_layout()

plt.show()