import time
from typing import List
from tabulate import tabulate

class Solution:
    def containsDuplicateBruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplicateSort(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    def containsDuplicateHashMap(self, nums: List[int]) -> bool:
        hashmap = {}

        for i, num in enumerate(nums):
            if num in hashmap:
                return True
            hashmap[num] = i
        
        return False

    def containsDuplicateSet(self, nums: List[int]) -> bool:
        numSet = set()

        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        
        return False

def run_test_cases():
    test_cases = [
    list(range(1, 1001)),                             # No duplicates, range from 1 to 1000
    list(range(1, 501)) + list(range(1, 500)),        # Contains duplicate, range from 1 to 500 repeated
    list(range(1, 501)) + [0] + list(range(2, 500))   # Contains duplicate, range from 1 to 500 with 0 inserted
]
    
    s = Solution()
    results = []

    for i, test in enumerate(test_cases):
        # Brute Force Solution
        start_time = time.time()
        result_bf = s.containsDuplicateBruteForce(test)
        end_time = time.time()
        time_bf = (end_time - start_time) * 1000

        # Sort Solution
        start_time = time.time()
        result_sort = s.containsDuplicateSort(test)
        end_time = time.time()
        time_sort = (end_time - start_time) * 1000

        # Hash Map Solution
        start_time = time.time()
        result_hm = s.containsDuplicateHashMap(test)
        end_time = time.time()
        time_hm = (end_time - start_time) * 1000

        # Set Solution
        start_time = time.time()
        result_set = s.containsDuplicateSet(test)
        end_time = time.time()
        time_set = (end_time - start_time) * 1000

        # Determine the fastest solution
        times = {'BruteForce': time_bf, 'Sort': time_sort, 'HashMap': time_hm, 'Set': time_set}
        fastest_solution = min(times, key=times.get)


        results.append([f'Test case {i + 1}', result_bf, result_sort, result_hm, result_set, time_bf, time_sort, time_hm, time_set, fastest_solution])

    headers = ['Test Case', 'BruteForce Result', 'Sort Result', 'HashMap Result', 'Set Result', 'BruteForce Time (ms)', 'Sort Time (ms)', 'HashMap Time (ms)', 'Set Time (ms)', 'Fastest Solution']
    print(tabulate(results, headers=headers, tablefmt='grid'))

if __name__ == "__main__":
    run_test_cases()