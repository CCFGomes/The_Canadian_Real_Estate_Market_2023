# 3 Temporal trends analyses

# 3.1 Historical Overview of Home Price Index (HPI) - National and Provinces (2005-2023)

# Set the palette
sns.set_palette("bright")

# Plotting the aggregated data
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Composite_HPI_SA', hue='Province', data=agg_df_provinces, marker='o')

plt.xlabel('Year', fontsize = 16)
plt.ylabel('Average Home Price Index (HPI)', fontsize = 16)
plt.title('Historical Overview of Home Price Index (HPI) - National and Provinces (2005-2023)', fontsize = 16)

# Set ticks for all years
plt.xticks(agg_df_provinces['Year'].unique())

# Add horizontal grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Increase the number of ticks on the y-axis
plt.yticks(np.arange(agg_df_provinces['Composite_HPI_SA'].min(), agg_df_provinces['Composite_HPI_SA'].max(), 10))

# Format y-axis ticks as integers
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

# Move the legend to the right outside the plot
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left')
plt.tight_layout()
plt.show()



# 3.1.1 Calculate HPI variations over the years

# Filter data for the year 2023
df_2023_provinces = agg_df_provinces[agg_df_provinces['Year'] == 2023]

# Calculate HPI variation for each city
initial_hpi_2005_provinces = agg_df_provinces.groupby('Province')['Composite_HPI_SA'].min()
final_hpi_2023_provinces = df_2023_provinces.groupby('Province')['Composite_HPI_SA'].max()
hpi_variation_provinces = final_hpi_2023_provinces - initial_hpi_2005_provinces

# Calculate percentage increase in HPI
hpi_percentage_increase_provinces = (hpi_variation_provinces / initial_hpi_2005_provinces) * 100

# Find the city with the highest HPI variation
province_highest_variation = hpi_variation_provinces.idxmax()
highest_variation_value_provinces = hpi_variation_provinces.max()

# Extract HPI values for each city in 2023
hpi_2023_provinces = df_2023_provinces.set_index('Province')['Composite_HPI_SA']

# Find the city with the highest HPI in 2023
province_highest_hpi_2023 = hpi_2023_provinces.idxmax()
highest_hpi_2023_value_provinces = hpi_2023_provinces.max()

# Rank cities based on HPI variation, HPI in 2023, and HPI percentage increase
ranked_provinces = pd.DataFrame({
    'Initial_HPI_2005_Provinces': initial_hpi_2005_provinces,
    'HPI_Variation_Provinces': hpi_variation_provinces,
    'HPI_Percentage_Increase_Provinces': hpi_percentage_increase_provinces,
    'HPI_2023_Provinces': hpi_2023_provinces
}).sort_values(by=['HPI_Percentage_Increase_Provinces', 'HPI_2023_Provinces'], ascending=[False, False])

# Format the percentage values
ranked_provinces['HPI_Percentage_Increase_Provinces'] = ranked_provinces['HPI_Percentage_Increase_Provinces'].map('{:.2f}%'.format)

# Print results
print(f"Province with the highest HPI variation: {province_highest_variation} ({highest_variation_value_provinces:.2f})")
print(f"Province with the highest HPI in 2023: {province_highest_hpi_2023} ({highest_hpi_2023_value_provinces:.2f})")
print("\nRanking of provinces based on HPI variation, HPI in 2023, and HPI Percentage Increase:")
print(ranked_provinces)


# 3.2 Historical Overview of Home Price Index (HPI) Across Cities (2005-2023)

# Set the palette 
sns.set_palette("bright")

# Plotting the aggregated data
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Composite_HPI_SA', hue='City', data=agg_df, marker='o')

plt.xlabel('Year', fontsize = 16)
plt.ylabel('Average Home Price Index (HPI)', fontsize = 16)
plt.title('Historical Overview of Home Price Index (HPI) Across Cities (2005-2023)', fontsize = 16)

# Set ticks for all years
plt.xticks(agg_df['Year'].unique())

# Add horizontal grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Increase the number of ticks on the y-axis
plt.yticks(np.arange(agg_df['Composite_HPI_SA'].min(), agg_df['Composite_HPI_SA'].max(), 10))

# Format y-axis ticks as integers
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

# Move the legend to the right outside the plot
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left')
plt.tight_layout()
plt.show()


# 3.2.1 Calculate HPI variations over the years

# Filter data for the year 2023
df_2023 = agg_df[agg_df['Year'] == 2023]

