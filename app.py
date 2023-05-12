import streamlit as st

# Set the page title
st.title("My Page")

# Add a picture
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Google_Logo.svg/1200px-Google_Logo.svg.png")

# Add a button
st.button("Click here to go to Google", href="https://www.google.com")

# Display the page
st.show()