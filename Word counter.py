print("Welcome to the Word Counter Program!")
def count_words(text):
    """
    Counts the number of words in the given text.
    Args:
    - text (str): The input text to analyze.
    
    Returns:
    - int: The number of words in the input text.
    """
    # Split the text into words using whitespace as a delimiter and filter out empty strings
    words = text.split()
    return len(words)

def main():
    """
    Main function to run the Word Counter program.
    """
    #print("Welcome to the Word Counter Program!")
    while True:   
        text =input("Enter a sentence or paragraph (or 'q' to quit): ")
        
        if text.lower()== 'q':
            break
        else:
            word_count=count_words(text)
            if not text:
                print("Error: Input cannot be empty. Please try again.")
            print(f"\n The number of words provided in the text is :{word_count}")

if __name__ == "__main__":
    # Run the program
    main()
