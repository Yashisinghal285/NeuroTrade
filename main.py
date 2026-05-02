import feedparser
import requests
from config import TELEGRAM_TOKEN, CHAT_ID, RSS_URLS, KEYWORDS


def fetch_all_news():
    all_articles = []

    for url in RSS_URLS:
        feed = feedparser.parse(url)
        print(f"🌐 Fetching from: {url} → {len(feed.entries)}")

        all_articles.extend(feed.entries)

    return all_articles


def filter_news(articles):
    filtered = []

    for article in articles:
        title = article.get("title", "")
        summary = article.get("summary", "")
        text = (title + summary).lower()

        for keyword in KEYWORDS:
            if keyword.lower() in text:
                filtered.append(article)
                break

    return filtered


def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=data)
        print("📩 Telegram:", response.status_code)
    except Exception as e:
        print("❌ Telegram error:", e)


def main():
    print("🚀 Bot started...")

    # ✅ Test message
    send_to_telegram("✅ Bot is working!")

    # 🔥 FIX HERE
    articles = fetch_all_news()

    print("📰 Total articles:", len(articles))

    if len(articles) == 0:
        print("❌ No articles fetched")
        return

    filtered = filter_news(articles)
    print("🎯 Filtered articles:", len(filtered))

    if len(filtered) == 0:
        print("⚠️ No filtered news, sending latest instead...")
        filtered = articles

    for article in filtered[:5]:
        title = article.get("title", "No title")
        link = article.get("link", "")

        msg = f"{title}\n{link}"
        send_to_telegram(msg)


if __name__ == "__main__":
    main()