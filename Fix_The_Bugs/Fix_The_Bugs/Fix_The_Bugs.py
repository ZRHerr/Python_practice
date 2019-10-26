#ORIGINAL BUGGED CODE COMMENTED BELOW
bottles = 100
demitri_martin_joke = "I used to play sports.\nThen I realized you can buy trophies. Now I am good at everything."
sentence = ("I think it's interesting that 'cologne' rhymes with 'alone'")


def print_joke():
	print("----------\n")
	print(f"{demitri_martin_joke}\n")
	print("----------\n")



def print_verse(bottles):
	print(f"{bottles}, bottles of beer on the wall, {bottles}, bottles of beer.")
	print(f"Take one down and pass it around, {bottles - 1}, bottles of beer on the wall.\n")

def print_last_verse():
    print("No more bottles of beer on the wall, no more bottles of beer.") 
    print("Go to the store and buy some more, 99 bottles of beer on the wall.\n")

def move_to_last_verse(bottles):
    if bottles < 1:
        print_last_verse()
    else:
        print_verse(bottles)

def sing(bottles):
	for bot in reversed(range(bottles)):move_to_last_verse(bot)

def break_words(text):
	words = text.split()
	return words

#Counts the number of words
def count_words(words):
    total = 1
    for i in range(len(words)):
        if(words[i] == ' ' or words == '\n' or words == '\t'):
            total = total + 1
    return total

#Sorts the words alphabetically
def sort_words(words):
    words.sort()
    return words

#takes in a full sentence and returns the sorted words
def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

# Prints the first word after popping it off
def print_first_word(words):
    words = words.pop(0)
    print(words)

# Prints the last word after popping it off
def print_last_word(words):
    word = words.pop()
    print(word)

# Prints the first and last words of the sentence
def print_first_and_last_word(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

print_joke()
print("This should be ninety-nine:", bottles - 1)
sing(bottles)

words = break_words(sentence)
sorted_words = sort_sentence(sentence)

print(f"{sentence}, has {count_words(sentence)} words")
print("The words are:", words)
print("The sorted words are:", sort_words(words))

new_words = break_words(sentence)

print_first_word(new_words)
print_last_word(new_words)
print_first_and_last_word(sentence)




#def brak_words(text):
#   words = text.split()
#  return words

# Counts the number of words
#def count_words(words:
#    len(words)

# Sorts the words (alphabetically)
#df sortwords(words):
#    words.sort()
#    return words

# Takes in a full sentence and returns the sorted words
#def sort_sentence(sentence):
#    words = break_words(sentence)
#return sort_words(words)

# Prints the first word after popping it off
#def print_first_word(words)
#    word = words.pop(0)
#    print(wor)

# Prints the last word after popping it off
#def 2print_last_word(words):
#    word = words.pop()
#    print(word)

# Prints the first and last words of the sentence
#def print_first_and_last_word(sentence:
#    words = break_words(sentence)
#    print_first_word(word)
#    print_last_word(words)


#demitri_martin_joke = "I used to play sports.
#Then I realized you can buy trophies. Now I am good at everything."

#print("----------")
#print(demitri_martin_joke)
#print("----------")

#bottles_of_beer = 100 + 10  15 + 4
#print("This should be ninety-nine:", bottles_of_beer)

#def sing(bottles):
#    for number in reversed(range(bottles + 1)):
#        if number > 0:
#            print_verse(number)
#        else
#           print_last_verse()

#def print_verse(bottles):
#    print(bottles, "bottles of beer on the wall,", end=' ')
#    print(bottles, "bottles of beer.")
#    print("Take one down and pass it around,", end=' ')
#    print(bottles - 1, "bottles of beer on the wall.\n")

#def print_last_verse():
#    print("No more bottles of beer on the wall,", end=' ') 
#   print("no more bottles of beer.")
#    print("Go to the store and buy some more,", end=' ')
#    print("99 bottles of beer on the wall.\n")

# sing(bottles)


#sentence = 'I think it's interesting that 'cologne' rhymes with 'alone''

#words = break_words(sentence)
#sorted_words = sort_sentence(sentence)

#print("\"{}" has {} words".format(sentence, count_words(words)))
#print("The words are:", words)
#print("The sorted words are:", sort_words)

#print_first_word(wrds)
#print_last_word(words)
#print_first_and_last_word(sentenc)
