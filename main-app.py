import streamlit as st

# ----- Page Configuration -----
aboutme_page = st.Page(
    page = "views/aboutme.py",
    title = "About Me",
    icon = "👤",
    default=True,
)

certifications_page = st.Page(
    page = "views/certifications.py",
    title = "Certifications",
    icon = "📜",
)

contact_page = st.Page(
    page = "views/contact_me.py",
    title = "Contact",
    icon = "📧",
)

projects_page = st.Page(
    page = "views/projects.py",
    title = "Projects",
    icon = "💻",
)

internship_page = st.Page(
    page = "views/internship.py",
    title = "Internship",
    icon = "📚",
)


# ----- Page Navigation ----- [without sections] 

# pg = st.navigation(pages=[ aboutme_page, certifications_page, contact_page, projects_page,])

# ----- Page Navigation ----- [with sections]

pg = st.navigation(pages=
    {
        "About Me": [aboutme_page, certifications_page],
        "Contact": [contact_page],
        "Projects": [projects_page, internship_page],
    }
)

# ----- shared components -----
# st.logo("assets/bmw_logo.png")
st.sidebar.text(" Made by : \n Himanshu Chaudhari")


# ----- Run Navigation -----
pg.run()