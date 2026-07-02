import streamlit as st

st.set_page_config(
    page_title="AI Prediction System",
    page_icon="🤖",
    layout="wide"
)

# ---------------- HERO ---------------- #

st.markdown(
    """
    <h1 style='text-align:center; color:#4F8BF9;'>
        🤖 AI & Machine Learning Prediction System
    </h1>
    <h4 style='text-align:center; color:gray;'>
        Fast • Accurate • Intelligent Predictions
    </h4>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

left, right = st.columns([2,1])

with left:
    st.markdown("## 🚀 Welcome")

    st.write("""
This intelligent Machine Learning application helps users generate
accurate predictions from input data using trained ML models.

Whether you're a student, researcher, or professional,
our system provides a simple interface with powerful prediction capabilities.
""")

    if st.button("🚀 Start Prediction", use_container_width=True):
        st.switch_page("pages/prdiction.py")

with right:
    st.image(
        "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=700",
        use_container_width=True
    )

st.markdown("---")

# ---------------- FEATURES ---------------- #

st.header("✨ Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("""
### ⚡ Fast

Instant prediction results with optimized ML models.
""")

with c2:
    st.success("""
### 🎯 Accurate

Built using trained Machine Learning algorithms.
""")

with c3:
    st.warning("""
### 📊 Analytics

Easy visualization and result interpretation.
""")

st.markdown("---")

# ---------------- HOW IT WORKS ---------------- #

st.header("🛠 How It Works")

a, b, c, d = st.columns(4)

a.metric("Step 1", "Enter Data")
b.metric("Step 2", "Model Analysis")
c.metric("Step 3", "Prediction")
d.metric("Step 4", "View Results")

st.markdown("---")

# ---------------- TECHNOLOGIES ---------------- #

st.header("💻 Technologies")

col1, col2, col3, col4 = st.columns(4)

col1.success("🐍 Python")
col2.info("📈 Pandas")
col3.warning("🤖 Scikit-Learn")
col4.error("🎨 Streamlit")

st.markdown("---")

# ---------------- MODEL PERFORMANCE ---------------- #

st.header("📈 Model Performance")

acc, pre, rec = st.columns(3)

acc.metric("Accuracy", "98.2%", "2%")
pre.metric("Precision", "97.5%", "1.5%")
rec.metric("Recall", "96.8%", "1.2%")

st.progress(98)

st.markdown("---")

# ---------------- FOOTER ---------------- #

st.markdown(
"""
<div style="text-align:center;">
<h3>🎯 Smart Prediction • Better Decisions</h3>
<p>Made with ❤️ using Python & Streamlit</p>
</div>
""",
unsafe_allow_html=True
)
from database import add_user,check_user
username=st.sidebar.text_input("enter your username")
password=st.sidebar.text_input("enter your password",type='password')
col1,col2=st.sidebar.columns(2)
create=col1.button("create")
login=col2.button("login")
if create:
 add_user(username,password)
 st.sidebar.success("your account created")
if login:
  user=check_user(username,password)
  if user:
    st.sidebar.success("login")
  else:
    st.sidebar.error("check your name and password")
        
