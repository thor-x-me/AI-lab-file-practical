# run following commant in the terminal if NLTK is not already installed
# pip instll nltk

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download required NLTK data files
nltk.download('punkt')

# Function to perform stemming
def perform_stemming(sentence):
    stemmer = PorterStemmer()
    words = word_tokenize(sentence)
    stemmed_words = [stemmer.stem(word) for word in words]
    return ' '.join(stemmed_words)

# Input sentence
sentence = input("Enter a sentence: ")

# Perform stemming
stemmed_sentence = perform_stemming(sentence)

# Display the result
print("Original Sentence:", sentence)
print("Stemmed Sentence:", stemmed_sentence)
