import pandas as pd

#  dataset
df = pd.read_csv('scraped_data.csv')

print("PROJECT ANALYTICS REPORT: DATA HEALTH CHECK ")
print(f"Total entries processed: {len(df)}")

# Data Cleaning
initial_rows = len(df)
df.drop_duplicates(subset=['Headline'], keep='first', inplace=True)
cleaned_rows = len(df)

print(f"Data Cleaning: {initial_rows - cleaned_rows} duplicate headlines removed.")
print(f"Dataset now contains {cleaned_rows} unique, high-quality entries.")

# Save cleane
df.to_csv('cleaned_data.csv', index=False)
print("ANALYSIS COMPLETE: Data saved to 'cleaned_data.csv'")