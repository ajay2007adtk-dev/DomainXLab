import streamlit as st

# Page config
st.set_page_config(page_title="My Portfolio", page_icon="🌟")

# Sidebar
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

# Home
if menu == "Home":
    st.title("👩‍💻INNO_IDEAS")
    st.subheader("Aspiring Full Stack ")
    st.write("Welcome to my Streamlit portfolio!")
# About
elif menu == "About":
    st.header("📌 About Me")
    st.write("""
    - Beginner Electronics and communication Engineer   
    - Learning Python, C, Streamlit  
    - Interested in Music and Traveling""")

# Projects
elif menu == "Travel Content App":
    st.header("🛠 Traveled Palce History")
    st.write("🔹 Customer Feedback System")
    st.write("🔹 Travel Content App")
    st.write("🔹 GitHub Portfolio Website")

# Contact
elif menu == "Contact":
    st.header("📞 Contact Me")
    email = st.text_input("Enter your email")
    msg = st.text_area("Your message")

    if st.button("Send"):
        st.success("Message sent successfully ✅")
