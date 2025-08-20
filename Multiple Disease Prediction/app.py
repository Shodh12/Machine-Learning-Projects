
import pickle

import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model
diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('saved_models/parkinsons_model.sav', 'rb'))


#option menu for navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],

                            icons=['activity', 'heart', 'person'],
                            menu_icon='cast',

                            default_index=0)
    

# Diabetes Prediction Page

if selected == 'Diabetes Prediction':

    st.title('Diabetes Prediction using ML')

    # Collumns for input fields
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        Pregencies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')

    with col4:
        SkinThickness = st.text_input('Skin Thickness Value')

    with col1:
        Insulin = (st.text_input('Insulin Level') )

    with col2:
        BMI = st.text_input('BMI Value')
    
    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree')

    with col4:
        Age = st.text_input('Age of the Person')

    #code for prediction
    diab_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregencies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

if selected == 'Heart Disease Prediction':

    st.title('Heart Disease Prediction using ML')

    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain Type')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestoral')
    fbs = st.text_input('Fasting Blood Sugar')
    restecg = st.text_input('Resting Electrocardiographic')
    thalach = st.text_input('Maximum Heart Rate ')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST Depression Induced ')
    slope = st.text_input('Slope of the Peak Exercise')
    ca = st.text_input('Number of Major Vessels')
    thal = st.text_input('Thalassemia')



    #code for the prediction
    heart_diagnosis = ''

    # Creating the button for the prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if heart_prediction[0] ==1:
            heart_diagnosis = 'The person is likely to have heart disease'
        else:
            heart_diagnosis = 'The person is not likely to have heart disease'
    
    st.success(heart_diagnosis)
    

if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')

    # Collumns for input fields
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:  
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col1:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col2:
        RAP = st.text_input('MDVP:RAP')
    with col3:
        PPQ = st.text_input('MDVP:PPQ')
    with col4:
        DDP = st.text_input('Jitter:DDP')
    with col1:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col2:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col3:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col1:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col2:
        APQ = st.text_input('MDVP:APQ')
    with col3:
        DDA = st.text_input('Shimmer:DDA')
    with col4:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('Spread1')
    with col1:
        spread2 = st.text_input('Spread2')
    with col2:
        D2 = st.text_input('D2')
    with col3:
        PPE = st.text_input('PPE')  

    #code for prediction
    parkinsons_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Parkinsons Test Result'):

        parkinson_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE
                                                        ]])
        if parkinson_prediction[0] == 1:
            parkinsons_diagnosis = 'The person is likely to have Parkinsons disease'
        else:
            parkinsons_diagnosis = 'The person is not likely to have Parkinsons disease'

    st.success(parkinsons_diagnosis)