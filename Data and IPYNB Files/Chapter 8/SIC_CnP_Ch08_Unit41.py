import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px

st.header('1. Chart Elements- Simple Simple Charts')
chart_data = {
    'sales1': [45, 53, 65, 66, 97],
    'sales2': [256, 274, 319, 327, 375],
    'sales3': [143, 157, 145, 145, 155]
}
st.dataframe(chart_data)

st.text('Simple Line chart')
st.line_chart(chart_data, use_container_width=True) 

st.text('Simple Bar chart')
st.bar_chart(chart_data)

st.text('Simple area chart')
st.area_chart(chart_data)


st.header('2. Chart Elements- Altair Charts')

st.text('Preprocessing datasets For altair chart visualization')
sales_data = {
    'date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04',
             '2025-01-05', '2025-01-06', '2025-01-07'],
    'Sales1': [45, 53, 65, 66, 97, 83, 46],
    'Sales2': [256, 274, 319, 327, 375, 373, 202],
    'Sales3': [143, 157, 145, 155, 155, 156, 135]
}
df = pd.DataFrame(sales_data)
st.dataframe(df)

df_melted = pd.melt(df, id_vars=['date'], var_name='teams', value_name='sales')
st.dataframe(df_melted)

st.text('Altair Line chart')
chart = alt.Chart(df_melted, title='Daily Sales Comparison by Team').mark_line().encode(
         x='date', y='sales', color='teams', strokeDash='teams').properties(width=650, height=350)
st.altair_chart(chart)

st.text('Altair Bar chart + Text Labels')
chart = alt.Chart(df_melted, title='Daily Cumulative Sales').mark_bar().encode(
    x='date', y='sales', color='teams')
text = alt.Chart(df_melted).mark_text(dx=0, dy=0, color='black').encode(
    x='date', y='sales', detail='teams', text=alt.Text('sales:Q') )
st.altair_chart(chart+text, use_container_width=True)

st.text('Altair Scatter chart')
iris = pd.read_csv('C:/Users/user/streamlit/data/Iris/Iris.csv')
st.dataframe(iris)
chart = alt.Chart(iris).mark_circle().encode(
    x = 'petal_length', y='petal_width', color = 'species' )  
st.altair_chart(chart, use_container_width=True)


st.header('3. Chart Elements- Plotly Charts')

st.text('Plotly Pie/Donut chart') 
medal = pd.read_csv('C:/Users/user/streamlit/data/medal/Medal.csv')
st.dataframe(medal)

fig = px.pie(medal, values = "gold", names = "nation", 
             title="Olympic Archery Gold Medal Distribution", hole=.3 )
fig.update_traces(textposition='inside', textinfo = 'percent+value+label')
fig.update_layout(font = dict(size = 16))
st.plotly_chart(fig)

st.text('Plotly Bar chart')
fig = px.bar(medal, x="nation", y=["gold", "silver", "bronze"],
             text_auto=True, title="Olympic Archery Medal Counts by Nation")
st.plotly_chart(fig)


st.header('4. Chart Elements- st.map')

