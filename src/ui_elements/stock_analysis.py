from streamlit import write, error
from src.library.apis.yahoo_client import get_stock_details
import re


def extract_symbol(stock_string):

    match = re.search(r"\[(.*?)\]", stock_string)
    return match.group(1) if match else None


def get_stock_analysis(stock_symbol: str):
    symbol = extract_symbol(stock_symbol)
    if symbol is None:
        error("Invalid stock symbol", icon=":material/error:")
    write(get_stock_details(symbol))