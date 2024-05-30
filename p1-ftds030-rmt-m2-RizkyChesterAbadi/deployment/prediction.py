import pandas as pd
import streamlit as st
import numpy as np
import pickle
import json

#Load All files
#Load model

with open('list_num_feature.txt', 'r') as file_1:
  listfeaturenum = json.load(file_1)

with open('list_kat_feature.txt', 'r') as file_2:
  listfeaturekat = json.load(file_2)

with open('transformer.pkl', 'rb') as file_3:
  transformer = pickle.load(file_3)

with open('grid_pipeRF.pkl', 'rb') as file_4:
  model_grid_pipeRF = pickle.load(file_5)

def run():
    with st.form('smoking_drinking_dataS'):
        #Age, value untuk default value
        name = st.text_input('Age', value = ' ')

        
        age = st.number_input('height', value = 25, min_value = 15, max_value = 60, help = 'isi dengan tinggi pemain')

        
        height = st.number_input('weight', value = 170, min_value = 100, help = 'in cm')

        weight = st.slider('Weight', value = 70, min_value = 50, max_value = 150)

        price = st.number_input('Price', value = 0)

        st.markdown('---')
    

        tot_chole = st.number_input('tot_chole', min_value = 0, max_value = 100, value = 50)
        HDL_chole = st.number_input('HDL_chole', min_value = 0, max_value = 100, value = 50)
        LDL_chole = st.number_input('LDL_chole', min_value = 0, max_value = 100, value = 50)
        

        #membuat submit button form
        submitted = st.form_submit_button('Predict')

    data_inf = {'sex': sex,
    'age': age, 
    'height': height, 
    'weight': weight, 
    'waistline': waistline, 
    'sight_left': sight_left, 
    'sight_right': sight_right, 
    'hear_left': hear_left, 
    'hear_right': hear_right, 
    'SBP': SBP, 
    'DBP': DBP, 
    'BLDS': BLDS, 
    'tot_chole': tot_chole, 
    'HDL_chole': HDL_chole, 
    'LDL_chole': LDL_chole, 
    'triglyceride': triglyceride, 
    'hemoglobin': hemoglobin, 
    'urine_protein': urine_protein, 
    'serum_creatinine': serum_creatinine, 
    'SGOT_AST': SGOT_AST, 
    'SGOT_ALT': SGOT_ALT, 
    'gamma_GTP': gamma_GTP, 
    'SMK_stat_type_cd': SMK_stat_type_cd,
    'DRK_YN': DRK_YN 
        
    }
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        #split between numerical and categorical columns
        df_inf_num = df_inf[listfeaturenum]
        df_inf_cat = df_inf[listfeaturekat]
        
        #feature scaling and encoding

        # Memprediksikan Menggunakan Model Terbaikyaitu Random Forest  
        y_pred_inf = grid_pipeRF.predict(df_inf)
        print('Drunkard:',y_pred_inf) #before
        print('Drunkard:',round(y_pred_inf[0])) #after
        st.write('## Drunkard : ', str(int(y_pred_inf)))


if __name__ == '__main__':
   run()


