import pickle as pkl
import streamlit as st
import pandas as pd

def run():
    #loading file pickle
    with open('model.pkl', 'rb') as file_1:
        Hmodel_svm= pkl.load(file_1)


    
    with st.form("Form Data Pembayaran Bulan Selanjutnya"):
        title = st.text_input('sex (male/female)' )
        Age_val = st.number_input("Age",min_value=10, max_value=80)
        nextmonth_payment = st.text_input('default_payment_next_month (Yes/No)')

        sub=st.form_submit_button("Submit data Pembayaran")

    data_predict={
    'Age':Age_val,
    'default_payment_next_month': nextmonth_payment
    }
    st.dataframe(pd.DataFrame([data_predict]))

    hasil_predict=Hmodel_svm.predict(data_predict)

    st.write('Prediksi Pembayaran Bulan Depan', title, 'dengan umur:', Age_val, 'dan Bulan depan harus membayar: ', nextmonth_payment, hasil_predict[0])


