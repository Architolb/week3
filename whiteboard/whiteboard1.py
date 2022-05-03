# Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters 
# and empty space characters (" "), return the length of the last word. Meaning, 
# the word that appears far most to the right if we loop through the words.
# ex = "Hello World"
# Example Output: 5






# Given a sentence - "Benedict Cumberbatch cannot say the word penguin correctly."
# Once a letter has occurred in the sentence, replace all of its following occurrences with '_', then return the sentence
# bonus challenge: count uppercase and lowercase letters as the same


# sentence = "Benedict Cumberbatch cannot say the word penguin correctly."

def add_space(sentence):
    letters = []
    sentence = "Benedict Cumberbatch cannot say the word penguin correctly."
    
    for i in sentence:
        if i not in letters:
            letters.append(i)
            sentence.replace("", "_")
        else:
            print(sentence.lower())


from dataclasses import replace
sentence = "Benedict Cumberbatch cannot say the word penguin correctly."
def whiteboard(sen):
    seen_ls=[]
    for i in sen:
        if i.lower() not in str(seen_ls).lower():
            seen_ls.append(i)
        else:
            seen_ls.append('_')
    return ("").join(seen_ls)
print(whiteboard(sentence))