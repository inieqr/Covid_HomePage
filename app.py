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

col1, col2, col3 = st.columns(3)

with col1:
   st.image("air_trans.png")
.png

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")
   


with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

# Add a button
def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

# Add buttons
col1, col2 = st.beta_columns(2)
with col1:
    st.button('Know Your Covid-19 Status', on_click=open_page, args=('https://predictcovid.streamlit.app/',))
with col2:
    st.button('Learn More', on_click=open_page, args=('https://my.clevelandclinic.org/health/diseases/21214-coronavirus-covid-19',))
    
# st.button('Open link', on_click=open_page, args=('https://predictcovid.streamlit.app/'))

# # Display the page
# st.show()
