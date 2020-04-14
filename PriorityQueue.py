class PriorityQueue:

       def __init__(self):
           self.items = []

       def isEmpty(self):
           return self.items == []

       def sortComparatorByCost(self, item):
           return item.total_cost

       def enqueue(self, item):
              self.items.append(item)
              self.items.sort(key=self.sortComparatorByCost, reverse=False)

       def dequeue(self):
              return self.items[0]
              # return self.items.pop()

       def returnQueueAsString(self):
           queue_str = ""
           for eachItem in self.items:
               queue_str += str(eachItem.total_cost) + " "
           return queue_str

       def isQueueContainsElement(self, element):
           for eachElement in self.items:
               if eachElement[0] == element:
                   return True
           return False

       def clear_queue(self):
              del self.items
              self.items = []

       @staticmethod
       def are_equal(a, b):
              if len(a) != len(b):
                     return False
              for i in range(0, len(a)):
                     if a[i] != b[i]:
                            return False
              return True


       def find(self, item):
              for i in range(0, len(self.items)):
                     if PriorityQueue.are_equal(self.items[i].queens, item.queens):
                            # PriorityQueue.delete_index = i
                            return self.items[i]
              return None

       def delete(self, item):
              deleted = self.find(item)
              self.items.remove(deleted)
