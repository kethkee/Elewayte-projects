import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('HR analytics - Sheet1.csv')
df.columns = df.columns.str.strip()
print(df.head())

gender_counts = df['Gender'].value_counts()
print(gender_counts)

gender_department = df.groupby('Department')['Gender'].value_counts()
gender_location = df.groupby('Loc')['Gender'].value_counts()
print(gender_department)
print(gender_location)

# Clean the Salary column
df['Salary'] = df['Salary'].replace({'\$': '', ',': ''}, regex=True).str.strip()
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

average_salary_department = df.groupby('Department')['Salary'].mean()
highest_avg_salary_department = average_salary_department.idxmax()
print(f"\nDepartment with highest average pay: {highest_avg_salary_department}")
print(average_salary_department)

average_salary_location = df.groupby('Loc')['Salary'].mean()
highest_avg_salary_location = average_salary_location.idxmax()
print(f"\nLocation with highest average pay: {highest_avg_salary_location}")
print(average_salary_location)

rating_counts = df['Rating'].value_counts()
rating_percentages = (rating_counts / len(df)) * 100
print(rating_percentages)

pay_gap_department = df.groupby(['Department', 'Gender'])['Salary'].mean().unstack()
pay_gap_department['Gap'] = (pay_gap_department['Male'] - pay_gap_department['Female']) / pay_gap_department['Male'] * 100
print(pay_gap_department)

pay_gap_location = df.groupby(['Loc', 'Gender'])['Salary'].mean().unstack()
pay_gap_location['Gap'] = (pay_gap_location['Male'] - pay_gap_location['Female']) / pay_gap_location['Male'] * 100
print(pay_gap_location)

sns.countplot(x='Gender', data=df)
plt.title('Gender Distribution')
plt.show()

sns.countplot(x='Department', hue='Gender', data=df)
plt.title('Gender Distribution by Department')
plt.show()

sns.countplot(x='Loc', hue='Gender', data=df)
plt.title('Gender Distribution by Location')
plt.show()

sns.scatterplot(x='Loc', y='Salary', hue='Gender', data=df)
plt.title('Salary Distribution by Location')
plt.show()

sns.scatterplot(x='Department', y='Salary', hue='Gender', data=df)
plt.title('Salary Distribution by Department')
plt.show()
