sample = 'dabAcCaCBAcCcaDA'
sample_list = list(sample)
result = ''
actual_polymer = sample_list
while True:
    last_polymer = actual_polymer[:]
    for i in range(len(actual_polymer)):
        actual_letter = actual_polymer[i]
        if i != (len(actual_polymer) - 1):
            next_letter = actual_polymer[i+1]

        if actual_letter.lower() == next_letter.lower() and actual_letter != next_letter:
            del actual_polymer[i]
            try:
                del actual_polymer[i]
                break
            except:
                ...
    if actual_polymer == last_polymer:
        break
            

print(len(sample_list))