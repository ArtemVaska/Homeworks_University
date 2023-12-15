"""
2. Написать класс очереди и стека, используя внутри только списки.
"""


class Queue:
    def __init__(self, queue_list=[]):
        self.queue_list = queue_list

    @property
    def values(self):
        return self.queue_list

    def add_to_queue(self, value):
        self.queue_list.append(value)

    def get_from_queue(self, count=1):
        subset_queue = self.queue_list[:count]
        self.queue_list = self.queue_list[count:]
        return subset_queue


class Stack:
    def __init__(self, stack_list=[]):
        self.stack_list = stack_list

    @property
    def values(self):
        return self.stack_list

    def add_to_stack(self, value):
        self.stack_list.append(value)

    def get_from_stack(self, count=1):
        subset_stack = self.stack_list[-count:]
        self.stack_list = self.stack_list[:-count]
        return subset_stack


print('Пример с очередью:')
q1 = Queue([1, 2, 3, 4, 5])
print(q1.values)
q1.add_to_queue(6)
print(q1.values)
subs = q1.get_from_queue(2)
print(q1.values)
print(subs)
print()

print('Пример со стэком:')
s1 = Stack([1, 2, 3, 4, 5])
print(s1.values)
s1.add_to_stack(6)
print(s1.values)
subs = s1.get_from_stack(2)
print(s1.values)
print(subs)
print()
