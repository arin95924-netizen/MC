import streamlit as st
import joblib
st.set_page_config(
page_title="preiction page",
page_icon="🤖",
layout="wide"
)


model = joblib.load("marks_model.pkl")

st.title("🎓 Student Marks Predictor")

study = st.slider("Study Hours", 0.0, 12.0, 5.0)
attendance = st.slider("Attendance (%)", 0, 100, 80)
previous = st.slider("Previous Marks", 0, 100, 70)
assignments = st.slider("Assignments Completed", 0, 10, 5)

if st.button("Predict Marks"):
    prediction = model.predict([[study, attendance, previous, assignments]])
    st.success("predicted marks is : " + str(round(prediction[0],2)))
st.markdown("""-----""")
if st.button("Back to home"):
    st.switch_page("app.py")