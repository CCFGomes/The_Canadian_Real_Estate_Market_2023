# 5 Comparative Data Analyses

# 5.1 Single Family Price Comparison: National vs Provinces (2019-2023)

# Convert 'Date' column to datetime with a specific format
agg_df_provinces['Date'] = pd.to_datetime(agg_df_provinces['Date'], format='%b %Y', errors='coerce')

# Drop rows with missing 'Date' values
agg_df_provinces = agg_df_provinces.dropna(subset=['Date'])

# Extract year from the 'Date' column
agg_df_provinces['Year'] = agg_df_provinces['Date'].dt.year.astype(int)

# Filter data for the desired years
selected_years = [2019, 2020, 2021, 2022, 2023]
agg_df3 = agg_df_provinces[agg_df_provinces['Year'].isin(selected_years)]

# Set the palette 
sns.set_palette("muted")

# Create a grouped bar chart
plt.figure(figsize=(16, 8))
sns.set_theme(style="whitegrid")
bar_plot = sns.barplot(x='Year', y='Single_Family_Benchmark_SA', hue='Province', data=agg_df3, errorbar=None)
plt.xlabel('Year', fontsize = 20)
plt.ylabel('Average Single Family Housing Prices (CAD)', fontsize = 20)
plt.title('Single Family Price Comparison: National vs Provinces (2019-2023)', fontsize = 20)

