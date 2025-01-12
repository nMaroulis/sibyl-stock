import streamlit as st
from src.library.apis.yahoo_client import get_stock_details
import re
from src.plots.stock_info_plots import risk_gauge


def extract_symbol(stock_string) -> str | None:

    match = re.search(r"\[(.*?)\]", stock_string)
    return match.group(1) if match else None


def display_company_info(info: dict, stock_symbol: str):
    st.title(info.get("longName", "Company Information"))
    st.write("Stock symbol: {}".format(stock_symbol))
    st.write(f"**Industry:** {info.get('industryDisp', 'N/A')}")
    st.write(f"**Sector:** {info.get('sectorDisp', 'N/A')}")
    st.write(f"**Country:** {info.get('country', 'N/A')}")
    st.write(f"**Employees:** {info.get('fullTimeEmployees', 'N/A')}")
    st.write(f"**Website:** [Visit Website]({info.get('website', 'N/A')})")

    st.header("Market Data")
    c0, c1, c2 = st.columns(3)
    with c0:
        st.metric("Current Price", str(info.get('currentPrice'))+"$")  if "currentPrice" in info else st.metric("Current Price", "N/A", border=True)
    with c1:
        st.metric("Market Cap", f'{info.get('marketCap'):,}$')  if "marketCap" in info else st.metric("Market Cap", "N/A")
    with c2:
        st.metric("Enterprise Value", f'{info.get('enterpriseValue'):,}$')  if "enterpriseValue" in info else st.metric("Enterprise Value", "N/A")

    # st.write(
    #     f"**Headquarters:** {info.get('address1', 'N/A')}, {info.get('city', 'N/A')}, {info.get('state', 'N/A')}, {info.get('zip', 'N/A')}, {info.get('country', 'N/A')}")
    # st.write(f"**Phone:** {info.get('phone', 'N/A')}")

    # Financial Health Section
    # Create columns for market data and financial metrics
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Market Data")
        st.write(f"**Beta:** {info.get('beta', 'N/A')}")
    with col2:
        st.subheader("Financial Metrics")
        st.write(f"**Trailing P/E:** {info.get('trailingPE', 'N/A')}")
        st.write(f"**Forward P/E:** {info.get('forwardPE', 'N/A')}")
        st.write(f"**Price to Sales (TTM):** {info.get('priceToSalesTrailing12Months', 'N/A')}")
        st.write(f"**Price to Book:** {info.get('priceToBook', 'N/A')}")
        st.write(f"**Profit Margin:** {info.get('profitMargins', 'N/A')}%")
        st.write(f"**Operating Margin:** {info.get('operatingMargins', 'N/A')}%")

    # Dividend & Cash Flow Section
    st.header("Dividends & Cash Flow")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Dividend Rate:** ${info.get('dividendRate', 'N/A')}")
        st.write(f"**Dividend Yield:** {info.get('dividendYield', 'N/A')}%") #  * 100:.2f
    with col2:
        st.write(f"**Free Cash Flow:** ${info.get('freeCashflow', 'N/A'):,}")
        st.write(f"**Operating Cash Flow:** ${info.get('operatingCashflow', 'N/A'):,}")

    st.write(f"**Last Dividend Date:** {info.get('lastDividendDate', 'N/A')}")

    # Risk Section
    st.header("Risk & Governance")

    c0, c1, c2, c3, c4 = st.columns(5)
    with c0:
        st.write("Overall risk")
        st.pyplot(risk_gauge(info.get('overallRisk'))) if 'overallRisk' in info else st.write("N/A")
    with c1:
        st.write("Audit risk")
        st.pyplot(risk_gauge(info.get('auditRisk'))) if 'auditRisk' in info else st.write("N/A")
    with c2:
        st.write("Board risk")
        st.pyplot(risk_gauge(info.get('boardRisk'))) if 'boardRisk' in info else st.write("N/A")
    with c3:
        st.write("Compensation risk")
        st.pyplot(risk_gauge(info.get('compensationRisk'))) if 'compensationRisk' in info else st.write("N/A")
    with c4:
        st.write("Shareholder Rights risk")
        st.pyplot(risk_gauge(info.get('shareHolderRightsRisk'))) if 'shareHolderRightsRisk' in info else st.write("N/A")

    # Leadership Section
    st.header("Leadership Team")
    exp = True
    for officer in info.get("companyOfficers", []):
        with st.expander(f"{officer.get('title', 'N/A')}", expanded=exp):
            st.subheader(f"{officer.get('name', 'N/A')} - {officer.get('title', 'N/A')}")
            st.write(
                f"**Age:** {officer.get('age', 'N/A')} | **Total Pay (FY 2024):** ${officer.get('totalPay', 'N/A')}")
        exp = False

    # Stock Performance Section
    st.header("Stock Performance & Forecasts")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**52 Week High:** ${info.get('fiftyTwoWeekHigh', 'N/A')}")
        st.write(f"**52 Week Low:** ${info.get('fiftyTwoWeekLow', 'N/A')}")
    with col2:
        st.write(f"**Target Mean Price:** ${info.get('targetMeanPrice', 'N/A')}")
        st.write(
            f"**Recommendation:** {info.get('recommendationKey', 'N/A')} - Mean: {info.get('recommendationMean', 'N/A')}")
        st.write(f"**Analyst Opinions:** {info.get('numberOfAnalystOpinions', 'N/A')}")



def get_stock_analysis(stock_symbol: str):
    symbol = extract_symbol(stock_symbol)
    if symbol is None:
        st.error("Invalid stock symbol", icon=":material/error:")
    stock_details = get_stock_details(symbol)
    # write(get_stock_details(symbol))

    display_company_info(stock_details["info"], symbol)