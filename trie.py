from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

class TrieNode:
	def __init__(self):
		self.count=[0]*26
		self.reference=[None]*26

class Trie :

    def __init__(self) :
        self.rootNode=TrieNode()
        # constructor for the Trie
        pass
    
    def insert(self, string) :
        node=self.rootNode
        string=string.lower()
        for i in range(len(string)-1):
            char=string[i]
            charCode=ord(char)-97
            if node.reference[charCode]==None:
                node.reference[charCode]=TrieNode()
            node=node.reference[charCode]
        node.count[ord(string[-1])-97]+=1
	
			
        # Insert function goes here
        pass

    
    def search(self, word) :
        node=self.rootNode
        word=word.lower()
        for i in range(len(word)-1):
            char=word[i]
            charCode=ord(char)-97
            if node.reference[charCode]==None:
                return False
            node=node.reference[charCode]
        if node.count[ord(word[-1])-97]>=1:
            return True
        else:
            return False
        # Search function goes here
        pass

        
    def startWith(self, prefix) :
        node=self.rootNode
        prefix=prefix.lower()
        for i in range(len(prefix)-1):
            char=prefix[i]
            charCode=ord(char)-97
            if node.reference[charCode]==None:
                return False
            node=node.reference[charCode]
        if node.count[ord(prefix[-1])-97]>=1 or node.reference[ord(prefix[-1])-97]!=None:
            return True
        else:
            return False
        # StartWith function goes here
        pass



# main
t = int(input().strip())
root = Trie()
for i in range(t) :

    q_str = stdin.readline().strip().split(" ")
    q = int(q_str[0].strip())
    str1 = q_str[1].strip()

    if(q == 1) :
        root.insert(str1)
    
    elif (q == 2) :
        if(root.search(str1)) :
            print("true") 

        else :
            print("false")
        
    else :
        if(root.startWith(str1)) :
            print("true")

        else :
            print("false")

