file = open("input.txt",'r')

text = file.read()

char_count = len(text)
word_count = len(text.split())

file.seek(0)
line_count = len(file.readlines())

file.close()

output = open("output.txt",'w')
output.write("char count" + str(char_count) + "\n")
output.write("word count " + str(word_count)+ "\n")
output.write("line count"+ str(line_count)+ "\n")

output.close()