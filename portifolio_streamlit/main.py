import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    layout="wide"
)

st.title ("Welcome to My Portfolio")
st.write("""
This is a simple portfolio application built with Streamlit.
Feel free to explore my projects and skills showcased here.
""")

if st.button("Click Me"):
    st.balloons()