# Annotate values above each bar
for p in bar_plot.patches:
    value = p.get_height()
    if value >= 1e6:
        value_str = f'${value/1e6:.1f}M'
    else:
        value_str = f'${value/1e3:.0f}K'
    bar_plot.annotate(value_str, (p.get_x() + p.get_width() / 2., p.get_height()),
                      ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Set custom y-axis ticks
money_ticks = [0, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000, 1600000, 1700000, 1800000, 1900000, 2000000] 
bar_plot.set_yticks(money_ticks)

# Format y-axis tick labels based on the value
money_labels = [f'${val/1e6:.1f}M' if val >= 1e6 else f'${val/1e3:.0f}K' for val in money_ticks]
bar_plot.set_yticklabels(money_labels)

plt.show()



# 5.2 Single Family Price Comparison Across Cities (2019-2023)

# Set the palette before creating the plot
sns.set_palette("pastel")

# Convert 'Date' column to datetime with a specific format
agg_df['Date'] = pd.to_datetime(agg_df['Date'], format='%b %Y', errors='coerce')

# Drop rows with missing 'Date' values
agg_df = agg_df.dropna(subset=['Date'])

# Extract year from the 'Date' column
agg_df['Year'] = agg_df['Date'].dt.year.astype(int)

# Filter data for the desired years
selected_years = [2019, 2020, 2021, 2022, 2023]
agg_df2 = agg_df[agg_df['Year'].isin(selected_years)]

# Create a grouped bar chart
plt.figure(figsize=(16, 8))
sns.set_theme(style="whitegrid")
bar_plot = sns.barplot(x='Year', y='Single_Family_Benchmark_SA', hue='City', data=agg_df2, errorbar=None)
plt.xlabel('Year', fontsize = 20)
plt.ylabel('Average Single Family Prices (CAD)', fontsize = 20)
plt.title('Single Family Price Comparison Across Cities (2019-2023)', fontsize = 20)

# Annotate values above each bar
for p in bar_plot.patches:
    value = p.get_height()
    if value >= 1e6:
        value_str = f'${value/1e6:.1f}M'
    else:
        value_str = f'${value/1e3:.0f}K'
    bar_plot.annotate(value_str, (p.get_x() + p.get_width() / 2., p.get_height()),
                      ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Set custom y-axis ticks
money_ticks = [0, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000, 1600000, 1700000, 1800000, 1900000, 2000000] 
bar_plot.set_yticks(money_ticks)

# Format y-axis tick labels based on the value
money_labels = [f'${val/1e6:.1f}M' if val >= 1e6 else f'${val/1e3:.0f}K' for val in money_ticks]
bar_plot.set_yticklabels(money_labels)

plt.show()



# 5.3 Year over Year (YoY) Housing Price Comparison (2022 vs. 2023)

# 5.3.1 Housing Price Comparison: National vs. Provinces (2022 vs. 2023

from tabulate import tabulate

# Filter data for 2022 and 2023
selected_years = [2022, 2023]
filtered_df_provinces = agg_df_provinces[agg_df_provinces['Year'].isin(selected_years)].copy()
rename_mapping = {
    'Single_Family_Benchmark_SA': 'Single_Family',
    'One_Storey_Benchmark_SA': 'One_Storey',
    'Two_Storey_Benchmark_SA': 'Two_Storey',
    'Townhouse_Benchmark_SA': 'Townhouse',
    'Apartment_Benchmark_SA': 'Apartment'
}
filtered_df_provinces.rename(columns=rename_mapping, inplace=True)
# Reshape the DataFrame to long format
melted_df = pd.melt(filtered_df_provinces, id_vars=['Province', 'Year'], value_vars=['Single_Family', 'One_Storey', 'Two_Storey', 'Townhouse', 'Apartment'], var_name='Housing_Type', value_name='Price')

# Set the palette before creating the plot
sns.set_palette("muted")

# Create a grouped bar chart using catplot
g = sns.catplot(x='Housing_Type', y='Price', hue='Province', col='Year', data=melted_df, kind='bar', height=8, aspect=1.2, legend=True)

# Set labels and title
g.set_axis_labels('Province', 'Average Housing Price ($)', fontsize=20)
g.set_titles('Housing Prices: {col_name}', fontsize=20)
g.fig.suptitle('Housing Price Comparison: National vs. Provinces (2022 vs. 2023)', fontsize=24, y=1.02)
for ax in g.axes.flat:
    ax.set_title(ax.get_title(), {'fontsize': 20})

# Annotate values above each bar
for ax in g.axes.flat:
    for p in ax.patches:
        value = p.get_height()
        if value >= 1e6:
            value_str = f'${value/1e6:.1f}M'
        else:
            value_str = f'${value/1e3:.0f}K'
        ax.annotate(value_str, (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=16)

# Format y-axis tick labels
money_ticks = [0, 500000, 1000000, 1500000, 2000000]
g.set(yticks=money_ticks)

# Format y-axis tick labels based on the value
money_labels = [f'C${val/1e6:.1f}M' if val >= 1e6 else f'C${val/1e3:.0f}K' for val in money_ticks]
g.set_yticklabels(labels=money_labels, fontsize=16)

g.set_xticklabels(fontsize=18)

# Move the legend to the top right corner
sns.move_legend(g, loc='upper right', fontsize=16, title_fontsize=18, bbox_to_anchor=(1, 0.9))
# Adjust the layout
plt.tight_layout()
plt.show()


# 5.3.1.1 Extract data from the graphic for easier discussion
results_provinces = []
for year in selected_years:
    for housing_type in melted_df['Housing_Type'].unique():
        
        # Filter data for the specific year and housing type
        subset_data_provinces = melted_df[(melted_df['Year'] == year) & (melted_df['Housing_Type'] == housing_type)]
        
        # Append the relevant information to the results list
        results_provinces.append({
            'Year': year,
            'Housing Type': housing_type,
            'Data': subset_data_provinces[['Province', 'Price']]
        })

# Display the results using tabulate
for result in results_provinces:
    print(f"\nYear: {result['Year']}\nHousing Type: {result['Housing Type']}")
    print(tabulate(result['Data'], headers='keys', tablefmt='grid'))


# 5.3.2 Housing Price Comparison among Most Popular Cities (2022 vs. 2023)

# Filter data for 2022 and 2023
selected_years = [2022, 2023]
filtered_df = agg_df[agg_df['Year'].isin(selected_years)].copy()
filtered_df.rename(columns=rename_mapping, inplace=True)

# Reshape the DataFrame to long format
melted_df2 = pd.melt(filtered_df, id_vars=['City', 'Year'], value_vars=['Single_Family', 'One_Storey', 'Two_Storey', 'Townhouse', 'Apartment'], var_name='Housing_Type', value_name='Price')

# Set the palette before creating the plot
sns.set_palette("muted")

# Create a grouped bar chart using catplot
g = sns.catplot(x='Housing_Type', y='Price', hue='City', col='Year', data=melted_df2, kind='bar', height=8, aspect=1.5, legend=True)

# Set labels and title
g.set_axis_labels('Housing Type', 'Average Housing Price (CAD)', fontsize=20)
g.set_titles('Housing Prices: {col_name}', fontsize=20)
g.fig.suptitle('Housing Price Comparison among Most Popular Cities (2022 vs. 2023)', fontsize=24, y=1.02)
for ax in g.axes.flat:
    ax.set_title(ax.get_title(), {'fontsize': 20})

# Annotate values above each bar
for ax in g.axes.flat:
    for p in ax.patches:
        value = p.get_height()
        if value >= 1e6:
            value_str = f'${value/1e6:.1f}M'
        else:
            value_str = f'${value/1e3:.0f}K'
        ax.annotate(value_str, (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=16)

# Format y-axis tick labels
money_ticks = [0, 500000, 1000000, 1500000, 2000000]
g.set(yticks=money_ticks)

# Format y-axis tick labels based on the value
money_labels = [f'C${val/1e6:.1f}M' if val >= 1e6 else f'C${val/1e3:.0f}K' for val in money_ticks]
g.set_yticklabels(labels=money_labels, fontsize=16)

g.set_xticklabels(fontsize=18)

# Move the legend to the top right corner
sns.move_legend(g, loc='upper right', fontsize=18, title_fontsize=20, bbox_to_anchor=(1, 0.9))
# Adjust the layout
plt.tight_layout()
plt.show()



# 5.3.2.1 Extract data from the graphic for easier discussion
results = []

for year in selected_years:
    for housing_type in melted_df2['Housing_Type'].unique():
        # Filter data for the specific year and housing type
        subset_data = melted_df2[(melted_df2['Year'] == year) & (melted_df2['Housing_Type'] == housing_type)]
        
        # Append the relevant information to the results list
        results.append({
            'Year': year,
            'Housing Type': housing_type,
            'Data': subset_data[['City', 'Price']]
        })

# Display the results using tabulate
for result in results:
    print(f"\nYear: {result['Year']}\nHousing Type: {result['Housing Type']}")
    print(tabulate(result['Data'], headers='keys', tablefmt='grid'))
