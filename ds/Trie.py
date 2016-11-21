import sys
def make_trie(word,trie):
    """
    Make a trie by given words.
    """
    temp_trie = trie
    for letter in word:
        temp_trie = temp_trie.setdefault(letter,{"count":0})
        temp_trie["count"] +=1
    return trie

def in_trie(trie, word):
    """
    Count if word in trie.
    """
    min_count=100001
    temp_trie = trie
    for letter in word:
        if letter not in temp_trie:
            return 0
        temp_trie = temp_trie[letter]
        if min_count > temp_trie["count"]:
            min_count=temp_trie["count"]
    return min_count

n = int(raw_input().strip())
trie={}
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if (op == "add"):
        make_trie(contact,trie)
    elif(op == "find") :
        print in_trie(trie, contact)