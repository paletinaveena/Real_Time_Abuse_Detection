# 🛡️ Real-Time Abuse Detection on Twitter

A real-time moderation system for detecting and flagging abusive or harmful content on Twitter using both rule-based (regex) and machine learning (BERT-based NLP) techniques. This project also includes a Streamlit dashboard to visualize and manage flagged tweets.

## 🚀 Features

- 🔎 Real-time tweet monitoring using Twitter’s API (via Tweepy)
- 🧠 Hybrid abuse detection:
  - Rule-based using Regex
  - Machine learning using fine-tuned BERT
- 🗃️ SQLite database to store and update tweet data
- 📊 Streamlit dashboard for interactive moderation
- 🕒 Scheduled background scanning every 5 minutes

## 🧰 Tech Stack

- Python
- Tweepy (Twitter API)
- Regex
- BERT (HuggingFace Transformers)
- SQLite
- Streamlit
- schedule (job scheduling)

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/paletinaveena/Real_Time_Abuse_Detection.git
cd real_time_abuse_detection
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API keys
Update your Twitter API credentials in app/config.py
```python
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"
```

### 5. Run the moderation system
```python
python run.py
```

### 6. Launch the Streamlit dashboard
```python
streamlit run dashboard/dashboard.py
```

## 📬 Output
Tweets flagged as abusive are stored in a local SQLite DB.

Streamlit dashboard allows filtering, reviewing, and moderation actions.

## 📌 Notes
You can switch between rule-based and ML-based detection in abuse_detection.py.

For real-time stream filtering, extend streaming.py.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
