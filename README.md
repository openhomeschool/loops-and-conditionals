# The "loops-and-conditionals" project
## openhome.school Computer Class

This project reflects on python loops and conditionals with some "quiz" code, below.
The code is also found in separate files in this directory, to run/test/expand.

## Details

**A "loop" is a bit of code that repeats, but with slight variations every iteration.**

What does this code do?

```python
for i in range(10):
	j = i + 1
	print(f'{i} is less than {j}')
```

Run c.py ('python3 c.py') to find out!

What does this code do?

```python
numbers = [3, 7, 16, 1, 26, 12]
s = 0

for number in numbers:
	s += number

print(f's is {s}')
```

Run s.py ('python3 s.py') to find out!

What does this code do?

```python
numbers = [5, 4, 7, 9, 6, 4]
s = 0.0

for number in numbers:
	s += number
a = s / len(numbers)

print(f'a is {a}')
```

Run a.py ('python3 a.py') to find out!

What does this code do?

```python
numbers = [5, 4, 7, 9, 6, 4]

i = min(numbers)
x = max(numbers)
r = x - i
print (f'r is {r}')
```

Run r.py ('python3 r.py') to find out!

What does this code do?

```python
numbers = [5, 12, 7, 9, 6, 4]
results = []

for number in numbers:
	for i in range(len(results)):
		result = results[i]
		if number < result:
			results.insert(i, number)
			break
	else:
		results.append(number)
		continue

print(f'results: {results}')
```

Run o.py ('python3 o.py') to find out!

What does this code do?

```python
words = ['hello', 'bye', 'zebra', 'alphabet', 'money']
results = []

for word in words:
	for i in range(len(results)):
		result = results[i]
		if word < result:
			results.insert(i, word)
			break
	else:
		results.append(word)
		continue

print(f'results: {results}')
```

Run o2.py ('python3 o2.py') to find out!

What does this code do?

```python
def o(items):
	results = []
	for item in items:
		for i in range(len(results)):
			result = results[i]
			if item < result:
				results.insert(i, item)
				break
		else:
			results.append(item)
			continue
			
	return results


words = o(['hello', 'bye', 'zebra', 'alphabet', 'money'])
print(f'word results: {words}')
numbers = o([5, 12, 7, 9, 6, 4])
print(f'number results: {numbers}')
```

Run o3.py ('python3 o3.py') to find out!

