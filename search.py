import sqlite3


def tokenize(text): 
    bag_of_words = [] 
    for word in text.split(): 
        clean_word = word.strip("!\"#\\$%&'()*+,-./:;<=>?@[]^_`{|}~").lower()
        if clean_word: 
            bag_of_words.append(clean_word) 
    return bag_of_words


inv_index = {}
def index(word, id): 
    
    if word not in inv_index:
        inv_index[word] = {id : 0}
    
    if id not in inv_index[word]: 
        inv_index[word][id] = 1
    else: 
        count = inv_index[word][id] + 1 
        inv_index[word][id] = count 

def indexing(tokenized_text, id): 
    for word in tokenized_text:
        index(word, id)


def search(query): 
    tokens = tokenize(query)
    score_record = {}
    for token in tokens: 
        
        if token not in inv_index: 
            continue 

        word_dict = inv_index[token] 
        for id in word_dict: 
            if id not in score_record: 
                score_record[id] = word_dict[id]
            else: 
                score_record[id] += word_dict[id] 

    score_record = {k: v for k, v in sorted(score_record.items(), key=lambda item: item[1])}
    return score_record










def main(): 
    con = sqlite3.connect("webpages.db")
    cur = con.cursor()

    texts = cur.execute(" SELECT id, text FROM webpages").fetchall()
    con.close()
    
    for id, text in texts: 
        print(id)
        print(text)
        print(tokenize(text))
        indexing(tokenize(text), id)
        print(inv_index)

    print(search("war in iran"))



    



if __name__ == "__main__": 
    main()
