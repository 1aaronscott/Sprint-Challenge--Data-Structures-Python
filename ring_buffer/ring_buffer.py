''' Ringbuffer class '''


class RingBuffer:
    ''' class defining a type of list which has a fixed, 
    specified size. '''

    def __init__(self, capacity):
        self.capacity = capacity
        # have to fill with Nones so I have something to replace later
        self.buffer = [None]*self.capacity
        self.position = 0

    def append(self, item):
        ''' add item to the list self.stor'''
        # print(self.capacity)
        # print(self.position)
        # if the position is beyond the max index position move it to the beginning
        if self.position == self.capacity:
            self.position = 0
        # replace the existing value with item
        self.buffer[self.position] = item
        # point the cursot to the next position
        self.position += 1

    def get(self):
        ''' return the buffer list without Nones '''
        values = []
        for i in self.buffer:
            if i:
                values.append(i)
        return values


# buffer = RingBuffer(3)
# print(buffer.get())   # should return []
# buffer.append('a')
# print(buffer.get())

# buffer.append('b')
# buffer.append('c')
# print(buffer.get())
# buffer.append('d')
# print(buffer.get())
# buffer.append('e')
# print(buffer.get())
