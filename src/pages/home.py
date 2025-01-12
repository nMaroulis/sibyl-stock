import streamlit as st
from src.database.database_client import get_stocks_list
from src.ui_elements.stock_analysis import get_stock_analysis

st.set_page_config(page_title="Home", layout="wide")
st.html("""<style> .block-container { padding-top: 3.5rem; }</style>""")

if "selected_stock" not in st.session_state:
    st.header("Home")
    st.write(
        "Choose the Company you want in order to get all the information available. Once the company is chosen, the Home page 🏠 will display all the information regarding the company and its stock. The advisor tab, using AI and financial formulas and algorithms will determine if the company's stock is worth buying.")
    stocks = get_stocks_list()
    with st.form(key="stocks_form", clear_on_submit=False):
        selected_stock = st.selectbox("Select a Stock to Analyze", stocks, placeholder="Find a Stock", index=None)
        sub_button = st.form_submit_button(label="Generate Analysis", icon=":material/query_stats:")
        if sub_button:
            if selected_stock is None:
                st.warning("You must select a stock to analyze", icon=":material/warning:")
            else:
                st.session_state.selected_stock = selected_stock
                st.write(selected_stock)
                st.rerun()
else:
    if st.sidebar.button("Reset Analysis", type="primary", use_container_width=True, icon=":material/restart_alt:"):
        del st.session_state.selected_stock
        st.rerun()
    with st.spinner("Fetching Stock Data..."):
        get_stock_analysis(st.session_state.selected_stock)
