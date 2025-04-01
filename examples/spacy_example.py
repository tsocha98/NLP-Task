import spacy

# Załadowanie modelu językowego
nlp = spacy.load("pl_core_news_sm")

# Przetwarzanie tekstu
text = "Przetwarzanie języka naturalnego jest fascynującym tematem."
doc = nlp(text)

# Wyświetlanie tokenów i ich części mowy
for token in doc:
    print(token.text, token.pos_)
