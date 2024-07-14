'''def remove_duplicates(input_string):
    seen_chars = set()
    result_string = ""

    for char in input_string:
        if char not in seen_chars:
            seen_chars.add(char)
            result_string += char

    return result_string

# Example usage
input_str = input("Enter a string: ")
result = remove_duplicates(input_str)
print(f"String after removing duplicates: {result}")

'''
s=input()
s1=""
for i in s:
    if i not in s1:
        s1+=i
print(s1)