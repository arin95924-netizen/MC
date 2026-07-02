import streamlit as st

st.set_page_config(page_title="About Us", page_icon="🤖", layout="wide")

st.title("🤖 About Our ML Project")

st.markdown("---")

col1, col2 = st.columns([2,1])

with col1:
    st.header("📌 Project Overview")

    st.write("""
    Welcome to our Machine Learning project!

    This application is designed to make predictions using advanced Machine Learning algorithms.
    Our goal is to provide users with fast, accurate, and easy-to-understand results through
    a simple and interactive web interface built with Streamlit.

    Whether you're a student, researcher, or professional, this platform helps you analyze
    data and generate predictions efficiently.
    """)

    st.header("🎯 Our Objectives")

    st.markdown("""
    - Build an easy-to-use ML application.
    - Provide accurate predictions.
    - Deliver a clean and responsive interface.
    - Make Machine Learning accessible for everyone.
    """)

with col2:
    st.image(
        "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=500",
        use_container_width=True,
    )

st.markdown("---")

st.header("⚙️ Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **Frontend**
    - Streamlit
    - HTML
    - CSS
    """)

with col2:
    st.success("""
    **Machine Learning**
    - Python
    - Scikit-learn
    - Pandas
    - NumPy
    """)

with col3:
    st.warning("""
    **Visualization**
    - Matplotlib
    - Seaborn
    - Plotly
    """)

st.markdown("---")

st.header("✨ Key Features")

st.markdown("""
✅ User-friendly Interface

✅ Fast Predictions

✅ Real-time Input Processing

✅ Interactive Visualizations

✅ Accurate Machine Learning Model

✅ Responsive Design
""")

st.markdown("---")

st.header("👨‍💻 Developer")

st.write("""
This project was developed as a Machine Learning application using Python and Streamlit.
It demonstrates how modern ML models can be integrated into an interactive web application
to solve real-world problems.
""")

st.markdown("---")

st.caption("© 2026 Machine Learning Project | Built with ❤️ using Streamlit")
if st.button("back to home"):
    st.switch_page("app.py")