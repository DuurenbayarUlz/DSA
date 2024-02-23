import time
from typing import List
from tabulate import tabulate

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Understanding the problem
            # Can you rephrase the problem in your own words?
            # Can you give me an example of anagram words?
        
        # Input and output
            # What is the input of the function?
            # What is the output of the function?  
            # Can you provide some example inputs and their corresponding outputs?
        
        # Clarifying the doubts
            # Are there any edge cases that I need to be aware of?
            # What happens if the input array is empty?

        # Solving the problem
            # Step 1: Sorting the strings in the str array
            # Step 2: Use hashmap to store each string values with sorted keys
            # Step 3: Return the hashmap.values in an array
        
        # Complexity analysis
            # Time Complexity: O(n * mlog(m)) --> O(n) where "n" is the number of items in strs array, "m" is the average number of character in each item
            # Space Complexity: O(n)

        hashmap = {}
        
        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s in hashmap:
                hashmap[sorted_s].append(s)
            else:
                hashmap[sorted_s] = [s]

        return list(hashmap.values())

def run_test_cases():
    test_cases = [
        ["eat","tea","tan","ate","nat","bat"],
        ["eat","tea","tan","nat","bat", "a", "abc", "def"],
        ["a"],
        [""],
    ]
    
    s = Solution()
    results = []

    for i, test in enumerate(test_cases):
        
        # Hash Map Solution
        start_time = time.time()
        result_hm = s.groupAnagrams(test)
        end_time = time.time()
        time_hm = (end_time - start_time) * 1000


        results.append([f'Test case {i + 1}', result_hm, time_hm])

    headers = ['Test Case', 'HashMap Result', 'HashMap Time (ms)']
    print(tabulate(results, headers=headers, tablefmt='grid'))

if __name__ == "__main__":
    run_test_cases()