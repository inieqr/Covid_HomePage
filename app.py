import streamlit as st
from streamlit.components.v1 import html

st.markdown("<h1 style='text-align: center; color: #474646;'>COVID-19 Prediction App</h1>", unsafe_allow_html=True)

# # Set the page title
# with st.container():
#   st.title("COVID-19 Prediction App")

# Add a picture
st.image("https://upload.wikimedia.org/wikipedia/commons/8/82/SARS-CoV-2_without_background.png")

# Add textual information
st.markdown("<h1 style='text-align: center; color: red;'>What Is Covid-19</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #2a2b2a;'>Coronavirus</h1>", unsafe_allow_html=True)
st.write("Coronaviruses are a large family of viruses that are known to cause diseases ranging from colds to more severe diseases such as Middle Eastern respiratory syndrome (MERS) and severe acute respiratory syndrome (SARS). Symptoms of COVID-19 are similar to those of a cold at first. However, the disease can cause severe pneumonia, which can be fatal.")

st.markdown("<h2 style='text-align: center; color: #2a2b2a;'>Contagion</h1>", unsafe_allow_html=True)
st.write("COVID-19 is spread primarily when people are in close contact and one person inhales small drops produced by an infected person when coughing, sneezing or talking.")

# Add a button
def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

st.button('Open link', on_click=open_page, args=('https://predictcovid.streamlit.app/'))

# # Display the page
# st.show()
