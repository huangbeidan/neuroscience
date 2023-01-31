#This program will read a PubMed format abstract file and count the number of words and characters in it.
#Written by Holly Jing, November 15, 2022

def count_chars(text):      # use a function and a loop to count characters
    result = 0
    for char in text:
        result = result + 1
    return result

def count_words(text):      # use a function and a loop to count words based on spaces
    count = 0
    for space in text:
        if space == " ":
            count = count + 1
    return count

line_number = 0             #initialize total counts
total_chars = 0
total_words = 0

file = open('pubmed_test.txt')   # open a test input file in read-only mode
for line in file:
    line = line.strip()
    line_number = line_number + 1
    char_number = count_chars(line)   #call the functions defined above
    word_number = count_words(line)
    total_chars = total_chars + char_number
    total_words = total_words + word_number
    print (line_number, char_number, word_number, line)

print ("=================================")
print ("The number of lines is:", line_number)
print ("The number of words is:", total_words)
print ("The number of characters is:", total_chars)
