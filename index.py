import streamlit as st

pages = {
    "Dashboard": [
        st.Page("src/pages/home.py", title="Home", icon=":material/home:"),
    ],
    "Config": [
        st.Page("src/pages/settings.py", title="Settings", icon=":material/settings:"),
    ],
}

pg = st.navigation(pages)
pg.run()
