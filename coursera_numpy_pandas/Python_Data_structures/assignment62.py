text = "X-DSPAM-Confidence:    0.8475"

ind = text.find(' ')
#print(ind)
number = text[ind+1:len(text)]
print(float(number.strip()))  # Extract substring after the first space