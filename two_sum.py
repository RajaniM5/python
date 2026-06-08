def two_sum():
    nums = [4,3,2,0,0,2, 3, 11, 15]
    target = 9
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
  


def main():
    result = two_sum()
    print(f"Indices of the two numbers that add up to the target: {result}")

if __name__ == "__main__":
    main()