#!/usr/bin/env python

userdna = input ("Provide a DNA sequence: ")
# Calculate Total Sequence Length
print ("Total Sequence Length:")
print (len(userdna))
#Number of As
print ("Total number of As:")
print (userdna.lower().count('a'))
# Calculate number of Cs
print ("Total number of Cs:")
print (userdna.lower().count('c'))
#Calculate number of Gs
print ("Total number of Gs:")
print (userdna.lower().count('g'))
#Calculate number of Ts
print ("Total number of Ts:")
print (userdna.lower().count('t'))

# DB: Good! My only suggestion is that you can make it more general by
#     accepting both upper- and lowercase sequences. You can do this
#     by adding .lower() to userdna (see above).