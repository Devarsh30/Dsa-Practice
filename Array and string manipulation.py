# Reverse Array (Two Pointer)
arr = [1,2,3,4,5]

l, r = 0, len(arr)-1

while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1

print(arr)



#Find Largest Element
arr = [10, 20, 5, 8]

max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num

print(max_val)



# Rotate an Array by d - Counterclockwise or Left
def leftRotate(arr, d):
    n = len(arr)
    d = d % n   # handle d > n
    return arr[d:] + arr[:d]

arr = [1, 2, 3, 4, 5, 6]
d = 2
print(leftRotate(arr, d))



# Missing and Repeating in an Array
def findNumbers(arr):
    n = len(arr)
    freq = [0] * (n + 1)

    for num in arr:
        freq[num] += 1

    repeating = -1
    missing = -1

    for i in range(1, n + 1):
        if freq[i] == 2:
            repeating = i
        elif freq[i] == 0:
            missing = i

    return [repeating, missing]

print(findNumbers([3, 1, 3]))          
print(findNumbers([4, 3, 6, 2, 1, 1]))


# Missing ranges of numbers
def missing_ranges(arr, lower, upper):
    result = []
    
    prev = lower - 1
    
    # loop till len(arr) + 1 to handle upper
    for i in range(len(arr) + 1):
        
        if i < len(arr):
            curr = arr[i]
        else:
            curr = upper + 1
        
        # check if gap exists
        if curr - prev >= 2:
            result.append([prev + 1, curr - 1])
        
        prev = curr
    
    return result

arr = [14, 15, 20, 30, 31, 45]
lower = 10
upper = 50

print(missing_ranges(arr, lower, upper))


def combine_strings(a, b):
    # Step 1: find shorter and longer
    if len(a) < len(b):
        short = a
        long = b
    else:
        short = b
        long = a
    
    # Step 2: combine
    return short + long + short


#  Problem:
# Given an array, return indices of two numbers that add up to target.
# Example:
# Input: nums = [2,7,11,15], target = 9  
# Output: [0,1]
# Approach:
# Use hashmap (dictionary)
# Store number → index
# Check if (target - current) exists
def two_sum(nums, target):
    seen = {}
    
    for i in range(len(nums)):
        diff = target - nums[i]
        
        if diff in seen:
            return [seen[diff], i]
        
        seen[nums[i]] = i

# CALL FUNCTION
result = two_sum([2, 7, 11, 15], 9)

# PRINT OUTPUT
print(result)

# Complexity:
# Time: O(n)
# Space: O(n)


# Longest Substring Without Repeating Characters
# Problem:
# Find length of longest substring with all unique characters.
#  Example:
# Input: "abcabcbb"  
# Output: 3 ("abc")
# Approach:
# Use sliding window + set
# Expand window, shrink when duplicate appears
def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
# CALL + PRINT
print("Longest Substring Length:", longest_substring("abcabcbb"))
# Complexity:
# Time: O(n)
# Space: O(n)




# Valid Anagram
# Problem:
# Check if two strings are anagrams.
#  Example:
# Input: s = "listen", t = "silent"  
# Output: True
#  Approach:
# Count characters OR sort
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True
# CALL + PRINT
print("Is Anagram:", is_anagram("listen", "silent")) 
# Complexity:
# Time: O(n)
# Space: O(n)



# Reverse Words in a String
#  Problem:
# Reverse order of words (not characters).
# Example:
# Input: "the sky is blue"  
# Output: "blue is sky the"
#  Approach:
# Split → Reverse → Join

def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)

# CALL + PRINT
print("Reversed Sentence:", reverse_words("the sky is blue"))

# Complexity:
# Time: O(n)


# Two Sum (Hash Map)
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
result = two_sum([2, 7, 11, 15], 9)
print(result)
# Time Complexity = O(n)
