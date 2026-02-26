import pandas as pd
import matplotlib.pyplot as plt

# Load dataset from CSV
df = pd.read_csv("students.csv")

print("Student Data:")
print(df)

# Calculate average marks
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

print("\nAverage Marks:")
print(df[["Name", "Average"]])

# Find top performer
top_student = df.loc[df["Average"].idxmax()]

print("\nTop Performer:")
print(top_student)

# Save updated file
df.to_csv("updated_students.csv", index=False)

# Plot average marks
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")
plt.show()