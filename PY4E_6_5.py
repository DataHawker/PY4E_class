#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
#Convert the extracted value to a floating point number and print it out.

# import re

# text = "X-DSPAM-Confidence:    0.8475"

# this = float(re.findall("\d*\.*\d+", text)[0])
# print(this)


# This was the first go
# text = "X-DSPAM-Confidence:    0.8475"
# start = text.find("0")
# start_float = float(text[start : ])
# print(start_float)

text = "X-DSPAM-Confidence:    0.8475"

ipos = text.find(':')+1
value = float(text[ipos : ].strip())
print(value)