map_data = pd.DataFrame({
    'lat':[-34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
    'lon':[-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
    'name':['Buenos Aires', 'Paris', 'melbourne', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador'],
    'value':[10, 12, 40, 70, 23, 43, 100, 43]
})
st.write(map_data)
st.map(map_data,
    latitude='lat',
    longitude='lon')


st.header('5. Chart Elements- folium.map')

import folium

my_map = folium.Map( location=[map_data['lat'].mean(), map_data['lon'].mean()], zoom_start=2 )
for index, row in map_data.iterrows():        
    folium.CircleMarker(                    
        location=[row['lat'], row['lon']],  
        radius=row['value'] / 5,             
        color='pink',                     
        fill=True,                       
        fill_opacity=1.0                  
    ).add_to(my_map)                    

    folium.Marker(                          
        location=[row['lat'], row['lon']],   
        icon=folium.DivIcon(html=f"<div>{row['name']} {row['value']}</div>"), 
    ).add_to(my_map)                    

st.components.v1.html(my_map._repr_html_(), width=800, height=600)


st.header('Pair programming')

st.subheader('Q1. Survival Analysis of Titanic Passengers Using Plotly Charts')

# Import the libraries required to run the code.
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the file Titanic.csv into a dataframe named titanic
titanic = pd.read_csv('C:/Users/user/streamlit/data/titanic/Titanic.csv')

# Add a checkbox to display the titanic dataset.
if st.checkbox('View Titanic Dataset'):
    st.dataframe(titanic)

# Create a selectbox for choosing the survival analysis option
tit = st.selectbox(
     'Select an option for survival analysis.',
     ('Analysis by Embarkation', 'Analysis by Passenger Class') )

# Set 'sel' based on the selected analysis option
if tit == 'Analysis by Embarkation':
    sel = 'Embarked'
else:
    sel = 'Pclass'

# Use st.columns(2) to create two side-by-side chart areas named col1 and col2.
col1, col2 = st.columns(2)

with col1:  # pie chart: name=sel, values='Survived'
    fig = px.pie(titanic, names=sel, values='Survived') 
    fig.update_traces(textposition='inside', textinfo = 'percent+label+value')
    fig.update_layout(height=400, width=400, font = dict(size = 16))
    fig.update(layout_showlegend=False)
    st.plotly_chart(fig)
with col2:  # bar chart: x=sel, y="Survived", color="Sex"
    fig = px.bar(titanic, x=sel, y="Survived", color="Sex")
    fig.update_layout(height=400, width=400)
    st.plotly_chart(fig)


st.subheader('Q2. TV Sales Impact Analysis Using an Altair Scatter Chart')

# Import the libraries required to run the code.
import streamlit as st
import pandas as pd
import altair as alt

#Load the file TV_Sales.csv into a dataframe named sales.
sales = pd.read_csv('C:/Users/user/streamlit/data/TVsales/TV_Sales.csv')

# Add a checkbox to display the TV sales dataset.
if st.checkbox('View the TV sales datat'):
    st.dataframe(sales)

# Create a radio button to select a variable for sales comparison.
sel = st.radio(
     'Select an item for the sales comparison analysis.',
     ('Income', 'Price', 'CompPrice'))

# Build an Altair scatter chart
fig = alt.Chart(sales).mark_circle().encode( x='Sales', y=sel, size=sel).properties(width=650, height=450)
# Display the scatter chart
st.altair_chart(fig, use_container_width=True)


st.subheader('Q3. Covid-19 Case Status Using a Folium Map')

# Import the libraries required to run the code.
import streamlit as st
import folium
import pandas as pd

# Load the file Covid.csv into a dataframe named map_data.
map_data = pd.read_csv('C:/Users/user/streamlit/data/covid/Covid.csv')
# Display the map_data dataset.
st.dataframe(map_data)

# Create a Folium map centered at the dataset’s average coordinates with zoom_start=2.
my_map = folium.Map( location=[map_data['lat'].mean(), map_data['lon'].mean()], zoom_start=2 )

# Add a CircleMarker for each row using lat/lon, scaling radius by value/10000 
# and styling with pink fill opacity.
# Add a text label marker showing the region name and case value using DivIcon.
for index, row in map_data.iterrows():       
    folium.CircleMarker(                     
        location=[row['lat'], row['lon']],   
        radius=row['value']/10000,           
        color='pink',                        
        fill=True,                           
        fill_opacity=0.8                     
    ).add_to(my_map)                         

    folium.Marker(                           
        location=[row['lat'], row['lon']],   
        icon=folium.DivIcon(html=f'<div>{row['name']} {row['value']}</div>'), 
    ).add_to(my_map)    

# Render the interactive Folium map in Streamlit at 1000×800 size.
st.components.v1.html(my_map._repr_html_(), width=1000, height=800)