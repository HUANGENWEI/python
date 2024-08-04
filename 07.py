Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class CircularDoubleLinkList(object):
...     def __init__(self):
...         self.__head = DoubleLinkNode(None)
...         self.__head.next = self.__head
... 
...     def InsertInHead(self, val_list):
...         """
...         头插法
...         :param val_list:
...         :return:
...         """
...         prehead = self.__head
...         for val in val_list:
...             new_node = DoubleLinkNode(val)
...             if self.IsEmpty():
...                 prehead.next = new_node
...                 new_node.prior = prehead
...                 new_node.next = self.__head
...                 self.__head.prior = new_node
...             else:
...                 new_node.next = prehead.next
...                 prehead.next.prior = new_node
...                 prehead.next = new_node
...                 new_node.prior = prehead
... 
...     def InsertInTail(self, val_list):
...         """
...         尾插法
...         :param val_list:
...         :return:
...         """
...         prehead = self.__head
...         for val in val_list:
...             new_node = DoubleLinkNode(val)
...             prehead.next = new_node
...             new_node.prior = prehead
...             new_node.next = self.__head
            self.__head.prior = new_node
            prehead = prehead.next

    def IsEmpty(self):
        """
        判断循环双链表是否为空, 空表返回True
        :return:
        """
        if self.__head.next == self.__head:
            return True

    def LengthList(self):
        """
        返回循环双链表的长度
        :return:
        """
        prehead = self.__head
        count = 0
        if self.IsEmpty():
            return count
        while prehead.next != self.__head:
            count += 1
            prehead = prehead.next
        return count

    def TraverseList(self):
        """
        遍历循环双链表, 并打印
        :return:
        """
        prehead = self.__head
        if self.IsEmpty():
            print('链表为空!')
            return 0
        while prehead.next != self.__head:
            prehead = prehead.next
            print(prehead.data, end=' ')
        print('')

    def InsertInPosition(self, pos, data):
        """
        在某个位置插入
        :param pos: [1, LengthSingleLinkList + 1]
        :param data:
        :return:
        """
        prehead = self.__head
        new_node = DoubleLinkNode(data)
        if pos <= 0 or pos > self.LengthList() + 1:
            print('插入位置错误!')
            return 0
        count = 0
        while count < pos - 1:
            prehead = prehead.next
            count += 1
        if prehead.next != self.__head:
            new_node.next = prehead.next
            prehead.next.prior = new_node
        else:
            new_node.next = self.__head
            self.__head.prior = new_node
        new_node.prior = prehead
        prehead.next = new_node

    def SearchWithPosition(self, pos):
        """
        按位置查找元素
        :param pos: [1, LengthSingleLinkList]
        :return:
        """
        prehead = self.__head
        if pos <= 0 or pos > self.LengthList():
            print('位置错误!')
            return -1
        count = 0
        while count < pos:
            prehead = prehead.next
            count += 1
        data = prehead.data
        return data

    def SearchWithVal(self, data):
        """
        按值查找元素
        :param data:
        :return:
        """
        prehead = self.__head
        count = 0
        while prehead.next != self.__head:
            prehead = prehead.next
            count += 1
            if prehead.data == data:
                return count
        print('该节点不存在!')
        return -1

    def RemoveWithPosition(self, pos):
        """
        按位置移除元素
        :param pos: [1, LengthSingleLinkList]
        :return:
        """
        prehead = self.__head
        if pos <= 0 or pos > self.LengthList():
            print('位置错误!')
            return 0
        count = 0
        while count < pos - 1:
            prehead = prehead.next
            count += 1
        temp = prehead.next
        if temp.next == self.__head:
            prehead.next = self.__head
            self.__head.prior = prehead
        else:
            prehead.next = temp.next
            temp.next.prior = prehead
        del temp

    def RemoveWithVal(self, data):
        """
        按值移除元素
        :param data:
        :return:
        """
        prehead = self.__head
        while prehead.next != self.__head:
            prehead = prehead.next
            if prehead.data == data:
                if prehead.next == self.__head:
                    prehead.prior.next = self.__head
                    self.__head.prior = prehead.prior
                else:
                    prehead.prior.next = prehead.next
                    prehead.next.prior = prehead.prior
                return -1
        print('该节点不存在!')

