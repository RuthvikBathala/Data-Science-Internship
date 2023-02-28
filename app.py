import streamlit as st 

st.title(":green[Innomatics] Data App:smiley:")
st.header("Data Science Internship")
bt=st.button("Click here")

if bt==True:
    st.success(":blue[Congratulations]!	:tada:	:confetti_ball:",icon="✅")
    st.snow()
else:
    st.balloons()
    