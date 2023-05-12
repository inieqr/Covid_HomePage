import streamlit as st
from link_button import link_button

st.markdown("<h1 style='text-align: center; color: black;'>COVID-19 Prediction App</h1>", unsafe_allow_html=True)

# # Set the page title
# with st.container():
#   st.title("COVID-19 Prediction App")

# Add a picture
st.image("https://upload.wikimedia.org/wikipedia/commons/8/82/SARS-CoV-2_without_background.png")

# Add a button
# st.button("Click here to go to Google", href="https://www.google.com")
link_button('Click Me!', 'https://docs.streamlit.io/en/stable/')

# Display the page
st.show()
