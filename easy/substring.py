#Given two strings, check whether the first string is a substring of the 
# second string.  What is the runtime of your algorithm? 


def substring(str1, str2):
  is_substring = False  
  for i in range(len(str2)):
    is_match = True 
    for j in range(len(str1)):
       if str2[i + j] != str1[j]:
         is_match = False
    if is_match:
      return True
  return False


# with single loop

def str_search(str1, str2):
    for i in range(len(str2) - len(str1) + 1):
        if str1 == str2[i:i+len(str1)]:
            return True
    else:
        return False

