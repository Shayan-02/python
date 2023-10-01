f = open("./1.txt", "r")
text_a = f.readline()

new_text = text_a.replace("?"," ").replace("!"," ").replace("."," ").replace(","," ").lower()

def count_same_word(sentence, word):
    words = sentence.split()
    count = 0
    for x in words:
        if x == word:
            count += 1
    return count

word_to_count = "and"

occurrences = count_same_word(new_text, word_to_count)
print(f"The word '{word_to_count}' occurs {occurrences} times in the sentence.")