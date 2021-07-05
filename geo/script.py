
import pandas as pd

# The URL we will read our data from
#url = 'https://en.wikipedia.org/wiki/List_of_countries_by_meat_consumption'
#url = 'http://calculadistancias.herokuapp.com/'
#url= 'https://webpokerroom.herokuapp.com/poker/listadotorneos/'
url='https://x-y.es/covid19/la-rioja.ccaa'
# read_html returns a listof tables from the URL
#pd.options.display.max_rows = 4
#pd.set_option('display.max_rows', 100)
pd.set_option("display.max_rows", None)
tables = pd.read_html(url)

# The data is in the first table - this changes from time to time - wikipedia is updated all the time.
table = tables[0]
print(table.head(None))



'''

import pandas as pd
import folium
import geopandas


# The URL we will read our data from
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_meat_consumption'
# read_html returns a list of tables from the URL
tables = pd.read_html(url)

# The data is in the first table - this changes from time to time - wikipedia is updated all the time.
table = tables[0]

# Read the geopandas dataset
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

# Merge the two DataFrames together
table = world.merge(table, how="left", left_on=['name'], right_on=['Country'])

# Clean data: remove rows with no data
table = table.dropna(subset=['kg/person (2002)[9][note 1]'])

# Create a map
my_map = folium.Map()

# Add the data
folium.Choropleth(
    geo_data=table,
    name='choropleth',
    data=table,
    columns=['Country', 'kg/person (2002)[9][note 1]'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Meat consumption in kg/person'
).add_to(my_map)
my_map.save('meat.html')

'''