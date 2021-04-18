import string # import string.punctuation so that it can be iterated and removed from the input

while 1:
    sentence_input = input('Enter sentence: ')
    for i in string.punctuation:
        sentence_input = sentence_input.replace(i, "") # remove all punctuations
        sentence_input = sentence_input.lower() # converts all words to lowercase
    break

def frequency(clean):
    clean = clean.split() # split "cleaned" string into a list of words
    list1 = [] # create an empty list to store the split words alphabetically
    for n in clean:
        if n not in list1:
            list1.append(n)
            list1.sort() # sort the list in an alphabetical order
    for m in range(0, len(list1)):
        # printing each unique string + semicolon + the count of each unique string using list1.
        print(list1[m], ":", clean.count(list1[m]))
    return

frequency(sentence_input)
