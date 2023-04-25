class queue:
    def __init__(self):
        self.q=[]
    def isempty(self):
        if self.q==[]:
            return True
        else:
            return False
    def enqueue(self,element):
        self.q.append(element)
    def dequeue(self):
        if self.isempty():
            return -1
        else:
            return self.q.pop(0)
    def search(self,element):
        if self.isempty():
            return -1
        else:
            try:
                n=self.q.index(element)
                return n
            except ValueError:
                return -2
    def display(self):
        return self.q

        
