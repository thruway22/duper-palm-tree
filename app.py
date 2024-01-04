import streamlit as st
import datetime
import auth 

db = auth.Connect()

st.title('Test2')

# st.write(db.get_collection('test-col').get().to_dict())

docs = db.get_collection("test-col").stream()

for doc in docs:
    st.write(f"{doc.id} => {doc.to_dict()}")


# data = {
#     "stringExample": "Hello, World!",
#     "booleanExample": True,
#     "numberExample": 3.14159265,
#     "dateExample": datetime.datetime.now(tz=datetime.timezone.utc),
#     "arrayExample": [5, True, "hello"],
#     "nullExample": None,
#     "objectExample": {"a": 5, "b": True},
# }

# db.get_collection("test-col").add(data)



st.write(db.get_collection('test-col').get("RvM8sJ87ypRGavSXNoXA").to_dict())

