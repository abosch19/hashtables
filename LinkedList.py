class LinkedList(object):
    class Node(object):
        def __init__(self, key, data, next = None):
            self.data = data
            self.key = key
            self.next = next
        def getData(self):
            return self.data
        def getNext(self):
            return self.next
        def getKey(self):
            return self.key
        def setData(self, data):
            self.data = data
        def setNext(self, next):
            self.next = next
        def setKey(self, key):
            self.key = key
        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def getHead(self):
        if self.head == None:
            raise IndexError
        else:
            return self.head.getData()
    def getTail(self):
        if self.tail == None:
            raise IndexError
        else:
            return self.tail.getData()
    def getCurrent(self):
        if self.current == None:
            raise IndexError
        else:
            return self.current.getKey(), self.current.getData()
    def moveNext(self):
        if self.head == None:
            raise IndexError
        elif self.current.getNext() == None:
            raise IndexError
        else:
            aux = self.current.getNext()
            self.current = aux
    def moveHead(self):
        if self.head == None:
            raise IndexError
        else:
            self.current = self.head
    def isEmpty(self):
        return self.size == 0
    def getSize(self):
        return self.size
    def clear(self):
        self.size = 0
        self.current = None
        self.tail = None
        self.head = None
    def insertBefore(self, key, data):
        if self.head == None:
            aux = self.Node(key, data)
            self.head = aux
            self.tail = aux
            self.current = aux
        elif self.current == self.head:
            aux = self.Node(key, data,self.head)
            self.head = aux
            self.current = aux
        else:
            aux = self.head
            aux1 = self.Node(key, data)
            while aux.getNext() != self.current:
                aux = aux.getNext()
            aux1.setNext(self.current)
            aux.setNext(aux1)
            self.current = aux1
        self.size += 1
    def insertAfter(self, key, data):
        if self.head == None:
            aux = self.Node(key, data)
            self.head = aux
            self.tail = aux
        elif self.current == self.tail:
            aux = self.Node(key,data)
            self.tail = aux
            self.current.setNext(aux)
        else:
            aux = self.Node(key, data,self.current.getNext())
            self.current.setNext(aux)
        self.current = aux
        self.size += 1
    def remove(self):
        if not self.head == None:
            if self.current == self.head:
                if self.current.getNext() == None:
                    self.head = None
                    self.current = None
                    self.tail = None
                else:
                    self.head = self.current.getNext()
                    self.current = self.head
            else:
                if self.current == self.tail:
                    aux = self.head
                    while aux.getNext() != self.current:
                        aux = aux.getNext()
                    aux.setNext(self.current.getNext())
                    self.current = aux
                    self.tail = aux
                else:
                    aux = self.head
                    while aux.getNext() != self.current:
                        aux = aux.getNext()
                    aux.setNext(self.current.getNext())
                    self.current = aux
            self.size -= 1     
        else:
            raise IndexError

    def modifyData(self, data):
        aux = self.current
        aux.setData(data)
        
    def __str__(self):
        l = ''
        if self.size > 0:
            aux = self.head
            for i in range(self.size):
                l = l + aux.__str__() + ' '
                aux = aux.getNext()
        else:
            l = 'None'
        return l
        
