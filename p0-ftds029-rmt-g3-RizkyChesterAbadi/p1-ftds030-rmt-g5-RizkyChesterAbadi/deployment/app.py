import prediction
import eda

import streamlit as st
PAGES = {"EDA":eda, "Model Prediction":prediction
}
st.sidebar.title('Navigation')
selection= st.sidebar.radio("Go To", list(PAGES.keys()))

page = PAGES[selection]
page.run()
