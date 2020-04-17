import concurrent.futures
import logging
import time


class Common:
    def __init__(self, number: int):
        self.number = number


class Vector:
    class Item:
        def __init__(self, left: Common, right: Common):
            self.left = left
            self.right = right

    def __init__(self):
        self.items = list()

    def append(self, item: Item):
        self.items.append(item)

    def __str__(self):
        output = []
        for item in self.items:
            output.append(f"{item.left.number} - {item.right.number}")

        return '\n'.join(output)

    def __len__(self):
        return len(self.items)


def thread_function(item: Vector.Item):
    thread = item.right.number
    logging.info("Thread %s: starting", thread)
    item.left.number *= 10
    item.right.number += 10
    logging.info("Thread %s: finishing", thread)


if __name__ == "__main__":
    vector = Vector()
    for i in range(10):
        left  = Common(-i)
        right = Common(+i)
        vector.append(Vector.Item(left, right))

    print(vector)

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(vector)) as executor:
        executor.map(thread_function, vector.items)

    print(vector)
