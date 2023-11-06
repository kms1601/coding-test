def solution(stones, k):
    left, right = 0, 200000000
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        max_jump = 0
        jump = 0
        
        for stone in stones:
            if stone - mid <= 0:
                jump += 1
                if max_jump < jump:
                    max_jump = jump
            else: jump = 0
            
            if max_jump > k: break
        print(mid, max_jump)
        
        if max_jump == k:
            answer = mid
        elif max_jump < k:
            left = mid + 1
        elif max_jump > k:
            right = mid - 1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))