# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 15:12:22 2021

@author: acer
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 00:13:16 2021

@author: acer
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score


loaded_model=pickle.load(open('parkinsons/apps/trained_model1.sav','rb'))

def parkinsons_prediction(input_data):
    

   # scaler=StandardScaler()
   # input_data=tuple(float(x.strip()) for x in input("give input: ").split(','))
   # changing input data to a numpy array
   input_data_as_numpy_array = np.asarray(input_data)

   # reshape the numpy array
   input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

   # standardize the data
   # std_data = StandardScaler.transform(input_data_reshaped)

   prediction = loaded_model.predict(input_data_reshaped)
   print(prediction)


   if (prediction[0] == 0):
     return'The Person does not have Parkinsons Disease'

   else:
    return'The Person has Parkinsons'
  
    
  
def main1():
    
    
    # giving a title
    st.title('parkinsons prediction web app' )
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
    
    
    # getting the input data from the user
    
   													
    # MDVP:Fo(Hz) = st.text_input('Number of Pregnancies')
    # MDVP:Fhi(Hz) = st.text_input('Glucose Level')
    # MDVP:Flo(Hz) = st.text_input('Blood Pressure value')
    # MDVP:Jitter = st.text_input('Skin Thickness value')
    # MDVP:Jitter(Abs) = st.text_input('Insulin Level')
    # MDVP:RAP = st.text_input('BMI value')
    # MDVP:PPQ = st.text_input('Diabetes Pedigree Function value')
    # Jitter:DDP = st.text_input('Age of the Person')
    # MDVP:Shimmer = st.text_input('Age of the Person')
    # MDVP:Shimmer(dB) = st.text_input('Age of the Person')
    # Shimmer:APQ3 = st.text_input('Age of the Person')
    # Shimmer:APQ5 = st.text_input('Age of the Person')
    # MDVP:APQ = st.text_input('Age of the Person')
    # Shimmer:DDA = st.text_input('Age of the Person')
    # NHR = st.text_input('Age of the Person')
    # HNR= st.text_input('Age of the Person')
    # RPDE= st.text_input('Age of the Person')
    # DFA= st.text_input('Age of the Person')
    # spread1= st.text_input('Age of the Person')
    # spread2= st.text_input('Age of the Person')
    # D2= st.text_input('Age of the Person')
    # PPE= st.text_input('Age of the Person')
    aaa = st.text_input('Rapid Eye Movement?', key="111     ")
    bbb= st.text_input('olfactory loss,?', key="222")
    a = st.text_input('MDVP:Fo(Hz)', key="1")
    b= st.text_input('MDVP:Fhi(Hz)', key="2")
    c= st.text_input('MDVP:Flo(Hz)', key="3")
    d= st.text_input('MDVP:Jitter(%)', key="4")
    e= st.text_input('MDVP:Jitter(Abs)', key="5")
    f= st.text_input('MDVP:RAP', key="6")
    g= st.text_input('MDVP:PPQ', key="7")
    h= st.text_input('Jitter:DDP', key="8")
    ll= st.text_input('MDVP:Shimmer', key="9")
    j= st.text_input('MDVP:Shimmer(dB)', key="10")
    k= st.text_input('Shimmer:APQ3', key="11")
    l= st.text_input('Shimmer:APQ5', key="12")
    m= st.text_input('MDVP:APQ', key="13")
    n= st.text_input('Shimmer:DDA', key="14")
    o= st.text_input('NHR', key="15")
    p= st.text_input('HNR', key="16")
    q= st.text_input('RPDE', key="17")
    r= st.text_input('DFA', key="18")
    s= st.text_input('Spread1', key="19")
    t= st.text_input('Spread2', key="20")
    u= st.text_input('D2', key="21")
    v= st.text_input('PPE', key="22")
    
    
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('parkinsons Test Result'):
        diagnosis = parkinsons_prediction([a,b,c,d,e,f,g,h,ll,j,k,l,m,n,o,p,q,r,s,t,u,v])
   
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main1()
    
    
