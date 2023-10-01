def count_each_word(address_file):
    
    f = open(address_file, "r")
    
    txt_a=""
    for line in f:
        txt_a+=line

    txt_a = txt_a.replace("?"," ").replace("!"," ").replace("."," ").replace(","," ").lower()

    words=txt_a.split()
    
    repeated_word=""
    
    for word in words:
            if word!= repeated_word:
                repeated_word=word
                count=0
                for x in words:
                    if x == word:
                        count += 1
                print (f"The word '{word}' occurs {count} times in the file.")
              
        

count_each_word("./1.txt")
