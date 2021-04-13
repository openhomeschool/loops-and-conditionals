ords = ['hello', 'bye', 'zebra', 'alphabet', 'money']
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
