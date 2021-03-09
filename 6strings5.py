text = "X-DSPAM-Confidence:    0.8475"

pos0 = text.find('0')
num = float(text[pos0:])
print(num)
