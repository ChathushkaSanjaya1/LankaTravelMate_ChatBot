# nlp_engine/nlp_tools.py

import string

def clean_text(text):
    """
    Basic NLP cleaning: Lowercase and remove punctuation.
    """
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()
