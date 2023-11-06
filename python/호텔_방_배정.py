def solution(k, room_number):
    occupied_rooms = {}
    answer = []
    for guest in room_number:
        visit = [guest]
        while guest in occupied_rooms:
            guest = occupied_rooms[guest]
            visit.append(guest)
        answer.append(guest)
        for i in visit: occupied_rooms[i] = guest + 1
    return answer
        

print(solution(10, [1,3,4,1,3,1]))
