import streamlit as st
import auth 

db = auth.Connect()

st.title('Test2')

# st.write(conn.get_collection('test-col').get().to_dict())

docs = db.get_collection("test-col").stream()

for doc in docs:
    st.write(f"{doc.id} => {doc.to_dict()}")


data = {
    "stringExample": "Hello, World!",
    "booleanExample": True,
    "numberExample": 3.14159265,
    "arrayExample": [5, True, "hello"],
    "nullExample": None,
    "objectExample": {"a": 5, "b": True},
}

db.collection("test-col").add(city)
