#  Implement a program to use the collections module to
#  perform advanced data manipulation tasks.


from collections import Counter, defaultdict, namedtuple, deque

# Counter example: Count occurrences of elements in a list
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print("Element counts:", counter)

# defaultdict example: Group values by keys
grouped = defaultdict(list)
pairs = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
for key, value in pairs:
    grouped[key].append(value)
print("Grouped values:", dict(grouped))

# namedtuple example: Create lightweight objects
Person = namedtuple('Person', ['name', 'age'])
person1 = Person('Alice', 25)
person2 = Person('Bob', 30)
print("Namedtuple example:", person1, person2)

# deque example: Efficient queue operations
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
dq.pop()