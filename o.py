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
