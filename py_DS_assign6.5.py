text = "X-DSPAM-Confidence:    0.8475";
x=text.find('0')
print(float(text[x:x+6]))
