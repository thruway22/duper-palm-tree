import streamlit as st
import datetime
import pandas as pd
import auth 

db = auth.Connect()

st.title('Test2')

tab1, tab2, tab3, tab4 = st.tabs(['Performance', 'Transactions', 'Rebalancing', 'Fund'])

with tab1:

    # st.write(db.get_collection('test-col').get().to_dict())

    docs = db.get_collection("test-col").stream()

    for doc in docs:
        st.write(f"{doc.id} => {doc.to_dict()}")


    data = {
        "stringExample": "Hello, World!",
        "booleanExample": True,
        "numberExample": 3.14159265,
        "dateExample": datetime.datetime.now(tz=datetime.timezone.utc),
        "arrayExample": [5, True, "hello"],
        # "nullExample": None,
        # "objectExample": {"a": 5, "b": True},
    }

    add = st.button('add')
    if add:
        db.get_collection("test-col").add(data)






    st.write(db.get_collection('test-col').document("USvxq0zBam4Q0JeG5gdF").get().to_dict())

    raw = db.get_collection('test-col').document("USvxq0zBam4Q0JeG5gdF").get().to_dict()["arrayExample"]

    st.write(pd.DataFrame(raw))
