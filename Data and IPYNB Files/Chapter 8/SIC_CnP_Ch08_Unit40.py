import streamlit as st
import pandas as pd

# 1. Text Elements
st.markdown('# Text Elelemts')

st.text('1.2. Displaying Basic Text')
st.title('This is the title')
st.header('This is the header')
st.subheader('This is the subheader')
st.text('This is the text')
st.caption('This is the caption')
st.divider()
st.write('This is the write')
df = pd.DataFrame({'col1':[1, 2, 3, 4], 'col2':[10, 20, 30, 40]})
st.write('Display a DataFrame using st.write', df)

st.text('1.4. Displaying Markdown')
st.markdown('# This is a Markdown title')    
st.markdown('## This is a Markdown header')
st.markdown('### This is a Markdown subheader')
st.markdown('this is the markdown')
st.markdown('this is **the markdown**')
st.markdown('this is _the markdown_')
st.markdown('this is *the markdown*')
st.markdown('this is **_the markdown_**')

st.text('1.6. Displaying Formatting and Display Tools')
st.code('x=134')
st.latex(r'''a + ar + a r^2 ''')


# 2. Media Elements
st.markdown('# Media Elelemts')
st.text('2.1. Displaying Media Elements')
# image 
st.image('https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80', caption='Sunrise by the mountains')
# audio
st.audio('C:/Users/user/streamlit/data/media/MusicSample.mp3')
# video 
st.video('C:/Users/user/streamlit/data/media/VideoSample.mp4')


# 3. Data Elelemts
st.markdown('# Data Elelemts')

st.text('3.1. Displaying Metric')
st.metric(label='Temperature', value='30.5 °C', delta='2.5 °C')
st.metric(label='Temperature', value='28 °C', delta='-2.5 °C')
# metric with columns
col1, col2, col3 = st.columns(3) 
col1.metric('Temperature', '30.5 °C', '2.5 °C')
col2.metric('Wind Speed', '9 mph', '-8%')
col3.metric('Humidity', '86%', '4%')

st.text('3.3. Displaying Data')
st.text('dataframe')
customers = pd.read_csv('C:/Users/user/streamlit/data/Mobile/Mobile_Customers.csv')
st.dataframe(customers) 
st.text('table')
st.table(customers.head(10))
st.text('data_editor')
st.data_editor(customers)


# 4. Input Widgets
st.markdown('# Input widget')

st.text('4.1. Displaying Input Widgets')
st.caption('Button')
if st.button('Say hello button'):
    st.write('Hello')
else:
    st.write('Goodbye')
    
st.caption('checkbox')
agree = st.checkbox('I agree')
if agree:
    st.write('😄'*10) # Emoji panel : windows key + .(period)

st.caption('toggle')
on = st.toggle('Activate feature')
if on:
    st.write('Feature activated!')

st.caption('selectbox')
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Mobile phone', 'Office phone'))
st.write('Okay, we will contact you via', option)

st.caption('multiselect')
options = st.multiselect(
    'Select all your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'] )
st.write('Selected colors:', ', '.join(options))

st.text('4.3. Displaying text/number/date/chat Input')

st.caption('text_input')
title = st.text_input('Enter your favorite movie', 'Sound of Music') 
# 'Sound of Music': default value
st.write('Your favorite movie is:', title)

st.caption('number_input')
number = st.number_input(
    'Insert a number (1–10)',
    min_value=1, max_value=10, value=5, step=1)
st.write('The current number is', number)

st.caption('date_input')
from datetime import datetime
ymd = st.date_input('When is your birthday', datetime(2000, 9, 6)) 
st.write('Your birthday is:', ymd)

st.caption('chat_input')
prompt = st.chat_input("Say something")
if prompt:
   st.write(f"User has sent the following prompt: {prompt}")

