import streamlit as st
from streamlit.components.v1 import html
import webbrowser


# st.markdown("<h1 style='text-align: center; color: #474646;'>COVID-19 Prediction App</h1>", unsafe_allow_html=True)

# # Set the page title
# with st.container():
#   st.title("COVID-19 Prediction App")

# Add a picture
# st.image("https://upload.wikimedia.org/wikipedia/commons/8/82/SARS-CoV-2_without_background.png")
st.image("https://fscluster.org/sites/default/files/styles/core-group-featured-image/public/banner-696x321.png?itok=l7uFday9")

# Add textual information
st.markdown("<h1 style='text-align: center; color: red;'>What Is Covid-19</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #2a2b2a;'>Coronavirus</h1>", unsafe_allow_html=True)
st.write("Coronaviruses are a large family of viruses that are known to cause diseases ranging from colds to more severe diseases such as Middle Eastern respiratory syndrome (MERS) and severe acute respiratory syndrome (SARS). Symptoms of COVID-19 are similar to those of a cold at first. However, the disease can cause severe pneumonia, which can be fatal.")

st.markdown("<h2 style='text-align: center; color: #2a2b2a;'>Contagion</h1>", unsafe_allow_html=True)
st.write("COVID-19 is spread primarily when people are in close contact and one person inhales small drops produced by an infected person when coughing, sneezing or talking.")

def open_support_ticket():
    email_link = "mailto:servicesdesk@evilcorp.com"
    webbrowser.open(email_link)

st.button("Contact us!", on_click=open_support_ticket)

col1, col2, col3 = st.columns(3)

with col1:
   st.markdown("<h4 style='text-align: center; color: #2a2b2a;'>Air Transmission</h4>", unsafe_allow_html=True)
   st.image("https://bloximages.chicago2.vip.townnews.com/fox23.com/content/tncms/assets/v3/editorial/6/34/634b7242-5d49-5093-94c3-bf7f084e7efd/63e62776a4697.image.jpg?resize=736%2C474")
   st.write("Through respiratory droplets produced when an infected person coughs, sneezes, or talks")
   
with col2:
   st.markdown("<h4 style='text-align: center; color: #2a2b2a;'>Human Contact</h4>", unsafe_allow_html=True)
   st.image("https://contact-centres.com/wp-content/uploads/2018/05/human-touch-image-may-2018.jpg")
   st.write("Any person who was within 6 feet of an infected person for at least 15 minutes, starting from 2 days before illness")
   
with col3:
   st.markdown("<h4 style='text-align: center; color: #2a2b2a;'>Contaminated Surfaces</h4>", unsafe_allow_html=True)
   st.image("https://static01.nyt.com/images/2020/05/27/well/well-surfaces-door/well-surfaces-door-mobileMasterAt3x-v3.jpg?quality=75&auto=webp&disable=upscale&width=1200")
   st.write("Touching a surface or object on which there is a virus, and then touching your own mouth, nose, or your eyes")

st.markdown("<h2 style='text-align: center; color: #2a2b2a;'>Symptoms</h1>", unsafe_allow_html=True)
st.write("COVID-19 symptoms are varied, but usually include fever and cough. Some people without symptoms may spread the virus. The most common symptoms in humans include:")
st.image("https://images.ctfassets.net/pxcfulgsd9e2/articleImage160692/bab314f288123a1eedf3759bd17d0225/Top-5-Symptoms-of-COVID-19-HN2387-iStock-1217199413-Sized.png?f=top&fit=fill&fm=webp&h=450&q=35&w=800")

# Add buttons
def open_page1(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

def open_page2(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)
   
st.markdown("<h5 style='text-align: center; color: #2a2b2a;'>Check your COVID-19 status today with our machine learning model. Click 'Check my status' to know your COVID 19 status and 'Learn More' to know more about COVID 19.</h5>", unsafe_allow_html=True)

# Add buttons
#col1, col2 = st.beta_columns(2)
#with col1:
#    st.button('Know Your Covid-19 Status', on_click=open_page1, args=('https://predictcovidgo.streamlit.app/',))
#with col2:
#    st.button('Learn More', on_click=open_page2, args=('https://my.clevelandclinic.org/health/diseases/21214-coronavirus-covid-19',))


st.button('Check my status', on_click=open_page1, args=('https://predictcovidgo.streamlit.app/',))
st.button('Learn More', on_click=open_page2, args=('https://my.clevelandclinic.org/health/diseases/21214-coronavirus-covid-19',))


# # Display the page
# st.show()
