import json

STOCKS_PATH = 'src/database/stocks.json'

def write_stocks_to_json():
    """
    Writes a static list of stocks to a JSON file.

    Args:
        file_path (str): The path to the JSON file to write the stocks.
    """
    # Static list of stocks
    stock_list = {
        "AAPL": "Apple Inc.",
        "MSFT": "Microsoft Corporation",
        "GOOGL": "Alphabet Inc. (Google)",
        "AMZN": "Amazon.com, Inc.",
        "TSLA": "Tesla, Inc.",
        "META": "Meta Platforms, Inc. (Facebook)",
        "NVDA": "NVIDIA Corporation",
        "BRK-A": "Berkshire Hathaway Inc. (Class A)",
        "JNJ": "Johnson & Johnson",
        "V": "Visa Inc."
    }

    # Write the dictionary to a JSON file
    with open(STOCKS_PATH, "w") as f:
        json.dump(stock_list, f, indent=4)
    print(f"Stocks have been written to {STOCKS_PATH}")


def get_stocks_list():
    """
    Reads stocks from a JSON file and returns a list of strings in the format "Name [Symbol]".

    Args:

    Returns:
        list: A list of strings formatted as "Name [Symbol]".
    """
    # Read the JSON file
    with open(STOCKS_PATH, "r") as f:
        stock_list = json.load(f)

    # Convert the dictionary to a list of strings
    return [f"{name} [{symbol}]" for symbol, name in stock_list.items()]
