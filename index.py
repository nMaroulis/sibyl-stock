import streamlit as st

pages = {
    "Dashboard": [
        st.Page("src/pages/home.py", title="Home", icon=":material/home:"),
        st.Page("src/pages/advisor.py", title="Advisor", icon=":material/query_stats:"),

    ],
    "Config": [
        st.Page("src/pages/settings.py", title="Settings", icon=":material/settings:"),
    ],
}

pg = st.navigation(pages)
pg.run()
