import streamlit as st
st.title("prime number")

a = st.text_input(label="Enter the term number (n)")

if st.button("Submit"):
        n = int(a)
        count=0
        for i in range(1,n+1):
            if(n%i==0):
                count+=1
        if(count==2):
             st.write("prime number")
        else:
            st.write("not a prime number")
    