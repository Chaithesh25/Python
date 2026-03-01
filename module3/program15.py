import pandas as pd

# Create employee data
data = {
    "Name": ["Rahul", "Sneha", "Arjun", "Priya", "Kiran", "Meena"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Salary": [50000, 60000, 55000, 70000, 52000, 65000]
}

df = pd.DataFrame(data)


avg_sal = df.groupby("Department")["Salary"].mean()
print(avg_sal)