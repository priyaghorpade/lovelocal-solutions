input_str = input("Enter a string: ") 
words = input_str.split() 
if words: 
  last_word_length = len(words[-1]) 
  print(last_word_length) 
else: 
  print("No words in the input string.")
