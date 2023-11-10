
from Tree import Tree
from User import User
from random import randint

if __name__ == "__main__":
    T: Tree = Tree()
    usuarios = [User("juan",10101013),
                User("Pablo",10001011),
                User("Maria",10101015),
                User("Ana",1010000),
                User("Diana",10111105),
                User("Mateo",10110005)]
    
    for u in usuarios:
        T.insert(u.get_key(), u)
        
    
    #print(T)
    print(T.traverse("in"))