# Calculate HPI variation for each city
initial_hpi_2005 = agg_df.groupby('City')['Composite_HPI_SA'].min()
final_hpi_2023 = df_2023.groupby('City')['Composite_HPI_SA'].max()
hpi_variation = final_hpi_2023 - initial_hpi_2005

# Calculate percentage increase in HPI
hpi_percentage_increase = (hpi_variation / initial_hpi_2005) * 100

# Find the city with the highest HPI variation
city_highest_variation = hpi_variation.idxmax()
highest_variation_value = hpi_variation.max()

# Extract HPI values for each city in 2023
hpi_2023 = df_2023.set_index('City')['Composite_HPI_SA']

# Find the city with the highest HPI in 2023
city_highest_hpi_2023 = hpi_2023.idxmax()
highest_hpi_2023_value = hpi_2023.max()

# Rank cities based on HPI variation, HPI in 2023, and HPI percentage increase
ranked_cities = pd.DataFrame({
    'Initial_HPI_2005': initial_hpi_2005,
    'HPI_Variation': hpi_variation,
    'HPI_Percentage_Increase': hpi_percentage_increase,
    'HPI_2023': hpi_2023
}).sort_values(by=['HPI_Percentage_Increase', 'HPI_2023'], ascending=[False, False])

# Format the percentage values
ranked_cities['HPI_Percentage_Increase'] = ranked_cities['HPI_Percentage_Increase'].map('{:.2f}%'.format)

# Print results
print(f"City with the highest HPI variation: {city_highest_variation} ({highest_variation_value:.2f})")
print(f"City with the highest HPI in 2023: {city_highest_hpi_2023} ({highest_hpi_2023_value:.2f})")
print("\nRanking of cities based on HPI variation, HPI in 2023, and HPI Percentage Increase:")
print(ranked_cities)


# 3.3 Post-COVID Analysis of Home Price Index (HPI) - National and Provinces (2019-2023)

# Set the palette before creating the plot
sns.set_palette("bright")

# Filter data for the last 5 years
selected_years = [2019, 2020, 2021, 2022, 2023]
agg_df_last_5_years_provinces = agg_df_provinces[agg_df_provinces['Year'].isin(selected_years)]

# Plotting the aggregated data
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Composite_HPI_SA', hue='Province', data=agg_df_last_5_years_provinces, marker='o')

plt.xlabel('Year', fontsize=16)
plt.ylabel('Average Home Price Index (HPI)', fontsize=16)
plt.title('Post-COVID Analysis of Home Price Index (HPI) - National and Provinces (2019-2023)', fontsize=16)

# Set ticks for all years
plt.xticks(agg_df_last_5_years_provinces['Year'].unique())

# Add horizontal grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Increase the number of ticks on the y-axis
plt.yticks(np.arange(agg_df_last_5_years_provinces['Composite_HPI_SA'].min(), agg_df_last_5_years_provinces['Composite_HPI_SA'].max(), 10))

# Format y-axis ticks as integers
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

# Move the legend to the right outside the plot
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left')

plt.tight_layout()
plt.show()


# 3.3.1 Calculate HPI variations over the years

# Filter data for the year 2023
df_2023_provinces = agg_df_provinces[agg_df_provinces['Year'] == 2023]

# Calculate HPI variation for each city
initial_hpi_2019_provinces = agg_df_last_5_years_provinces.groupby('Province')['Composite_HPI_SA'].first()
final_hpi_2023_provinces = df_2023_provinces.groupby('Province')['Composite_HPI_SA'].mean()
hpi_variation_provinces = final_hpi_2023_provinces - initial_hpi_2019_provinces

# Calculate percentage increase in HPI
hpi_percentage_increase_provinces = (hpi_variation_provinces / initial_hpi_2019_provinces) * 100

# Find the city with the highest HPI variation
province_highest_variation = hpi_variation_provinces.idxmax()
highest_variation_value_provinces = hpi_variation_provinces.max()

# Extract HPI values for each city in 2023
hpi_2023_provinces = df_2023_provinces.set_index('Province')['Composite_HPI_SA']

# Find the city with the highest HPI in 2023
province_highest_hpi_2023 = hpi_2023_provinces.idxmax()
highest_hpi_2023_value_provinces = hpi_2023_provinces.max()

