from itertools import combinations

class Person:
    def __init__(self, x, y, place):
        self.x = x
        self.y = y
        self.place = place
    def check_sd(self, Person):
        distance = abs(self.x - Person.x) + abs(self.y - Person.y)
        if distance == 1: return False
        elif distance == 2:
            self.dx = self.x - Person.x
            self.dy = self.y - Person.y
            if self.dx * self.dy == 0: return True if self.place[int((self.y + Person.y)/2)][int((self.x + Person.x)/2)] == 'X' else False
            else: return True if self.place[self.y][self.x - self.dx] == 'X' and self.place[self.y - self.dy][self.x] == 'X' else False
        else: return True

def solution(places):
    result = []
    for place in places:
        people = []
        result_temp = 1
        for row in list(enumerate(place)):  
            for is_person in list(enumerate(row[1])):
                if is_person[1] == 'P':
                    people.append(Person(is_person[0], row[0], place))
        combination = list(combinations(people, 2))
        for pair in combination:
            if not pair[0].check_sd(pair[1]):
                result_temp *= 0
                break
        result.append(result_temp)
    return(result)