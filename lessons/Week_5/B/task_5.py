def three_sum(items: list, target: int) -> list:
    items.sort()
    options = []

    for i in range(len(items)-2):
        left, right = i + 1, len(items) - 1

        while left < right:
            sum_of_indexes = items[i] + items[left] + items[right]
           
            if sum_of_indexes == target:
                options.append((items[i], items[left], items[right]))
            
            if sum_of_indexes < target:
                left += 1
                continue
            
            right -= 1

    return options

print(three_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 12))
