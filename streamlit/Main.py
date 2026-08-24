import streamlit as st
import pandas as pd


st.markdown('1.2. Displaying basic text')
st.text("This is the title")
st.header("This is the header")
st.subheader("This is a subheader")
st.caption("This is a caption")
st.divider()
st.write("This is my text")

df = pd.DataFrame({"col1":[1, 2, 3, 4], "col2":[10 , 20, 30, 40]})
st.write("Display a Dataframe using st.write", df)


st.divider()
df = pd.read_csv("/home/nexahub/Desktop/Python3/streamlit/Iris/Iris.csv")
df = df.drop(columns=['sepal_width', 'petal_width'])
st.text("Iris Dataset")
st.write(df)

st.divider()
st.latex(r"""a + ar + a r^2""")

st.divider()
st.code("""
x = 123
print(x)
""")


st.divider()
st.text("This is my audio")
st.audio("/home/nexahub/Music/Prince-Indah-Mummy-Chulo.mp3", autoplay=False)

st.divider()
st.image("/home/nexahub/Pictures/Camera/DSC_7270.jpg",caption='Afya ventures', channels="RGB", width="stretch", link="https://streamlit.io")

st.logo("/home/nexahub/Pictures/Camera/DSC_7270.jpg", size="small", link="https://google.com")



# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)



# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


with st.sidebar:
    add_button = st.button(
        label="ClickMe", 
        disabled=False, 
        width="content",
    )

with st.sidebar:
    percent = st.select_slider(
        "Select the number of percentage",
        options=[
            0,
            10,
            20,
            30,
            40,
            50,
            60,
            70,
            80,
            90,
            100
        ],
    )
    st.write("Your percentage is:", percent)