#intro to filter
# names = ['austin', 'penny', 'anthony', 'angel', 'billy']
# a_names = list(filter(lambda n: n[0] == 'a', names))
# print(a_names)


# filter inactive user of twitter
# users = [
#     {'username': 'James', 'tweets': ['I love basketball']},
#     {'username': 'Mathew', 'tweets': ['I love to sing rap']},
#     {'username': 'Derik', 'tweets': []},
#     {'username': 'Anthony', 'tweets': []},
#     {'username': 'Tony', 'tweets': ['Going to build my house']}
# ]
# #below is the 1st way to define.
# # inactive_user = list(filter(lambda u: len(u['tweets'])==0, users))   #tweet ka jo value hai uska length zero hai
# #below is the second way to define, as we know empty list is by default a false, here not of false is true.
# inactive_user = list(filter(lambda u: not u['tweets'], users))        
# print(inactive_user)


def count_letters(text):
  result = {}
  count = 1
  # Go through each letter in the text
  for letter in text.lower():
    if letter.isalpha() == True :
    # Check if the letter needs to be counted or not
      if letter in result:
        result[letter] +=1
      else:
        result[letter] =1
    
    # Add or increment the value in the dictionary
    
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

