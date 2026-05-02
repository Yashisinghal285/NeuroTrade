# 🧠 NeuroTrade

NeuroTrade is a smart stock news alert system that fetches real-time news related to stocks and financial markets using RSS feeds. It filters important news based on keywords and sends instant alerts directly to users through a Telegram bot, helping them stay informed and reduce potential financial losses.

## 🚀 Features
- Real-time stock market news fetching from multiple sources  
- Keyword-based filtering (Nifty, Sensex, IPO, earnings, etc.)  
- Instant Telegram bot notifications  
- Covers both Indian 🇮🇳 and Global 🌍 market news  
- Simple and lightweight Python-based system  

## 🛠️ Tech Stack
- Python  
- RSS Feeds (MoneyControl, Economic Times, CNBC, etc.)  
- Telegram Bot API  
- Libraries: `feedparser`, `requests`  

## 📌 How It Works
1. Fetches news from multiple RSS feed sources  
2. Combines all articles into a single dataset  
3. Filters news using predefined stock-related keywords  
4. Sends top relevant news directly to Telegram  

## ⚙️ Installation

### 1. Clone the repository
git clone https://github.com/Yashisinghal285/NeuroTrade.git  
cd NeuroTrade  

### 2. Install dependencies
pip install feedparser requests  

### 3. Configure the project
- Open `config.py`  
- Add your Telegram Bot Token and Chat ID  
- Make sure your Telegram bot is started (click "Start" in Telegram)

### 4. Run the project
python main.py  

## 📦 Requirements
- Python 3.x  
- Internet connection  
- Telegram account  

## 📢 Example Output
📢 Stock Alert: Market falls after global recession fears  
<News article link>
## 🔮 Future Improvements
- AI-based news sentiment analysis  
- Stock-specific alerts (user input based)  
- Web dashboard for tracking alerts  
- Deployment for 24/7 automation  

## ⚠️ **Disclaimer**
**This project is for educational purposes only. It does not provide financial advice.**
