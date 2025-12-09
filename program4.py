#Create a program that asks the user to input a sentence, and display:
# 1 Count total words in the sentence.
# 2 Find the longest word in the sentence.
# 3 Display the sentence in uppercase.
# 4 Display the sentence in lowercase.
# 5 Display the sentence in Title Case (first letter of each word capitalized).
# 6 Display the sentence in reverse order.
# Student Name: Prashant Rijal
# Student Id: 397152
# Assignment: 1 
# Group: DAN/EXT 14

# Here, Def tells the python that we are defining a function called sentence_analysis, which act as container for all the logic.
def sentence_analysis():
    text = "" #here we kept the text empty to initalize the loop
    
    # here, we are using while loop which keeps running until user enters valid sentence
    while not text.strip(): # here, .strip checks the characters other than whitespaces
        text = input("Please enter a sentence: ") # here, the program pauses and waits for user inputs
        if not text.strip(): # here, input is checked immediately after user enters the sentence 
            print("Please enter a valid sentence.") # if input is invalid, this message is shown to user
            
    
    # This line splits the input text into a list.
    words = text.split() 
    
    total_words = len(words) # This line calculates the total number of words in the list   
    
    # This line finds the longest word in the list using the max function with key=len to compare word lengths.
    longest_word = max(words, key=len)

    
    print(f"Total words: {total_words}") # This line prints the total number of words in the sentence.
    print(f"Longest word: {longest_word} ({len(longest_word)} Letters)") # This line prints the longest word along with its length in letters.
    print(f"Uppercase: {text.upper()}") # This line prints the sentence in uppercase using the upper() method.
    print(f"Lowercase: {text.lower()}") # This line prints the sentence in lowercase using the lower() method.
    print(f"Title Case: {text.title()}") # This line prints the sentence in title case using the title() method.    
    print(f"Reversed:{text[::-1]}") # This line prints the sentence in reverse order using slicing with a step of -1.

# This line checks if you are running the script directly.
if __name__ == "__main__": 
        sentence_analysis() # this calls the above defined funtion 