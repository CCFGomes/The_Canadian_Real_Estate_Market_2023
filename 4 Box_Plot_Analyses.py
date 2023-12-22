# 4 Box-Plot Analyses

# 4.1 Variability of Housing Prices - National vs Provinces (2019-2023)
import matplotlib.ticker as ticker

# Set the palette
sns.set_palette("muted")

selected_years = [2019, 2020, 2021, 2022, 2023]
agg_df1_provinces = agg_df_provinces[agg_df_provinces['Year'].isin(selected_years)]
                                     
# Define money ticks
money_ticks = [200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 950000, 1000000, 1050000, 1100000, 1150000, 1200000] 

plt.figure(figsize=(12, 8))
sns.boxplot(x='Province', y='Composite_Benchmark_SA', data=agg_df1_provinces)
plt.xlabel('Province', fontsize = 16)
plt.ylabel('Average of Housing Price (CAD)', fontsize = 16)
plt.title('Variability of Housing Prices - National vs Provinces (2019-2023)', fontsize = 16)

# Set money ticks and labels
formatted_labels = [f'C${tick/1000:.0f}K' if tick < 1000000 else f'C${tick/1e6:.1f}M' for tick in money_ticks]
plt.yticks(money_ticks, formatted_labels)

plt.show()


# 4.1.1 Extract data from the box plot
selected_years = [2019, 2020, 2021, 2022, 2023]
agg_df1_provinces = agg_df_provinces[agg_df_provinces['Year'].isin(selected_years)]

# Group data by 'City' and collect housing prices for each city
box_plot_data_provinces = {province: agg_df1_provinces[agg_df1_provinces['Province'] == province]['Composite_Benchmark_SA'].values for province in agg_df1_provinces['Province'].unique()}

# Print the extracted data

for province, prices in box_plot_data_provinces.items():
    formatted_prices = ', '.join([f'C${price/1000:.0f}K' if price < 1000000 else f'C${price/1e6:.1f}M' for price in prices])
    print(f"{province}: [{formatted_prices}]")



# 4.2 Variability of Housing Prices Across Cities during the last 5 years (2019-2023)
# Set the palette
sns.set_palette("muted")

selected_years = [2019, 2020, 2021, 2022, 2023]
agg_df1 = agg_df[agg_df['Year'].isin(selected_years)]
                                     
# Define money ticks
money_ticks = [200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 950000, 1000000, 1050000, 1100000, 1150000, 1200000] 

plt.figure(figsize=(12, 8))
sns.boxplot(x='City', y='Composite_Benchmark_SA', data=agg_df1)
plt.xlabel('City', fontsize = 16)
plt.ylabel('Average of Housing Price (CAD)', fontsize = 16)
plt.title('Variability of Housing Prices Across Cities during the last 5 years (2019-2023)', fontsize = 16)

# Set money ticks and labels
formatted_labels = [f'C${tick/1000:.0f}K' if tick < 1000000 else f'C${tick/1e6:.1f}M' for tick in money_ticks]
plt.yticks(money_ticks, formatted_labels)

plt.show()



# 4.2.1 Extract data from the box plot
selected_years = [2019, 2020, 2021, 2022, 2023]
agg_df1 = agg_df[agg_df['Year'].isin(selected_years)]

# Group data by 'City' and collect housing prices for each city
box_plot_data = {city: agg_df1[agg_df1['City'] == city]['Composite_Benchmark_SA'].values for city in agg_df1['City'].unique()}

# Print the extracted data

for city, prices in box_plot_data.items():
    formatted_prices = ', '.join([f'C${price/1000:.0f}K' if price < 1000000 else f'C${price/1e6:.1f}M' for price in prices])
    print(f"{city}: [{formatted_prices}]")

