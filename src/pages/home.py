import streamlit as st
from src.database.database_client import get_stocks_list
from src.ui_elements.stock_analysis import get_stock_analysis


st.set_page_config(layout="wide")

stocks = get_stocks_list()

if "selected_stock" not in st.session_state:
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
    st.write("Analysis for", st.session_state.selected_stock)
    get_stock_analysis(st.session_state.selected_stock)
