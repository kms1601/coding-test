from itertools import combinations

def get_intersection(line1, line2): #교점 구하는 함수
    
    if not (line1[0]*line2[1]-line1[1]*line2[0]): return False  #AD-BC가 0일 때
    
    x = (line1[1]*line2[2]-line1[2]*line2[1])/(line1[0]*line2[1]-line1[1]*line2[0])
    y = (line1[2]*line2[0]-line1[0]*line2[2])/(line1[0]*line2[1]-line1[1]*line2[0])
    
    if not x.is_integer() or not y.is_integer(): return False   #정수가 아닐 때
    return (int(x), int(y))

def solution(line):
    intersections = set()   #교점 집합
    x_min = y_min = int(1e20)
    x_max = y_max = -int(1e20)
    draw = answer = []   #결과
    
    line_combinations = combinations(line, 2)   #직선 조합 생성

    for line_combination in line_combinations:   #직선 조합의 교점 구하기
        intersection = get_intersection(line_combination[0],line_combination[1])
        
        if intersection: intersections.add(intersection)    #정수 교점이라면 교점 집합에 추가
            
    for x, y in intersections:  #그림의 최소 크기 구하기
        if x < x_min: x_min = x
        if y < y_min: y_min = y
        if x > x_max: x_max = x
        if y > y_max: y_max = y
    
    draw = [['.']*(x_max-x_min+1) for _ in range(y_max-y_min+1)]    #빈 그림 생성
    
    for x, y in intersections:  #그리기
        x_star = x + abs(x_min) if x_min < 0 else x - x_min
        y_star = y + abs(y_min) if y_min < 0 else y - y_min
        draw[y_star][x_star] = '*'
    
    for i in draw: answer.append(''.join(i))    #리스트를 문자열로 변환
    
    return answer[::-1]     #위 아래 뒤집어서 반환