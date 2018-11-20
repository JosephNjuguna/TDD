def my_sort(numbers):
    odd_numbers = sorted([x for x in numbers if x%2 == 1 ])
    even_numbers =  sorted([x for x in numbers if x%2 == 0])
    return odd_numbers+ even_numbers
