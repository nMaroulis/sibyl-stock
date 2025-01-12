# Sibyl Stock

### 🚧 **Work in Progress** 🚧  
<span style="color:red">This project is in pre-alpha stage and under active development. Features may change frequently, and bugs are expected.</span>

Sibyl-stock is a powerful Streamlit app that provides in-depth stock analysis and investment recommendations using machine learning and advanced algorithms. Whether you're a seasoned investor or just starting out, Sibyl-stock helps you make informed decisions by offering a comprehensive view of a company's performance and potential.

---

## 🚀 Features

- **Company Overview**:  
  Get detailed information about any stock, including company profile, key metrics, and financials.

- **Analytics & Visualizations**:  
  Explore various analytics such as price trends, volume, moving averages, and more. Gain insights with interactive charts and visualizations.

- **Investment Insights**:  
  Leverage machine learning models and advanced algorithms to determine if a stock is a good investment.

- **Stock Selector**:  
  Easily search and select from a wide range of stocks to analyze.

- **Customizable Analysis**:  
  Tailor your analysis with custom parameters for deeper insights.

---

## 🛠️ Technologies Used

- **Frontend**:  
  Built using [Streamlit](https://streamlit.io/), providing an intuitive and user-friendly interface.

- **Backend**:  
  Powered by Python with libraries such as:
  - [yfinance](https://pypi.org/project/yfinance/) for stock data retrieval.
  - [pandas](https://pandas.pydata.org/) and [numpy](https://numpy.org/) for data manipulation.
  - [tensorflow](https://github.com/tensorflow/tensorflow), [scikit-learn](https://scikit-learn.org/) and other ML libraries for predictive models.

- **Visualization**:  
  Interactive and dynamic plots using [Plotly](https://plotly.com/) and [matplotlib](https://matplotlib.org/).
---

## 🔧 Setup and Installation

**Clone the repository**:
   ```bash
   git clone https://github.com/your-username/sibyl-stock.git
   cd sibyl-stock
   ```

1. **Using python locally** 

Install dependencies:
Ensure you have Python 3.10 or above installed. Then, run:
   ```bash
   pip install -r requirements.txt
   streamlit run index.py  # launch the server
   ```
Open your browser and navigate to http://localhost:8501.

2. **Using Docker**

Build the Docker image:
   ```bash
   docker build -t sibyl_stock .
   docker run -p 8501:8501 sibyl_stock
   ```

Again access the app through your browser and navigate to http://localhost:8501.

---

### 📊 Machine Learning Models

The app includes various ML models to predict stock performance, such as:

> Regression models for price prediction.

> Classification models for buy/sell/hold recommendations.

> Sentiment analysis based on news and social media.
---

### 🧪 Future Improvements

Incorporate advanced sentiment analysis using large language models (LLMs).
Provide portfolio optimization features.
---

### 🤝 Contributing

We welcome contributions!

Fork the repository.
Create a feature branch: git checkout -b feature-name.
Commit your changes: git commit -m 'Add some feature'.
Push to the branch: git push origin feature-name.
Open a pull request.
---

###  📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

### 🌟 Acknowledgements

Streamlit for the interactive web app framework.
yfinance for financial data APIs.
tensorflow and scikit-learn for the ML capabilities.
