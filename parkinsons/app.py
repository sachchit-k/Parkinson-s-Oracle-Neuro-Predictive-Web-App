import streamlit as st
from multiapp import MultiApp
from apps import home, parkinsonswebapp# import your app modules here

app = MultiApp()

st.markdown("""

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("parkinson's  disease  prediction", parkinsonswebapp.main1)




# The main app
app.run()
