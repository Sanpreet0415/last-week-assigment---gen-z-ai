import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('burglary_data.csv')

# Display the first few rows of the dataframe
print(df.head())

# Total burglary cases per state
cases_per_state = df.groupby('State')['Cases'].sum().sort_values(ascending=False)
print("\nTotal Burglary Cases Per State:")
print(cases_per_state)

# Total value of property recovered per state
value_per_state = df.groupby('State')['Property_Recovered_Value'].sum().sort_values(ascending=False)
print("\nTotal Value of Property Recovered Per State:")
print(value_per_state)

# Visualization: Total Burglary Cases Per State
plt.figure(figsize=(12, 6))
cases_per_state.plot(kind='bar', color='skyblue')
plt.title('Total Burglary Cases Per State')
plt.xlabel('State')
plt.ylabel('Total Cases')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Visualization: Total Value of Property Recovered Per State
plt.figure(figsize=(12, 6))
value_per_state.plot(kind='bar', color='lightgreen')
plt.title('Total Value of Property Recovered Per State')
plt.xlabel('State')
plt.ylabel('Total Value (₹)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Insights by Year
cases_by_year = df.groupby('Year')['Cases'].sum()
value_by_year = df.groupby('Year')['Property_Recovered_Value'].sum()

# Visualization: Burglary Cases and Property Recovered Value by Year
fig, ax1 = plt.subplots(figsize=(14, 7))

ax1.set_xlabel('Year')
ax1.set_ylabel('Total Cases', color='tab:blue')
ax1.plot(cases_by_year.index, cases_by_year.values, color='tab:blue', marker='o', label='Total Cases')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Total Value (₹)', color='tab:orange')
ax2.plot(value_by_year.index, value_by_year.values, color='tab:orange', marker='o', label='Total Value')
ax2.tick_params(axis='y', labelcolor='tab:orange')

plt.title('Burglary Cases and Property Recovered Value by Year')
fig.tight_layout()
plt.show()
