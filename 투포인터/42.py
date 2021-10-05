def trap(self, height: List[int]) -> int:
    if not height:
        return 0

    answer = 0
    left, right = 0, len(height) - 1
    maxLeft, maxRight = height[left], height[right]

    while left < right:
        if maxLeft <= maxRight:
            left += 1
            maxLeft = max(maxLeft, height[left])
            answer += maxLeft - height[left]
        else:
            right -= 1
            maxRight = max(maxRight, height[right])
            answer += maxRight - height[right]
    return answer
