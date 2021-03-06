import LinkedList

class HashTable(object):
    """
    Tabla hash de momento sin QueueList, posibles colisiones
    """
    def __init__(self,tableSize):
        self.tableSize = tableSize
        self.table = []
        for i in range(self.tableSize):
            aux = LinkedList.LinkedList()
            self.table.append(aux)

    def getHash(self,key):
        key = str(key)
        index = 0
        for i in key:
            index += ord(i)
        index = index%self.tableSize
        
        return index

    def insertElement(self,key,value):
        inserted = False
        index = self.getHash(key)
        linkedList = self.table[index]
        listSize = linkedList.getSize()
        if not linkedList.isEmpty():
            linkedList.moveHead()
            for i in range(listSize):
                nodeKey, nodeValue = linkedList.getCurrent()
                if nodeKey == key:
                    linkedList.modifyData(value)
                    inserted = True
                    break
                linkedList.moveNext()
            if not inserted:
                linkedList.insertAfter(key,value)
        else:
            linkedList.insertAfter(key,value)
        print 'Insertado Correctamente'

    def findElement(self,key):
        index = self.getHash(key)
        found = False
        linkedList = self.table[index]
        if not linkedList.isEmpty():
            linkedList.moveHead()
            for i in range(linkedList.getSize()):
                nodeKey , nodeValue = linkedList.getCurrent()
                if nodeKey == key:
                    return str(key) + ": " + str(nodeValue)
                linkedList.moveNext()
        return "No se encuentra"

    def deleteElement(self,key):
        index = self.getHash(key)
        linkedList = self.table[index]
        if not linkedList.isEmpty():
            linkedList.moveHead()
            for i in range(linkedList.getSize()):
                nodeKey, nodeValue = linkedList.getCurrent()
                if nodeKey == key:
                    linkedList.remove()
                    return True
                linkedList.moveNext()
                
        return False


    def __str__(self):
        text = ''
        for i in range(self.tableSize):
            queueList = self.table[i]
            text += queueList.__str__() + '\n'           
        return text
