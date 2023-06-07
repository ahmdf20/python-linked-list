class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
class TodoList:
  def __init__(self):
    self.head = None
    self.newDict = {}
  
  def addToFront(self, data):
    newNode = Node(data)
    newNode.next = self.head
    self.head = newNode
  
  def addToEnd(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = newNode

  def printLinkedList(self):
    current = self.head
    print(f"{'Prioritas':<10} {'Deskripsi':<25}")
    while current:
      print(f"{current.data['prioritas']:<10} {current.data['desc']:<25}")
      current = current.next

todo = TodoList()
todo.addToFront({"desc": "Mengerjakan Tugas Project 1", "prioritas": 1})
todo.addToFront({"desc": "Mengerjakan tugas komunikasi teknik", "prioritas": 2})
todo.addToFront({"desc": "Mengerjakan tugas SQL", "prioritas": 3})


print("Linked List Awal : ")
todo.printLinkedList()
