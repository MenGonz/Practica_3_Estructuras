
from Tree import Tree
from User import User
from random import randint

if __name__ == "__main__":
    T: Tree = Tree()
    for _ in range(10):
        r = randint(0,100)
        T.insert(r, User("Juan", r))
        
    print(T)