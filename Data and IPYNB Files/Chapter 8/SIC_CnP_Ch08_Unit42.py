import streamlit as st
import pandas as pd
import altair as alt

# --- Function to load data (using the uploaded file name) ---
@st.cache_data
def load_data(filepath):
    """Loads the CSV data into a pandas DataFrame."""
    try:
        df = pd.read_csv(filepath)
        # Ensure medal columns are numeric and handle missing values by filling with 0
        medal_cols = ['gold', 'silver', 'bronze']
        for col in medal_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
            else:
                # Add the column if it's missing (though unlikely given the snippet)
                df[col] = 0
        
        # Calculate the 'total' medals column
        df['total'] = df[medal_cols].sum(axis=1)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}. Please ensure 'Medal.csv' is correctly formatted.")
        return pd.DataFrame()

# --- Load the Data ---
# Note: In a live Streamlit environment, you might use st.file_uploader, 
# but here we reference the explicitly named file provided in the prompt.
DATA_FILEPATH = 'C:/Users/user/streamlit/data/medal/Medal.csv'
df_medals = load_data(DATA_FILEPATH)

# Check if data loaded successfully
if df_medals.empty:
    st.stop()

# --- Streamlit App Configuration ---
st.set_page_config(
    page_title="Dynamic Medal Count Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🥇 Dynamic Medal Count Dashboard")
st.markdown("Dashboard analyzing medal counts by nation, filtered by medal type.")

# --- 1. Sidebar for Medal Type Selection ---
st.sidebar.header("Filter Options")

# List of available medal types for selection
medal_types = {
    "Gold Medals": "gold",
    "Silver Medals": "silver",
    "Bronze Medals": "bronze",
    "Total Medals": "total"
}

# Radio button selector in the sidebar
selected_label = st.sidebar.radio(
    "Select Medal Type to Display:",
    list(medal_types.keys()),
    index=3 # Default to 'Total Medals'
)

# Get the corresponding column name
selected_column = medal_types[selected_label]
display_label = selected_label.split()[0] # e.g., 'Gold', 'Total'

# --- 2. KPI Metrics (Key Performance Indicators) ---
st.header("Key Performance Indicators (KPIs)")

# Calculate overall totals
total_gold = df_medals['gold'].sum()
total_silver = df_medals['silver'].sum()
total_bronze = df_medals['bronze'].sum()
total_overall = df_medals['total'].sum()

# Display KPIs using st.columns and st.metric
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Gold", value=f"{total_gold:,}")
with col2:
    st.metric(label="Total Silver", value=f"{total_silver:,}")
with col3:
    st.metric(label="Total Bronze", value=f"{total_bronze:,}")
with col4:
    st.metric(label="Overall Medals", value=f"{total_overall:,}")

st.markdown("---")

# --- 3. Dynamic Bar Chart ---
st.header(f"Medal Count by Nation: {selected_label}")

# Determine color based on selection for better visual distinction
color_scheme = {
    "gold": "gold",
    "silver": "silver",
    "bronze": "sienna",
    "total": "steelblue"
}
chart_color = color_scheme.get(selected_column, "steelblue")

# Sort the data by the selected column in descending order
df_sorted = df_medals.sort_values(by=selected_column, ascending=False)

# Create the Altair chart
chart = alt.Chart(df_sorted).mark_bar().encode(
    # X-axis: Nation (nominal data)
    x=alt.X('nation', sort='-y', title="Nation"),
    # Y-axis: The dynamically selected medal count
    y=alt.Y(selected_column, title=f"Number of {selected_label}"),
    # Color the bars based on the medal type
    color=alt.value(chart_color),
    # Add tooltips for better interaction
    tooltip=['nation', alt.Tooltip(selected_column, title=f"{display_label} Count")]
).properties(
    title=f"Top Nations by {selected_label}"
).interactive() # Allows zooming and panning

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)

# --- 4. Optional: Display Raw Data ---
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Medal Data')
    st.dataframe(df_medals)

########################################################################################################

st.header('Pair programming')
st.subheader('Q1. Vibe Coding Practice with TV_Sales.csv')
st.markdown('#### Dashboard Goal: Analyze how different economic factors influence TV sales. ####')

import streamlit as st
import pandas as pd
import altair as alt

# --- App Configuration ---
st.set_page_config(
    page_title="TV Sales Data Analysis",
    layout="wide"
)

# --- Load Data ---
@st.cache_data
def load_data():
    """Loads the TV Sales data from CSV."""
    # Assumes TV_Sales.csv is in the same directory as the Streamlit app file
    df = pd.read_csv("C:/Users/user/streamlit/data/TVsales/TV_Sales.csv")
    return df

df = load_data()

# --- Title and Header ---
st.title("📺 TV Sales Data Explorer")

st.markdown("""
This application allows you to explore the relationship between **Sales** and other numerical variables in the `TV_Sales.csv` dataset.
""")

# -------------------------------------
## 1. Display the Dataset
st.header("1. TV Sales Dataset")
st.dataframe(df)

# -------------------------------------
## 2. Dynamic Scatter Chart
st.header("2. Sales vs. Comparison Variable Scatter Chart")

# Define numerical columns suitable for the scatter chart (excluding 'Sales')
# Categorical variables like ShelveLoc, City, Local are excluded for a cleaner scatter chart
numerical_cols = ['CompPrice', 'Income', 'Price']

# 2a. Add a selectbox to choose the comparison variable
selected_variable = st.selectbox(
    "Select a variable for comparison with Sales:",
    options=numerical_cols,
    index=1 # 'Income' as the default selection
)

# 2b. Create the scatter chart using Altair
# We use Altair because it integrates seamlessly with Streamlit for dynamic charts
chart = alt.Chart(df).mark_circle(size=60).encode(
    # 'Sales' is fixed on the Y-axis
    y=alt.Y('Sales', title='Sales ($ Thousands)'),
    # The selected variable is on the X-axis
    x=alt.X(selected_variable, title=selected_variable),
    # Add tooltip for interaction
    tooltip=['Sales', selected_variable, 'ShelveLoc', 'City', 'Local']
).properties(
    title=f"Sales vs. {selected_variable}"
).interactive() # Make the chart zoomable and pannable

# Display the chart
st.altair_chart(chart, use_container_width=True)

st.markdown(f"The scatter chart dynamically shows how **Sales** changes with respect to **{selected_variable}**.")

st.header("3.1. Sales Distribution Histogram")

# Create the Histogram using Altair
hist_chart = alt.Chart(df).mark_bar().encode(
    # X-axis: Sales, calculating frequency per bin using binning
    x=alt.X('Sales', bin=alt.Bin(maxbins=30), title='Sales ($ Thousands)'),
    # Y-axis: Count (Frequency)
    y=alt.Y('count()', title='Frequency'),
    tooltip=['Sales', 'count()']
).properties(
    title="Distribution of Sales"
).interactive()

st.altair_chart(hist_chart, use_container_width=True)

st.markdown("""
This histogram helps determine if the **Sales** data is skewed (Skewness) or if it has multiple peaks (Modality).
""")