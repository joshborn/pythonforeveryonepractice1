text = "X-DSPAM-Conidence:  0.8475"

beg = text.find('0')
end = text.find('5')

number = text[beg:end+1]
n = float(number)

print(n)