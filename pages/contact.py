import streamlit as st
st.set_page_config(page_title='contact us',page_icon='📊',layout='wide')
st.title(" 📞 contact us")
st.markdown("""------""")

st.markdown(
    """
    <p style='text-align:center; color:#4F8BF9;'>
    </p>""",
unsafe_allow_html=True)
a,b=st.columns([2,1])
with a:
    st.write(""""Have questions, feedback, or suggestions?  We're here to help! If you have any queries about our Machine                              Learning                     project, encounter any issues, or                  want to share your feedback, feel free to reach           out. We value your                                     input and will get back to you as soon as possible""")
with b:
    st.image("https://images.unsplash.com/photo-1677442136019-21780ecad995?w=700",
        use_container_width=True)
st.markdown("""-------""")
