def solution(new_id):
    filtered = []
    index = 0
    new_id = new_id.lower()
    for char in new_id:
        if char.isalpha() or char.isdigit() or char in '-_.':
            filtered.append(char)
    new_id = ''.join(filtered)
    for char in new_id[:-1]:
        if char == '.' and new_id[index + 1:index + 2] == '.':
            new_id = new_id[:index] + new_id[index + 1:]
        else:
            index += 1
    if new_id[0] == '.': new_id = new_id[1:]
    if new_id and new_id[-1] == '.': new_id = new_id[:-1]
    if not new_id: new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id and new_id[-1] == '.': new_id = new_id[:-1]
    elif len(new_id) == 2: new_id += new_id[-1:]
    elif len(new_id) == 1: new_id += new_id[-1:] * 2
    return new_id
print(solution("abcdefghijklmn.p"))