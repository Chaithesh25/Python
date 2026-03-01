import pandas as pd

# Create employee salary data
data = {
    "Name": ["Rahul", "Sneha", "Arjun", "Priya", "Kiran"],
    "Salary": [50000, 60000, 55000, 70000, 52000]
}

df = pd.DataFrame(data)

mean_salary = df["Salary"].mean()
mediean_salary = df["Salary"].median()
mode_salary = df["Salary"].mode()[0]
std_dv = df["Salary"].std()
variance_salary = df["Salary"].var()


print(mean_salary)
print(mean_salary)
