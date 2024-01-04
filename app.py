import streamlit as st
import auth 

conn = auth.Connect()

st.title('Test1')

st.write(conn.get_collection('test-col').get().to_dict())