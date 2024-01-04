import streamlit as st
import auth 

conn = auth.Connect()

st.title('Test')

st.write(conn.get_collection('test-col').document('test-doc').get().to_dict())