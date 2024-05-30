import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    # Membuat Judul
    st.title(' Drunkard or Not Rating Prediction')

    # Membuat sub Header
    st.subheader('EDA untuk analisa dataset Drunkard')

    #tambahkan gambar 
    image = Image.open('wine1.jpg')
    st.image(image, caption='Wine ')

    #Menambahkan deskripsi
    st.write('## Model ML dibuat untuk mengetahui apakah Seseorang bisa dianggap sebagai pecandu Minuman atau tidak')




    #mmebuat batas dengan garis lurus
    st.markdown('---')

    #show dataframe
    data = pd.read_csv(r'smoking_drinking_dataS.csv')
    st.dataframe(data)

    #membuat bar plot
    st.write('#### Total Kolestrol')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='tot_chole ', data = data)
    st.pyplot(fig)

    #membuat histogram
    st.write('#### Histogram of Drunkard or Tot')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data['DRNK_YN'], bins = 30, kde = True)
    st.pyplot(fig)

    #membuat histogram berdasarkan input user
    st.write('#### Histogram berdasarkan input user')
    option = st.selectbox('Pilih column : ', ('Age', 'Weight', 'Height', 'tot_chole ', 'HDL_chole'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[option], bins = 30, kde = True)
    st.pyplot(fig)

    #membuat plotly plot
    #membandingkan apakah seseorang termasuk Pemabuk/ Tidak dengan Kebiasaan merokok
    st.write('#### Plotly plot - SMK_stat_type_cd vs DRN_YN')
    fig = px.scatter(data, x = 'SMK_stat_type_cd', y = 'DRNK_YN', hover_data = ['Age', 'Weight', 'Height', 'tot_chole ', 'HDL_chole'])
    st.plotly_chart(fig)

if __name__ == '__main__':
    run()
