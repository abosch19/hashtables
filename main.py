import HashTable
from time import *

if __name__=='__main__':
    table = HashTable.HashTable(100)
    table.insertElement(1235315,'hola')
    table.insertElement(1235344,'xd')
    element = table.findElement(123535)
    print element
    print table    
    

    
    
