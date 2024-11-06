import numpy as np
import pandas as pd
import streamlit as st

st.title("This is Rawan")
st.write("All of you are very NICE people!!!")
data=pd.DataFrame ({
    "C1": ['A','B','C','D','E'],
    "C2": [100, 200, 300,400,500]
})

st.write("Below are your Marks:")
st. write(data)

chart_data=pd.DataFrame (
    np.random.randn(20,4),
    columns= ['p','Q','R','T']
)

st.bar_chart(chart_data)
