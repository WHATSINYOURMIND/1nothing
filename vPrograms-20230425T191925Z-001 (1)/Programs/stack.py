class stack:
    def __init__(self):
        self.st=[]
    def isempty(self):
        if self.st==[]:
            return True
        else:
            return False
    def push(self,element):
        self.st.append(element)
    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.st.pop()
    def peek(self):
        n=len(self.st)
        return self.st[n-1]
    def search(self,element):
        if self.isempty():
            return -1
        else:
            try:
                n=self.st.index(element)
                return n
            except ValueError:
                return -2
    def display(self):
        return self.st

        
