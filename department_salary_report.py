import pandas as pd

df = pd.read_csv("employees_clean.csv")

report = df.groupby("Department").agg(
    total_employees=("Name", "count"),
    average_salary=("Salary", "mean"),
    max_salary=("Salary", "max")
)

report["average_salary"] = report["average_salary"].round(2)

report.to_csv("department_salary_report.csv")

print("✅ Department Salary Report:")
print(report)