# Strings of class str are created with quotes
quote_1 = 'single quoted'
quote_2 = "double quoted"
print('quote_1 =', quote_1)
print('quote_2 =', quote_2)

#Use opposing quotes to include them in string or use backslash
quote_3 = '"Hello"'
quote_4 = "It's Mine!"
quote_5 = 'It\'s Mine!'
print('quote_3 =', quote_3)
print('quote_4 =', quote_4)
print('quote_5 =', quote_5)

new_line = 'line1\nline2\nline3\n' #New Line
print(new_line)
tab = 'tab1\ttab2\ttab3' #Tab Space
print(tab)
backslash = 'backslash: \\'
print(backslash)

#raw strings, use r infront of a string
raw_new_line = r'line1\nline2\nline3\n'
print(raw_new_line)
raw_tab = r'tab1\ttab2\ttab3'
print(raw_tab)
raw_backslash = r'backslash: \\'
print(raw_backslash)

# sequence objects can use several operators and functions:
text = 'double'
print('text =',text)
print(text + text)
print('_' * 40)
print('len(text) =', len(text))
print('min(text) =', min(text))
print('max(text) =', max(text))
print('text not in quote_1', text not in quote_1)
print('text in quote_2', text in quote_2)

# string object methods:
text = 'She said, "Hello!"'
print('text =',text)
print('text.count("e") =', text.count('e'))
print('text.index("e") =', text.index('e'))
print('text.index("e", 3, 18) =', text.index('e', 3, 18))
print('text.find("X") =', text.find('X'))
print('text.find("e") =', text.find('e'))
print('text.startswith("She") =', text.startswith('She'))
print('text.endswith("!\\"") =', text.endswith('!"'))
print('text.upper() =', text.upper())
print('text.lower() =', text.lower())
abc = 'a,b,c'
print('abc.split(",") =',abc.split(","))
print('",".join(["a", "b", "c"]) =', ",".join(["a", "b", "c"]))
text = 'Hello'
print('text =',text)
print('text.isalpha() =', text.isalpha())
print('text.isdigit() =', text.isdigit())

# Replace a char with another char
text = 'She said, "Hello!"'
print('text =',text)
print("text.replace(',','')) =", text.replace(',',''))





