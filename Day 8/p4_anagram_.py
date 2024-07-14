'''def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Example usage:
word1 = "Listen"
word2 = "Silent"

if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
'''
d={}
for i in range(2):
    k,v=map(str,input().split())
    d[k]=v
print(d)
l=list(d.values())
if len([l[0]]==len[l[1]]):
    if sorted(list(l[0]))==sorted(list(l[1])):
        print(True)
    else:
        print(False)
else:
    print(False)