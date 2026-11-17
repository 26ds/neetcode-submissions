class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = []
        start_index = 0
        start = numbers[start_index]
        end_index = len(numbers)-1
        end = numbers[end_index]
        while start +end != target:
            if start +end < target:
                start_index = start_index+1
                start = numbers[start_index]
            if start +end > target:
                end_index = end_index -1
                end = numbers[end_index]
        answer.append(start_index+1) 
        answer.append(end_index+1) 
        return answer
