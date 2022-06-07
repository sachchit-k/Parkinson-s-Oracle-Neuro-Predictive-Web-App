import streamlit as st

def app():
    # st.title('Home')
    
    new_title = '<p style="font-family:sans-serif; color:white; font-size: 42px;">Intelligent technology you can trust</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.write('72% of internet users look for health information onlines')
    st.write(''' Our web application provides you with a fast and accurate health assessment
                Parkinson's disease is a progressive nervous system disorder that affects movement. Symptoms start gradually, sometimes starting with a barely noticeable tremor in just one hand. Tremors are common, but the disorder also commonly causes stiffness or slowing of movement.

                   (1)Enter your symptoms
                   (2)Click on Predict 
                   (3)Done! 


                    Your assessment will reveal:
                    1.the predicted disease
                    2.description of that disease
                    3.suggestions''')


 
    st.write('This is basic Machine Learning and Deep Learning based WebApp.')
    st.write('These Machine Learning model is trained on large dataset .')
              

#     st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background: url("https://d10lvax23vl53t.cloudfront.net/images/news/ImageForNews_14305_16110760529976243.jpg")
        
#     }
#    .sidebar .sidebar-content {
#         background: url("url_goes_here")
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )