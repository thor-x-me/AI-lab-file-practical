def remove_punctuations(input_string):
    punctuations = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ''.join(char for char in input_string if char not in punctuations)
    return result


# Usage of remove_punctuations
string = "Hello, World! This is a test-string."
print("Original string:", string)
print("String without punctuations:", remove_punctuations(string))
