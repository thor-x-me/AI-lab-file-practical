# run following commant in the terminal if NLTK is not already installed
# pip instll nltk

# create input.txt file in the same directory

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure you have downloaded the necessary resources
nltk.download('stopwords')
nltk.download('punkt')

# Function to remove stop words
def remove_stop_words(file_path):
    try:
        # Open and read the file
        with open(file_path, 'r') as file:
            text = file.read()

        # Tokenize the text into words
        words = word_tokenize(text)

        # Load the list of stop words
        stop_words = set(stopwords.words('english'))

        # Filter out stop words
        filtered_words = [word for word in words if word.lower() not in stop_words]

        # Return the filtered passage
        return ' '.join(filtered_words)

    except FileNotFoundError:
        return "File not found. Please check the file path."

# Example usage
file_path = 'input.txt'  # Replace with your file's path
filtered_text = remove_stop_words(file_path)
print("Filtered Text:\n", filtered_text)
