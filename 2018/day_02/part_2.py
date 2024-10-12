boxes = '''abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz'''

def get_similars(original: list, test: list) -> bool:
    different_letter = 0
    is_similar = True
    for letter in test:
        if letter not in original:
            different_letter += 1
            if different_letter > 1:
                is_similar = False
    return is_similar
boxes = boxes.splitlines()
correct_box = None
for i in range(len(boxes)):
    for box in boxes:
        if box == boxes[i]:
            continue
        elif get_similars(boxes[i], box):
            correct_box = [box, boxes[i]]
    if correct_box:
        break
id = ''
for letter in correct_box[0]:
    if letter in correct_box[1]:
        id += letter
print(id)