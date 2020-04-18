from multiprocessing import Pool, Array, Value, Process
import logging


class Common:
    def __init__(self, number: int):
        self.number = Value('i', number)

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
            output.append(f"{item.left.number.value} - {item.right.number.value}")

        return '\n'.join(output)

    def __len__(self):
        return len(self.items)


def thread_function(item: Vector.Item):
    thread = item.right.number
    logging.info("Thread %s: starting", thread)
    item.left.number *= 10
    item.right.number += 10
    logging.info("Thread %s: finishing", thread)


def left_process(items: list):
    logging.info("Thread left")
    for item in items:
        item.left.number.value += 10
        logging.info("Thread left: %s", item.left.number.value)


def right_process(items: list):
    for item in items:
        item.right.number.value *= 10
        logging.info("Thread right: %s", item.right.number.value)


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

    left = Process(target=left_process, args=(vector.items, ))
    right = Process(target=right_process, args=(vector.items, ))

    left.start()
    right.start()

    left.join()
    right.join()

    print(vector)