st.text('4.5. Displaying slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write('I am ', age, ' years old')

values = st.slider('Select a range of values', 
                    0.0, 100.0, (25.0, 75.0))
st.write('Values: ', values)

slider_date = st.slider('Select a range of date',
    min_value=datetime(2025, 1, 1),  max_value=datetime(2025, 12, 31),
    value=(datetime(2025, 6, 1), datetime(2025, 7, 31)),
    format='YY/MM/DD')
st.write('slider date: ', slider_date)
st.write('slider_date[0]: ', slider_date[0], 
         'slider_date[1]: ', slider_date[1] )


# 5. Layouts & Containers
st.markdown('# Layouts & Containers')

with st.sidebar:
    st.header('5.2. Sidebar')
add_selectbox = st.sidebar.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Mobile phone', 'Office phone'))
if add_selectbox == 'Email':
    st.sidebar.title('📧')
elif add_selectbox == 'Mobile phone':
    st.sidebar.title('📱')
else:
    st.sidebar.title('☎︎')

st.text('5.4. Displaying columns')
col1, col2, col3 = st.columns(3)
with col1:
    st.text('A cat')
    st.image('https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg')
with col2:
    st.text('A dog')
    st.image('https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg')
with col3:
    st.text('An owl')
    st.image('https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg')

st.text('5.6. Displaying tabs')
tab1, tab2, tab3 = st.tabs(['A cat', 'A dog', 'An owl'])
with tab1:
    st.caption('Cat')
    st.image('https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg', width=200)
with tab2:
    st.caption('Dog')
    st.image('https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg', width=200)
with tab3:
    st.caption('Owl')
    st.image('https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg', width=200)

st.text('5.8. Displaying multipage app')
def main_page():
      st.title('Main page 🎈')
      st.sidebar.title('Side Main 🎈')
def page2():
      st.title('Page 2 ❄️')
      st.sidebar.title('Side 2 ❄️')
def page3():
      st.title('Page 3 🎉')
      st.sidebar.title('Side 3 🎉')
page_names_to_funcs = {'Main Page': main_page, 'Page 2': page2, 'Page 3': page3}
selected_page = st.sidebar.selectbox('Select a page', page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

st.header('Pair programming')
st.subheader('Query Data by Date Range')

# Import Streamlit for building the web app
# Import Pandas for data handling and analysis
# Import datetime for creating and managing date values
import streamlit as st
import pandas as pd
from datetime import datetime

# Read the CSV file: 'Monthly_value.csv'
# This loads the dataset into a dataframe named df
df = pd.read_csv('C:/Users/user/streamlit/data/Monthly Value/Monthly_value.csv')

# Display the current data type of the 'Period' column using .dtypes
st.write('Date field data type:', df['Period'].dtypes)

# Show the raw dataframe before any processing
st.write(df)

# Convert the 'Period' column from string to a proper datetime type
df['Period'] = pd.to_datetime(df['Period'], format='%m/%d/%Y')

# Display the data type again to confirm it was successfully converted to datetime
st.write('Date field data type:', df['Period'].dtypes)

# Show the dataframe again after conversion
st.write(df) 

# Create a date range slider for filtering the dataframe
# Users can select a start and end date within the specified range
slider_date = st.slider(
    'Select a date range',
    datetime(2023, 1, 1),           # Minimum selectable date
    datetime(2025, 12, 31),         # Maximum selectable date
    value=(datetime(2025, 5, 1),    # Default start date
           datetime(2025, 7, 31)), # Default end date
    format='YY/MM/DD')              # Display format of the slider dates

# Display the selected start and end dates for confirmation
st.write('slider_date[0]: ', slider_date[0], 
         'slider_date[1]: ', slider_date[1])

# Store the selected dates into separate variables start_date, end_dat
start_date = slider_date[0]
end_date = slider_date[1]

# Filter the dataframe based on the selected date range
sel_df = df.loc[df['Period'].between(start_date, end_date)]

# Display the filtered results
st.dataframe(sel_df)