# Trading Bot (Binance Futures Testnet - Mock Version)

## 📌 Overview

This project is a CLI-based Python application that simulates placing trading orders similar to Binance Futures Testnet (USDT-M).

It supports:

* MARKET orders
* LIMIT orders
* BUY and SELL operations
* Input validation
* Logging of requests and responses
* Error handling

---

## ⚠️ Note

Due to access limitations with Binance Futures Testnet API (KYC/verification restrictions), a mock trading layer has been implemented.

The application is designed with a modular architecture, allowing easy replacement of the mock client with real Binance API integration using python-binance or REST APIs.

---

## ⚙️ Setup Instructions

### 1. Clone or Download the Project

```bash
git clone <your-repo-link>
cd trading_bot
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### On Windows:

```bash
venv\Scripts\activate
```

#### On Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 🔹 MARKET Order Example

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### 🔹 LIMIT Order Example

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## 📌 Sample Outputs

### MARKET Order Output

```
📌 Order Summary
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001
Price: None

✅ Order Placed Successfully!
Order ID: 157612
Status: FILLED
Executed Qty: 0.001
Avg Price: market_price
```

---

### LIMIT Order Output

```
📌 Order Summary
Symbol: BTCUSDT
Side: SELL
Type: LIMIT
Quantity: 0.001
Price: 60000.0

✅ Order Placed Successfully!
Order ID: 532507
Status: NEW
Executed Qty: 0
Avg Price: 60000.0
```

---

## 📂 Logging

All logs are stored in:

```
bot.log
```

The log file contains:

* Order requests
* Responses
* Error messages (if any)

Example:

```
Mock Request: BTCUSDT BUY MARKET 0.001 None
Mock Response: {...}

Mock Request: BTCUSDT SELL LIMIT 0.001 60000
Mock Response: {...}
```

---

## 🧠 Assumptions

* MARKET orders execute instantly (FILLED)
* LIMIT orders are placed but not executed immediately (NEW)
* Binance API interactions are simulated due to testnet access restrictions

---

## 🏗️ Project Structure

```
trading_bot/
│── main.py        # CLI interface
│── client.py      # Order execution (mock implementation)
│── utils.py       # Input validation
│── logger.py      # Logging configuration
│── requirements.txt
│── README.md
│── bot.log
```

---

## 🚀 Future Improvements

* Integrate real Binance Futures Testnet API
* Add retry and failure handling for API calls
* Implement async order execution
* Add trading strategies and automation

---

## 💡 Conclusion

This project demonstrates:

* Clean and modular code structure
* CLI-based user interaction
* Proper logging and error handling
* Scalable design for real API integration

---
