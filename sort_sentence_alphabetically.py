def sort_sentence_alphabetically(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Sort the words alphabetically
    sorted_words = sorted(words, key=str.lower)
    # Join the sorted words back into a sentence
    sorted_sentence = ' '.join(sorted_words)
    return sorted_sentence


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    sorted_sentence = sort_sentence_alphabetically(sentence)
    print("Sorted sentence:", sorted_sentence)
