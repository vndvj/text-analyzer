#basic text analyzer
text = input ("Enter a text: ")
text = text.lower()
punctuation = ".,!?;:()"
for symbol in punctuation:
    text = text.replace(symbol, "")
words = text.split()
word_count = len(words)
unique_words = set(words)
unique_count = len(unique_words)
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
most_common = max(frequency, key=frequency.get)

print("\nTEXT ANALYSIS")
print ("-----------")
print ("Total words:", word_count)
print ("Unique words:", unique_count)
print ("Most common word:", most_common)
print ("Frequency:", frequency[most_common])
 
  