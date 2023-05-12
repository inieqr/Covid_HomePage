import streamlit as st

st.markdown("<h1 style='text-align: center; color: grey;'>COVID-19 Prediction App</h1>", unsafe_allow_html=True)



# # Set the page title
# with st.container():
#   st.title("COVID-19 Prediction App")

# Add a picture
st.image("https://upload.wikimedia.org/wikipedia/commons/8/82/SARS-CoV-2_without_background.png")

# Add a button
st.button("Click here to go to Google", href="https://www.google.com")

# Display the page
st.show()