from LinkList import CircularDoubleLinkList
if __name__ == '__main__':
    l1 = CircularDoubleLinkList()
    print('頭插法創建循環雙鏈表l1: ',end=' ')
    l1.InsertInHead([1,3,5,7])
    l1.TraverseList()
    
    l2 = CircularDoubleLinkList()
    print('尾插法創間循環鏈表l2: ',end=' ')
    l2.InsertInTail([1,3,5,7])
    l2.TraverseList()
    
    print('鏈表12的長度為: %d' %l2.LengthList())
    print('在鏈表12的第3個位置插入值為2的節點: ',end = '')
    l2.InsertInPosition(3,2)
    l2.TraverseList()
    
    print('鏈表12的第4個位置上的節點為: %d' % l2.SearchWithPosition(4))
    print('鏈表12值為7的節點的位置為: %d' % l2.SearchWithVal(7))
    print('移除鏈表12的第5個位置上的節點: ', end='')
    
    l2.RemoveWithPosition(5)
    l2.TraverseList()
    
    print('移除鏈表12值為1的節點: ',end='')
    l2.RemoveWithVal(1)
    l2.TraverseList()class CircularDoubleLinkList(object):
    def __init__(self):
        self.__head = DoubleLinkNode(None)
        self.__head.next = self.__head

    def InsertInHead(self, val_list):
        """
        头插法
        :param val_list:
        :return:
        """
        prehead = self.__head
        for val in val_list:
            new_node = DoubleLinkNode(val)
            if self.IsEmpty():
                prehead.next = new_node
                new_node.prior = prehead
                new_node.next = self.__head
                self.__head.prior = new_node
            else:
                new_node.next = prehead.next
                prehead.next.prior = new_node
                prehead.next = new_node
                new_node.prior = prehead

    def InsertInTail(self, val_list):
        """
        尾插法
        :param val_list:
        :return:
        """
        prehead = self.__head
        for val in val_list:
            new_node = DoubleLinkNode(val)
            prehead.next = new_node
            new_node.prior = prehead
            new_node.next = self.__head
            self.__head.prior = new_node
            prehead = prehead.next

    def IsEmpty(self):
        """
        判断循环双链表是否为空, 空表返回True
        :return:
        """
        if self.__head.next == self.__head:
            return True

    def LengthList(self):
        """
        返回循环双链表的长度
        :return:
        """
        prehead = self.__head
        count = 0
        if self.IsEmpty():
            return count
        while prehead.next != self.__head:
            count += 1
            prehead = prehead.next
        return count

    def TraverseList(self):
        """
        遍历循环双链表, 并打印
        :return:
        """
        prehead = self.__head
        if self.IsEmpty():
            print('链表为空!')
            return 0
        while prehead.next != self.__head:
            prehead = prehead.next
            print(prehead.data, end=' ')
        print('')

    def InsertInPosition(self, pos, data):
        """
        在某个位置插入
        :param pos: [1, LengthSingleLinkList + 1]
        :param data:
        :return:
        """
        prehead = self.__head
        new_node = DoubleLinkNode(data)
        if pos <= 0 or pos > self.LengthList() + 1:
            print('插入位置错误!')
            return 0
        count = 0
        while count < pos - 1:
            prehead = prehead.next
            count += 1
        if prehead.next != self.__head:
            new_node.next = prehead.next
            prehead.next.prior = new_node
        else:
            new_node.next = self.__head
            self.__head.prior = new_node
        new_node.prior = prehead
        prehead.next = new_node

    def SearchWithPosition(self, pos):
        """
        按位置查找元素
        :param pos: [1, LengthSingleLinkList]
        :return:
        """
        prehead = self.__head
        if pos <= 0 or pos > self.LengthList():
            print('位置错误!')
            return -1
        count = 0
        while count < pos:
            prehead = prehead.next
            count += 1
        data = prehead.data
        return data

    def SearchWithVal(self, data):
        """
        按值查找元素
        :param data:
        :return:
        """
        prehead = self.__head
        count = 0
        while prehead.next != self.__head:
            prehead = prehead.next
            count += 1
            if prehead.data == data:
                return count
        print('该节点不存在!')
        return -1

    def RemoveWithPosition(self, pos):
        """
        按位置移除元素
        :param pos: [1, LengthSingleLinkList]
        :return:
        """
        prehead = self.__head
        if pos <= 0 or pos > self.LengthList():
            print('位置错误!')
            return 0
        count = 0
        while count < pos - 1:
            prehead = prehead.next
            count += 1
        temp = prehead.next
        if temp.next == self.__head:
            prehead.next = self.__head
            self.__head.prior = prehead
        else:
            prehead.next = temp.next
            temp.next.prior = prehead
        del temp

    def RemoveWithVal(self, data):
        """
        按值移除元素
        :param data:
        :return:
        """
        prehead = self.__head
        while prehead.next != self.__head:
            prehead = prehead.next
            if prehead.data == data:
                if prehead.next == self.__head:
                    prehead.prior.next = self.__head
                    self.__head.prior = prehead.prior
                else:
                    prehead.prior.next = prehead.next
                    prehead.next.prior = prehead.prior
                return -1
        print('该节点不存在!')







