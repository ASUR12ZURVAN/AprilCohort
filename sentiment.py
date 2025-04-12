import re
import json
from statistics import mean
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from huggingface_hub import login

# ==== Optional: Hugging Face token (better set via env variable in prod) ====
HF_TOKEN = "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"  # Replace with your own or set as env var
login(token=HF_TOKEN)

# ==== Load pretrained sentiment model ====
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=HF_TOKEN)
model = AutoModelForSequenceClassification.from_pretrained(model_name, use_auth_token=HF_TOKEN)
sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# ==== Read transcript ====
# Option 1: Direct string input
transcript_text = """
Hi, I’m having trouble with my bill.
Okay, let me check that for you.
It says I was overcharged.
I understand, I’ll fix it right away.
"""

# Option 2: Load from JSON
# with open("transcript.json", "r") as f:
#     data = json.load(f)
#     transcript_text = data["transcript"]

# ==== Split into individual turns ====
turns = re.split(r'(?<=[.?!])\s+', transcript_text.strip())

# Alternate turns assuming caller speaks first
caller_turns = turns[::2]   # 0, 2, 4,...
agent_turns = turns[1::2]   # 1, 3, 5,...

# ==== Analyze sentiment of caller turns ====
print("\n🔍 Sentiment Analysis of Caller Statements:\n")
scores = []

for i, turn in enumerate(caller_turns):
    result = sentiment_pipeline(turn)[0]
    sentiment = result["label"]
    score = result["score"]
    print(f"Caller Turn {i+1}: {turn}")
    print(f"  ➤ Sentiment: {sentiment} (score: {score:.2f})\n")

    # Convert sentiment into signed score for average
    signed_score = score if sentiment == "POSITIVE" else -score
    scores.append(signed_score)

# ==== Calculate average sentiment ====
avg_sentiment_score = mean(scores)
print(f"📊 Average Caller Sentiment Score: {avg_sentiment_score:.2f}")
