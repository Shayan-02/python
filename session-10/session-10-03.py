def count_each_word(address_file):
    
    f = open(address_file, "r")
    
    txt_a=""
    for line in f:
        txt_a+=line

    txt_a = txt_a.replace("?"," ").replace("!"," ").replace("."," ").replace(","," ").lower()
    words = txt_a.split()
    
    counts_word_dict= dict()
        
    for word in words:
        if word in counts_word_dict:
            counts_word_dict[word] += 1
        else:
            counts_word_dict[word] = 1

    print( counts_word_dict)
    
count_each_word("./2.txt")