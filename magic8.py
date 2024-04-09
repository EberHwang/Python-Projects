#!/usr/bin/env python3

import random
random.randint(1,10)
random_number = random.randint(1,10)
print(random_number)

name = "Eber"
question = "Will I get a promotion this year?"
answer = ""

if random_number == 1:
  answer = "Yes - Deinitely"

elif random_number == 2:
  answer = "Hell Yea"

elif random_number == 3:
  answer = "Yup"

elif random_number == 4:
  answer = "No But, Actually Yes"

elif random_number == 5:
  answer = "F*** Yea"

elif random_number == 6:
  answer = "Indeed"

elif random_number == 7:
  answer = "Of Course"

elif random_number == 8:
  answer = "Totally"
  
elif random_number == 9:
  answer = "Si"
#This will give an error if the answer is not within 1-9 range  
else:
  answer = "Error"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)
