# Word Counter

fname=input("Enter file name:")
fname=open(fname, "r")
data=fname.read()
def count_words(data):
    words=data.split()
    num_words=len(words)
    return num_words
num_words=count_words(data)
def count_lines(data):
    lines=data.split("\n")
    num_liness=len(lines)
    return num_liness
def count_char(data):
    num_char=len(data)- data.count('\n')
    return num_char
num_words=count_words(data)
num_lines=count_lines(data)
num_char=count_char(data)
print("The number of words:",num_words)
print("The number of lines:",num_lines)
print("The number of characters:",num_char)