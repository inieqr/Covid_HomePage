import streamlit as st

st.markdown("<h1 style='text-align: center; color: black;'>COVID-19 Prediction App</h1>", unsafe_allow_html=True)

# # Set the page title
# with st.container():
#   st.title("COVID-19 Prediction App")

# Add a picture
st.image("https://upload.wikimedia.org/wikipedia/commons/8/82/SARS-CoV-2_without_background.png")

# Add a button
# st.button("Click here to go to Google", href="https://www.google.com")
def get_st_button_a_tag(url_link, button_name):
    """
    generate html a tag
    :param url_link:
    :param button_name:
    :return:
    """
    return f'''
    <a href={https://predictcovid.streamlit.app/}><button style="
    fontWeight: 400;
    padding: 0.25rem 0.75rem;
    borderRadius: 0.25rem;
    margin: 0px;
    lineHeight: 1.6;
    width: auto;
    userSelect: none;
    backgroundColor: #FFFFFF;
    border: 1px solid rgba(49, 51, 63, 0.2);">{CLick To Predict}</button></a>
    '''
st.markdown(get_st_button_a_tag('https://predictcovid.streamlit.app/', 'Click To Predict'), unsafe_allow_html=True)

# Display the page
st.show()
