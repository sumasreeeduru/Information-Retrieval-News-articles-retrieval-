import glob
import string
from collections import defaultdict
from stop_words import get_stop_words
import math
import collections

stop_words = get_stop_words('english')
   
class Trie():
    def __init__(self):
        self.child=defaultdict()
        self.end=False
        self.address=None
   
   

    def insert_word(self,key,docid):
        root=self
       
        for i in range(len(key)):
            if ord(key[i])-ord('a') >=0 and ord(key[i])-ord('a') <26:
                index=ord(key[i])-ord('a')
           
                if index not in root.child:
                    root.child[index]=Trie()
                root=root.child[index]
            else:
                return
       
        root.end = True
        avl=avltree()
        avlroot=None
        avlroot=avl.insertnode(None,docid)
        root.address = avlroot
       
    def insert2(self,key,avlroot):
        root=self
        for i in range(len(key)):
             if ord(key[i])-ord('a')>=0 and ord(key[i])-ord('a') <26:
               
                index=ord(key[i])-ord('a')
           
           
                root=root.child[index]
       
        if root!=None and root.address:
            root.address=avlroot
       
    def search_word(self, key):
        root = self
        for i in range(len(key)):
            if ord(key[i])-ord('a') >=0 and ord(key[i])-ord('a') <26:
                index=ord(key[i])-ord('a')
           
                root = root.child.get(index)
                if root is None:
                    return False
            else:
                return
       
        return root.end
    def search_address(self, key):
        root = self
        for i in range(len(key)):
            if ord(key[i])-ord('a') >=0 and ord(key[i])-ord('a')<26:
                index=ord(key[i])-ord('a')
           
                root=root.child.get(index)
                if root is None:
                    return None
            else:
                return
           
        if root != None and root.address :
            return root.address
class treenode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.count=1
class avltree(object):
 
   
    def insertnode(self, root, key):
       
       
        if not root:
            return treenode(key)
        elif key < root.val:
            root.left = self.insertnode(root.left, key)
        elif key>root.val:
            root.right = self.insertnode(root.right, key)
        elif key==root.val:
            root.count=root.count+1
           
        root.height = 1 + max(self.calculate_height(root.left),self.calculate_height(root.right))
 
        balancefactor = self.getbfactor(root)
 
        if balancefactor > 1 and key < root.left.val:
            return self.rightrotate(root)
 
       
        if balancefactor < -1 and key > root.right.val:
            return self.leftrotate(root)
 
       
        if balancefactor > 1 and key > root.left.val:
            root.left = self.leftrotate(root.left)
            return self.rightrotate(root)
 
       
        if balancefactor < -1 and key < root.right.val:
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)
 
        return root
 
    def calculate_height(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getbfactor(self, root):
        if not root:
            return 0
 
        return self.calculate_height(root.left) - self.calculate_height(root.right)
    def leftrotate(self, z):
        y = z.right
        T2 = y.left
 
       
        y.left = z
        z.right = T2
 
         
        z.height = 1 + max(self.calculate_height(z.left),self.calculate_height(z.right))
        y.height = 1 + max(self.calculate_height(y.left),self.calculate_height(y.right))
 
       
        return y
 
    def rightrotate(self, z):
 
        y = z.left
        T3 = y.right
 
       
        y.right = z
        z.left = T3
 
       
        z.height = 1 + max(self.calculate_height(z.left),self.calculate_height(z.right))
        y.height = 1 + max(self.calculate_height(y.left),self.calculate_height(y.right))
 
         
        return y
 
   
 
    def inorder(self, root,result):
 
        if not root:
            return []
       
        self.inorder(root.left,result)
        result.append([root.val,root.count])
       
        self.inorder(root.right,result)
        return result
   


if __name__=="__main__":

    allfiles = glob.glob('./dataset/*.txt')  
    t=Trie()
    docid=0
    finalwords=[]
   
    for f in allfiles:
       
       
       
        docid=docid+1
     
        file = open(f,encoding="utf8")
        fhand = file.read()
        for ele in fhand:  
            fhand = fhand.replace("'","")      
        punctuation = '''!“()”-’[]{};:'"\, <>./?@#$%^&*_~'''
        for ele in fhand:  
            if ele in punctuation:  
                fhand = fhand.replace(ele, " ")  

        fhand=fhand.lower()
        words=fhand.split()
        words = [word for word in words if not word in stop_words]
        for word in words:

                finalwords.append(word)
                if t.search_word(word)==True:
                   
                    avl=avltree()
                    avlroot=t.search_address(word)
                    avlroot=avl.insertnode(avlroot,docid)
                   
                    t.insert2(word,avlroot)
                if t.search_word(word)==False:
                   
                    t.insert_word(word,docid)
           
    finalwords = list(dict.fromkeys(finalwords))  
    print("enter query:")
    query=input().split()
    tfq={}
   
    weight_q={}
    df={}
    for i in query:
        p=tfq.get(i,query.count(i))
        tfq[i]=p
    normal= collections.defaultdict(list)
       
    avl=avltree()
    temp_dict={}
    doc_score={}
    for i in finalwords:
        node=t.search_address((i))
        ls=[]
        l=avl.inorder(node,ls)
        temp_list=[]
       
        if i in query:
            # print(l)
            p=df.get(i,len(ls))
            df[i]=p
            weight_q[i]=(1+math.log(tfq[i]))*(math.log(30/df[i]))
            for j in l:
                wei=(1+math.log(j[1]))
                # p=normal.get(j[0],[0])

                normal[j[0]].append([i,wei])
                if j[0] not in temp_list:
                    temp_list.append(j[0])
        for i in temp_list:
            s=0
            for j in range(len(normal[i])):
                s=s+(normal[i][j][1]*normal[i][j][1])
           
            temp_dict[i]=math.sqrt(s)


        if node:
            with open('output.txt', 'a') as f:
                print("{} ({}) --->" .format(i,len(ls)),end=" ",file=f)
                print(*ls,sep=",",file=f)
                print(file=f)
    for i in temp_dict.keys():
        s=0
        for j in range(len(normal[i])):
            s=s+(normal[i][j][1]/temp_dict[i])*weight_q[normal[i][j][0]]
        doc_score[s]=i

   
    l=list(sorted(doc_score.keys()))
    ten=0
    for i in l[::-1]:
    	if(ten==10):
    		break
    	print(doc_score[i])
    	ten=ten+1
        
