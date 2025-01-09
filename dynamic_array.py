import ctypes
class Empty:
  def __repr__(self):
    return '<empty>'

class DynamicArray:
    def __init__(self):
        self.n = 0
        self.size = 1
        self.A = self._make_array(self.size)
        
    def __len__(self):
        return self.n
        
    def append(self,item):
        if self.n == self.size:
            self._resize(self.size*2)
        self.A[self.n] = item
        self.n+=1
        print("size "+ str(self.size))
        print ("n "+ str(self.n))

    def insertAt(self, index, item):
        if index<0 or index > self.n:
            print("Range of index is 0 <= index <= n")
            return
        if self.n == self.size:
            self._resize(self.size*2)
        self.n+=1
        for i in range(self.n-1,index,-1):
            self.A[i] = self.A[i-1]
        self.A[index] = item        

    def removeAt(self,index):
        if index >= self.n:
            raise ValueError("Index out of bound!")
        for i in range (index, self.n-1):
            self.A[i] = self.A[i+1]
        self.n-=1

    def remove(self,item):
        index = None
        for i in range(self.n):
            if self.A[i] == item:
                index = i
                break
        if index is None:
            print("Item not found in the array")
            return
        for i in range (index, self.n-1):
            self.A[i] = self.A[i+1]
        self.n-=1

    def clear(self):
        self.n = 0
        self.size = 1
        
    def __str__(self):
        temp = ""
        for i in range(self.n):
            temp = temp+str(self.A[i])+','
        return '['+temp[:-1]+']'
        
    def _resize(self, new_size):
        B = self._make_array(new_size)
        for i in range(self.n):
            B[i] = self.A[i]
        self.size = new_size
        self.A = B

    def _make_array(self, capacity):
        B = (capacity*ctypes.py_object)()
        return B
    
