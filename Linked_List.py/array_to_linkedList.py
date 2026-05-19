# Array convert into LL. and  traversal Linked List

'''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



def convertArrayLL(arr):

    head = Node(arr[0])

    mover = head

    for i in range(1,len(arr)):
        temp = Node(arr[i])

        mover.next = temp

        mover = temp

    return head

def main():

    arr = [12,4,6,8,10]

    head = convertArrayLL(arr)

    temp = head

    while temp != None:
        print(temp.data, end = " ")
        temp = temp.next



    # print(head.next.next.next.next.data)

if __name__ == '__main__':
    main()'''


'''   head ─┐
      ↓
temp ─┘
     [12 | • ] → [5 | • ] → [6 | • ] → [8 | None]'''




# LinkedList Length

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# def convertArrayLL(arr):

    # head = Node(arr[0])
    # mover = head

    # for i in range(1,len(arr)):
        # temp = Node(arr[i])
        # mover.next = temp
        # mover = temp

    # return head

def lengthofLL(head):

    cnt = 0
    temp = head

    while temp != None:
        cnt += 1

        temp = temp.next

    return cnt

def main():
    arr = [2,4,6,8]

    head = convertArrayLL(arr)

    print(lengthofLL(head))

if __name__ == '__main__':
    main()
