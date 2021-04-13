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
