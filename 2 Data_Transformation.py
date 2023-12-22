# Data Transformation


# Concatenate the Data frames vertically to combine prairies cities data
df_prairies = pd.concat([yxe, yyc, yeg, ywg], ignore_index=True)

# Concatenate the Data frames vertically to combine central cities data
df_central = pd.concat([yyz, yul, yqb, yow], ignore_index=True)

# Concatenate cities from prairies and central regions to Vancouver
combined_df = pd.concat([df_central, df_prairies, yvr], ignore_index=True)

# Concatenate provinces
combined_df_provinces = pd.concat([AB, SK, QC, BC, ON, CAN], ignore_index=True)



# Convert 'Date' column to datetime with a specific format
combined_df['Date'] = pd.to_datetime(combined_df['Date'], format='%b %Y', errors='coerce')

# Drop rows with missing 'Date' values
combined_df = combined_df.dropna(subset=['Date'])

# Extract year from the 'Date' column
combined_df['Year'] = combined_df['Date'].dt.year.astype(int)

# Aggregate data by year
agg_df = combined_df.groupby(['Year', 'City']).mean().reset_index()

# Check summary statistics for aggregated data
print("Summary statistics for Popular Cities (Aggregated by Year):")
print(agg_df.describe())


# Check missing values
for key, df in agg_df.items():
    print(f"Missing values in {key}:")
    print(df.isnull().sum())
    print("\n")


# Order cities names
custom_city_order = ['Vancouver', 'Toronto', 'Ottawa', 'Calgary', 'Edmonton', 'Winnipeg', 'Saskatoon', 'Montreal', 'Quebec']

# Convert 'City' column to categorical with custom order
agg_df['City'] = pd.Categorical(agg_df['City'], categories=custom_city_order, ordered=True)

# Sort the DataFrame based on the custom order
agg_df = agg_df.sort_values(by=['City', 'Year'])

print("Unique Cities:", agg_df['City'].unique())
print("Unique Years:", agg_df['Year'].unique())

# Convert 'Date' column to datetime with a specific format
combined_df_provinces['Date'] = pd.to_datetime(combined_df_provinces['Date'], format='%b %Y', errors='coerce')

# Drop rows with missing 'Date' values
combined_df_provinces = combined_df_provinces.dropna(subset=['Date'])

# Extract year from the 'Date' column
combined_df_provinces['Year'] = combined_df_provinces['Date'].dt.year.astype(int)

# Aggregate data by year
agg_df_provinces = combined_df_provinces.groupby(['Year', 'Province']).mean().reset_index()

# Check summary statistics for aggregated data
print("Summary statistics for Provinces and National (Aggregated by Year):")
print(agg_df_provinces.describe())


for key, df in agg_df_provinces.items():
    print(f"Missing values in {key}:")
    print(df.isnull().sum())
    print("\n")


# Order provinces names
custom_province_order = ['Canada', 'British Columbia', 'Ontario', 'Alberta', 'Saskatchewan', 'Quebec']

# Convert 'Province' column to categorical with custom order
agg_df_provinces['Province'] = pd.Categorical(agg_df_provinces['Province'], categories=custom_province_order, ordered=True)

# Sort the DataFrame based on the custom order
agg_df_provinces = agg_df_provinces.sort_values(by=['Province', 'Year'])

print("Unique Province:", agg_df_provinces['Province'].unique())
print("Unique Years:", agg_df_provinces['Year'].unique())
