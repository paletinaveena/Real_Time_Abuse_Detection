# abuse_detection.py
import re
from transformers import pipeline

# Rule-based patterns
RULES = {
    "abusive": r"\b(fuck|shit|asshole|bitch|damn)\b",
    "spam": r"(!{3,}|\b(?!http)\w+\.\w{2,3}\b)",
    "repetitive": r"(\b\w+\b)\s+\1{2,}"
}

def run_rules(text):
    for rule_name, pattern in RULES.items():
        if re.search(pattern, text, re.IGNORECASE):
            return rule_name
    return None

# ML Classifier
class AbuseClassifier:
    def __init__(self):
        self.classifier = pipeline(
            'text-classification',
            model='distilbert-base-uncased-finetuned-sst-2-english'
        )

    def is_abusive(self, text):
        result = self.classifier(text)[0]
        return result['label'] == 'NEGATIVE' and result['score'] > 0.9
