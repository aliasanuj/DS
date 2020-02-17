class node:
    def __init__(self,value):
        self.info = value
        self.link = None #link is the next reference
class linkedList:

    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("empty list")
            return
        else:
            print("list is : ")
            p = self.start
            while p is not None:
                print(p.info," ",end = " ")
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        count = 0
        while p is not None :
            count = count + 1
            p = p.link
        print("total no of node in list ",count)




list = singleLinkedList()
list.createList()

while True:
    print("1. Display list")
    print("2. Count no of nodes")
    print("3. search for an element")
    print("4. Insert in empty list / Insert in beginning of list")
    print("5. Insert a node at the end of list")
    print("6. Insert a node after a specified node")
    print("7. Insert a node before a sepcified node")
    print("8. Insert a node at a agiven position")
    print("9. Delete the frst node")
    print("10. Delete the last node")
    print("11. Delete any node")
    print("12. Reverse the list")

    option = int(input("select the choice : "))
    if option == 1:
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        data = int(input("Enter the element :"))
        list.search(data)
    elif option == 4:
        data = int(input("Enter the element :"))
        list.insert_in_beginning(data)
    elif option == 5:
        data = int(input("Enter the element :"))
        list.insert_at_end(data)
    elif option == 6:
        data = int(input("Enter the element to be inserted :"))
        x = int(input("Enter the element after which to insert:"))
        list.insert_after(data,x)
    elif option == 7:
        data = int(input("Enter the element to be inserted :"))
        x = int(input("Enter the element before which to insert:"))
        list.insert_before(data,x)
    elif option == 8:
        data = int(input("Enter the element to be inserted :"))
        x = int(input("Enter the position at which to insert : "))
        list.insert_at_position(data,x)
    elif option == 9:
        list.delete_first_node(data)
    elif option == 10:
        list.delete_last_node(data)
    elif option == 11:
        data = int(input("Enter the element to be deleted"))
        list.delete_node(data)
    elif option == 12:
        list.reverse_list()

