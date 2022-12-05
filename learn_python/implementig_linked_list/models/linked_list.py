from custom_errors.list_is_empty_error import ListIsEmptyError
from models.linked_list_node import ListNode


class LinkedList:
    def __init__(self):
        self.__head: ListNode = None
        self.__size = 0

    def with_head(self, head: ListNode):
        self.__head = head
        self.__size = 1
        return self

    def size(self):
        "returns number of data elements in list"
        return self.__size

    def is_empty(self):
        "bool returns true if empty"
        return self.size() == 0

    def push_front(self, data):
        "adds an item to the front of the list"
        if self.__head is None:
            node = ListNode(data)
            self.__head = node
        else:
            first_node = self.__head
            node = ListNode(data)
            node.set_next(first_node)
            self.__head = node
        self.__size += 1

    def pop_front(self):
        "removes front item and returns its value"
        if self.size() == 0:
            raise ListIsEmptyError()
        if self.size() == 1:
            data = self.__head.get_value()
            self.__head = None
            self.__size = 0
            return data

        data = self.__head.get_value()
        self.__head = self.__head.get_next()
        self.__size -= 1
        return data

    def push_back(self, value):
        "adds an item at the end"
        if self.size() == 0:
            self.push_front(value)
        elif self.size() == 1:
            self.__head.set_next(ListNode(value))
            self.__size += 1
        else:
            last_node = self.__head
            while last_node.get_next() is not None:
                last_node = last_node.get_next()
            last_node.set_next(ListNode(value))
            self.__size += 1

    def pop_back(self):
        if self.size() == 0:
            raise ListIsEmptyError()
        if self.size() == 1:
            value = self.__head.get_value()
            self.__head.set_next(None)
            return value

        prelast_node = self.__head
        while prelast_node.get_next().get_next() is not None:
            prelast_node = prelast_node.get_next()

        value = prelast_node.get_next().get_value()
        prelast_node.set_next(None)
        return value

    def value_at(self, index):
        "returns the value of the nth item (starting at 0 for first)"
        if index > self.size() or index < 0:
            raise IndexError(index)

        if index == 0:
            return self.__head.get_value()
        else:
            node = self.__head
            while index != 0:
                node = node.get_next()
                index -= 1
            return node.get_value()

    def insert(self, index, value):
        if index > self.size() or index < 0:
            raise IndexError(index)
        if index == 0:
            self.push_front(value)
            return
        else:
            cur_index = 0
            node = self.__head
            prev = node
            while cur_index != index and node is not None:
                cur_index += 1
                prev = node
                node = node.get_next()
            if cur_index != index:
                raise IndexError(index)
            else:
                new_node = ListNode(value)
                new_node.set_next(node)
                prev.set_next(new_node)
                self.__size += 1

    def front(self):
        "get value of the first item"
        if self.size() == 0:
            raise ListIsEmptyError
        return self.__head.get_value()

    def back(self):
        "get value of the last item"
        if self.size() == 0:
            raise ListIsEmptyError
        if self.size() == 1:
            return self.__head.get_value()
        else:
            node = self.__head
            while node.get_next() is not None:
                node = node.get_next()
            return node.get_value()

    def reverse(self):
        if self.size() == 0 or self.size() == 1:
            pass
        else:
            node = self.__head
            reversed_list = LinkedList()
            while reversed_list.size() != self.size():
                reversed_list.push_front(node.get_value())
                node = node.get_next()
            self.__head = reversed_list.__head

    def remove_at(self, index):
        if index > self.size() or index < 0:
            raise IndexError(index)
        node = self.__head
        prev = node
        cur_index = 0
        while cur_index != index:
            if node.get_next() is not None:
                prev = node
                node = node.get_next()
                cur_index += 1
            else:
                break
        if cur_index == index:
            prev.set_next(node.get_next())
        else:
            raise IndexError(index)

    def remove_value(self, value):
        node = self.__head
        prev = node
        while node.get_next() is not None:
            if node.get_value() == value:
                prev.set_next(node.get_next())
                break
            else:
                prev = node
                node = node.get_next()

    def print(self):
        str = ""
        node = self.__head
        while node is not None:
            str = f'{str} {node.get_value()}'
            node = node.get_next()
        return str.strip()