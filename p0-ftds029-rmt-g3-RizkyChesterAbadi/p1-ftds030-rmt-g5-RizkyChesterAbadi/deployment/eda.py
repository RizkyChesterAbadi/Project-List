import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


def run ():
    st.title('Eksploratory Data Analysis')
    #Menampilkan table
    df1=pd.read_csv(r'C:\Users\rizqc\Documents\Tugas Tugas\p1-ftds029-rmt-g5-RizkyChesterAbadi\P1G5_SET_1_RizkyChester.csv')

    st.write(df1)
   
   #Visualisasi 
    st.write('Visualisasi')

    option1=st.selectbox('Kolom1',('limit_balance','sex','education_level','marital_status','age','pay_0','pay_2','pay_3','pay_4','pay_5','pay_6','bill_amt_1','bill_amt_2','bill_amt_3','bill_amt_4','bill_amt_5','bill_amt_6','pay_amt_1','pay_amt_2','pay_amt_3','pay_amt_4','pay_amt_5','pay_amt_6','default_payment_next_month' ))
                                

    option2=st.selectbox('Kolom2',('limit_balance','sex','education_level','marital_status','age','pay_0','pay_2','pay_3','pay_4','pay_5','pay_6','bill_amt_1','bill_amt_2','bill_amt_3','bill_amt_4','bill_amt_5','bill_amt_6','pay_amt_1','pay_amt_2','pay_amt_3','pay_amt_4','pay_amt_5','pay_amt_6','default_payment_next_month' ))

    st.write('You Selected:', option1, 'and', option2)

    fig,ax = plt.subplots()
    ax.scatter(df1[option1],df1[option2])
    st.pyplot(fig)