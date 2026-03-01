import pandas as pd

# Dictionary of lists
data = {
    "Name": ["Rahul", "Asha", "Vijay", "Meena", "Kiran"],
    "Age": [21, 19, 22, 20, 23],
    "Marks": [85, 90, 78, 88, 92]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display first few rows
print("First few rows of the DataFrame:")
print(df.head(1))
