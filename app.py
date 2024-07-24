import streamlit as st
st.set_page_config(page_icon="👍",page_title="streamlit")

st.title("Bellamkonda Gayatri Srija",anchor=False)

st.subheader("Student")

with st.container(border=True):
    st.info("I am Gayatri Srija,a Student From Vishnu Institute Of Technology")

col1,col2,col3=st.columns(3)
with col1:
    with st.expander(label="know me more",expanded=False):
        st.warning("Hii")
        st.image("image.jpeg",width=100)
with col2:
    with st.expander(label="know me more",expanded=False):
        st.warning("Hello")
with col3:
    with st.expander(label="know me more",expanded=False):
        st.warning("Heyy")