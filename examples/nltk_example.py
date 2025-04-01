import nltk
from nltk.tokenize import word_tokenize

# Pobranie zasobów
nltk.download('punkt')

# Tokenizacja tekstu
text = "Witaj w świecie przetwarzania języka naturalnego!"
tokens = word_tokenize(text)

print(tokens)
