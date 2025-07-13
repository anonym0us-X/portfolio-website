import streamlit as st
from forms.contact import contact_form

# st.title("About Me")
# st.write("""
#     Hello! I'm Himanshu Chaudhari, a passionate software developer with a keen interest in creating innovative solutions. 
#     I love exploring new technologies and continuously improving my skills.
    
#     Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/himanshu-chaudhari-1b0a1b1b0/) or check out my projects on [GitHub](
#          https://github.com/anonym0us-X).
#     In my free time, I enjoy reading tech blogs, contributing to open-source projects, and learning about the latest trends in software development.
#     Thank you for visiting my portfolio!
# """)

# # Add more sections or details about yourself as needed


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

col1, col2 = st.columns(2,gap = "small", vertical_alignment="center")
with col1:
    st.image("assets/profile.jpg", width=230)
with col2:
    st.title("Himanshu Tushar Chaudhari")
    st.write("Software Developer, Web Developer, Cyber Security Enthusiast, and Open Source Contributor")

    if st.button("Contact me"):
        show_contact_form()




# ----- Myself -----
st.write("\n")
st.subheader("Introduction", anchor= False)
st.write("Hello there, I am Himanshu Tushar Chaudhari. I am a passionate software developer with a keen interest in creating innovative solutions. I love exploring new technologies and continuously improving my skills.")

st.write("Following is my skillset :")
st.write("\n")



st.subheader("Skills", anchor= False)
st.write("""
        - **Programming Languages**: Python, JavaScript.
        - **Web Development**: HTML, CSS, JavaScript
        - **Frameworks**: Flask, Django, Fast API, NextJS, Tailwind CSS.
        - **Cyber Security**: Ethical Hacking, Vulnerability Assessment, RAT, StegnoGraphy.
        - **Tools**: Git, Docker, Github, VS Code.
        - **Databases**: MySQL, MongoDB, Postgre SQL.
        """)




 

# ----- Experience and Skills -----
st.write("\n")
st.subheader("Experience", anchor= False)
st.write("""
        - **Full Stack Developer intern**: Developed multiple Kaizen Report project using Python, JavaScript and framework NextJS.
        - **Python developer intern**: Developed a web application using django and python.
        - **Cyber Security Enthusiast**: Passionate about security practices and ethical hacking, and developed a basic RAT and keylogger.
        - **Open Source Contributor**: Actively contributing to various open-source projects.
        """)
st.write("\n")
