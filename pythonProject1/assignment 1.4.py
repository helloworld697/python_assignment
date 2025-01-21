def my_split(sentence, separator):
    result = []
    current_word = ""
    for char in sentence:
        if char == separator:
            result.append(current_word)
            current_word = ""
        else:
            current_word += char
    if current_word:
        result.append(current_word)
    return result

def my_join(lst, separator):
    result = ""
    for i in range(len(lst)):
        result += lst[i]
        if i < len(lst) - 1:
            result += separator
    return result

# Example usage:
sentence = input("Please enter sentence: ")
split_list = my_split(sentence, " ")
joined_string = my_join(split_list, ",")

print(joined_string)
for item in split_list:
    print(item)
