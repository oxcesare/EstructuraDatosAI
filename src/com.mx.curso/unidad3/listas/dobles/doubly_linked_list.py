from typing import Any, Iterable, List, Optional, Iterator

class Node:
    """Nodo de una lista doblemente enlazada."""
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None

class DoublyLinkedList:
    """Implementación mínima de lista doblemente enlazada."""
    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._len: int = 0
        if iterable:
            for v in iterable:
                self.append(v)

    def __len__(self) -> int:
        return self._len

    def append(self, value: Any) -> None:
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            assert self.tail is not None
            self.tail.next = node
            self.tail = node
        self._len += 1

    def prepend(self, value: Any) -> None:
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._len += 1

    def insert_at(self, index: int, value: Any) -> None:
        """Inserta en posición index (0-based). Si index <= 0 hace prepend; si index >= len hace append."""
        if index <= 0:
            self.prepend(value)
            return
        if index >= self._len:
            self.append(value)
            return

        cur = self.head
        for _ in range(index):
            assert cur is not None
            cur = cur.next
        assert cur is not None
        node = Node(value)
        prev = cur.prev
        assert prev is not None
        prev.next = node
        node.prev = prev
        node.next = cur
        cur.prev = node
        self._len += 1

    def remove(self, value: Any) -> None:
        """Elimina la primera aparición de value. Levanta ValueError si no existe."""
        cur = self.head
        while cur:
            if cur.value == value:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.tail = cur.prev
                self._len -= 1
                return
            cur = cur.next
        raise ValueError(f"Value not found: {value!r}")

    def to_list(self) -> List[Any]:
        out: List[Any] = []
        cur = self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

    def to_list_reverse(self) -> List[Any]:
        out: List[Any] = []
        cur = self.tail
        while cur:
            out.append(cur.value)
            cur = cur.prev
        return out

    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __repr__(self) -> str:
        vals = ", ".join(repr(x) for x in self)
        return f"DoublyLinkedList([{vals}])"

if __name__ == "__main__":
    # Ejemplo de uso: crear, insertar, eliminar y recorrer
    dll = DoublyLinkedList()
    # append
    dll.append("A")
    dll.append("B")
    dll.append("C")
    print("Después de append:", dll.to_list())           # ['A', 'B', 'C']

    # prepend
    dll.prepend("Z")
    print("Después de prepend:", dll.to_list())          # ['Z', 'A', 'B', 'C']

    # insert en posición 2 (0-based)
    dll.insert_at(2, "X")
    print("Después de insert_at(2,'X'):", dll.to_list()) # ['Z', 'A', 'X', 'B', 'C']

    # eliminar elemento
    dll.remove("B")
    print("Después de remove('B'):", dll.to_list())     # ['Z', 'A', 'X', 'C']

    # recorrido inverso
    print("Recorrido inverso:", dll.to_list_reverse())  # ['C', 'X', 'A', 'Z']

    # longitud y representación
    print("Len:", len(dll))
    print(dll)