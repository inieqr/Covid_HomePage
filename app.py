import streamlit as st
from streamlit.components.v1 import html

st.markdown("<h1 style='text-align: center; color: black;'>COVID-19 Prediction App</h1>", unsafe_allow_html=True)

# # Set the page title
# with st.container():
#   st.title("COVID-19 Prediction App")

# Add a picture
st.image("https://upload.wikimedia.org/wikipedia/commons/8/82/SARS-CoV-2_without_background.png")

# Add a button
# st.button("Click here to go to Google", href="https://www.google.com")

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

st.button('Open link', on_click=open_page, args=('https://streamlit.io',))

# # Display the page
# st.show()
