from node import Node

class CircularList:
    def __init__(self):
        self.head = None
        self.current_song = None

    def is_empty(self):
        return self.head is None

    def print_list(self):
        if self.is_empty():
            print("La lista esta vacia")
            return

        current = self.head
        while True:
            print(current.data, end="->")
            current = current.next
            if current == self.head:
                break
        print()

    def add_element(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_element(self, data):
        if self.is_empty():
            print('La lista esta vacia')
            return

        if self.head.data == data:
            current = self.head
            while current.next != self.head:
                current = current.next
            if self.head == self.head.next:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
        else:
            current = self.head
            prev = None
            while True:
                if current.data == data:
                    prev.next = current.next
                    break
                prev = current
                current = current.next
                if current == self.head:
                    break

    def next_song(self):
        if self.is_empty():
            print("La playlist esta vacia")
            return

        if self.current_song is None:
            self.current_song = self.head
        else:
            self.current_song = self.current_song.next

            if self.current_song == self.head:
                self.current_song = None

        print(f"Reproduciendo {self.current_song.data}")

    def prev_song(self):
        if self.is_empty():
            print("La playlist esta vacia")
            return

        if self.current_song is None:
            self.current_song = self.head
        else:
            prev_node = None
            current = self.head

            while current.next != self.current_song:
                current = current.next

            prev_node = current
            self.current_song = prev_node

            if self.current_song == self.head:
                while current.next != self.head:
                    current = current.next
                    self.current_song = current

        print(f"Reproduciendo: {self.current_song.data}")