# Rank cities based on HPI variation, HPI in 2023, and HPI percentage increase
ranked_provinces = pd.DataFrame({
    'Initial_HPI_2019_Provinces': initial_hpi_2019_provinces,
    'HPI_Variation_Provinces': hpi_variation_provinces,
    'HPI_Percentage_Increase_Provinces': hpi_percentage_increase_provinces,
    'HPI_2023_Provinces': hpi_2023_provinces
}).sort_values(by=['HPI_Percentage_Increase_Provinces', 'HPI_2023_Provinces'], ascending=[False, False])

# Format the percentage values
ranked_provinces['HPI_Percentage_Increase_Provinces'] = ranked_provinces['HPI_Percentage_Increase_Provinces'].map('{:.2f}%'.format)
# Sort the ranked_cities DataFrame by HPI in 2023 in descending order
ranked_provinces_sorted = ranked_provinces.sort_values(by='HPI_2023_Provinces', ascending=False)

# Print results
print(f"Province with the highest HPI variation: {province_highest_variation} ({highest_variation_value_provinces:.2f})")
print(f"Province with the highest HPI in 2023: {province_highest_hpi_2023} ({highest_hpi_2023_value_provinces:.2f})")
print("\nRanking of Provinces based on HPI variation, HPI in 2023, and HPI Percentage Increase (Ordered by HPI in 2023):")
print(ranked_provinces_sorted)


# 3.4 Post-COVID Analysis of Home Price Index (HPI) Across Cities (2019-2023

# Set the palette before creating the plot
sns.set_palette("bright")

# Filter data for the last 5 years
selected_years = [2019, 2020, 2021, 2022, 2023]
agg_df_last_5_years = agg_df[agg_df['Year'].isin(selected_years)]

# Plotting the aggregated data
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Composite_HPI_SA', hue='City', data=agg_df_last_5_years, marker='o')

plt.xlabel('Year', fontsize=16)
plt.ylabel('Average Home Price Index (HPI)', fontsize=16)
plt.title('Post-COVID Analysis of Home Price Index (HPI) Across Cities (2019-2023)', fontsize=16)

# Set ticks for all years
plt.xticks(agg_df_last_5_years['Year'].unique())

# Add horizontal grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Increase the number of ticks on the y-axis
plt.yticks(np.arange(agg_df_last_5_years['Composite_HPI_SA'].min(), agg_df_last_5_years['Composite_HPI_SA'].max(), 10))

# Format y-axis ticks as integers
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

# Move the legend to the right outside the plot
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left')

plt.tight_layout()
plt.show()



# 3.4.1 Calculate HPI variations over the years

# Filter data for the year 2023
df_2023 = agg_df[agg_df['Year'] == 2023]

# Calculate HPI variation for each city
initial_hpi_2019 = agg_df_last_5_years.groupby('City')['Composite_HPI_SA'].first()
final_hpi_2023 = df_2023.groupby('City')['Composite_HPI_SA'].mean()
hpi_variation = final_hpi_2023 - initial_hpi_2019

# Calculate percentage increase in HPI
hpi_percentage_increase = (hpi_variation / initial_hpi_2019) * 100

# Find the city with the highest HPI variation
city_highest_variation = hpi_variation.idxmax()
highest_variation_value = hpi_variation.max()

# Extract HPI values for each city in 2023
hpi_2023 = df_2023.set_index('City')['Composite_HPI_SA']

# Find the city with the highest HPI in 2023
city_highest_hpi_2023 = hpi_2023.idxmax()
highest_hpi_2023_value = hpi_2023.max()

# Rank cities based on HPI variation, HPI in 2023, and HPI percentage increase
ranked_cities = pd.DataFrame({
    'Initial_HPI_2019': initial_hpi_2019,
    'HPI_Variation': hpi_variation,
    'HPI_Percentage_Increase': hpi_percentage_increase,
    'HPI_2023': hpi_2023
}).sort_values(by=['HPI_Percentage_Increase', 'HPI_2023'], ascending=[False, False])

# Format the percentage values
ranked_cities['HPI_Percentage_Increase'] = ranked_cities['HPI_Percentage_Increase'].map('{:.2f}%'.format)
# Sort the ranked_cities DataFrame by HPI in 2023 in descending order
ranked_cities_sorted = ranked_cities.sort_values(by='HPI_2023', ascending=False)

# Print results
print(f"City with the highest HPI variation: {city_highest_variation} ({highest_variation_value:.2f})")
print(f"City with the highest HPI in 2023: {city_highest_hpi_2023} ({highest_hpi_2023_value:.2f})")
print("\nRanking of cities based on HPI variation, HPI in 2023, and HPI Percentage Increase (Ordered by HPI in 2023):")
print(ranked_cities_sorted)
