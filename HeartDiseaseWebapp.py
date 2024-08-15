# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:55:16 2024

@author: Hp
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('trained_model.sav','rb'))

#create  a function
def heart_disease_prediction(input_data):
    input_data_array = np.asarray(input_data)
    input_data_reshaped = input_data_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    if(prediction[0]):
      return 'The person has Heart Disease'
    else:
      return 'The person is healthy'
  
def main():
    st.title('Heart disease prediction web app')
    #3,145,233,1,0,150,0,2.3,0,0,1
    #geeting input data from user
    age	= st.number_input('Age ',placeholder='example 63',value=None)
    sex	=st.number_input('Sex ',placeholder='1 = Male; 0 = female',value=None)
    cp =st.number_input('Type of chest pain ',placeholder='example 3',value=None)
    trestbps=st.number_input('The resting Blood Pressure ',placeholder='example 145',value=None)
    chol=st.number_input('Cholestrol ',placeholder='example 233',value=None)
    fbs=st.number_input('Fasting Blood Sugar ',placeholder='example 1 or 0',value=None)
    restecg	=st.number_input('Resting electrocardiographic measurement ',placeholder='example 0',value=None)
    thalach	=st.number_input('Maximum heart rate achieved ',placeholder='example 150',value=None)
    exang =st.number_input('Exercise induced angina ',placeholder='example 0',value=None) 
    oldpeak=st.number_input('ST depression induced by exercise relative to rest ',placeholder='example 2',value=None)
    slope=st.number_input('The slope of the peak exercise ST segment ',placeholder='example 3',value=None)
    ca=st.number_input('Number of major vessels (0-3) colored by flourosopy',placeholder='example 0',value=None)
    thal=st.number_input('Thalassemia (Blood disorder) ',placeholder='example 0',value=None)
    
    
    #prediction
    diagnosis =''
    #button for prediction
    if st.button('Heart Disease Test Result'):
        diagnosis = heart_disease_prediction(
            [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
            )
    st.success(diagnosis)
    
    
    
if __name__=='__main__':
    main()
