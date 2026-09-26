#write a python program to  Check if a number is an Armstrong number using recursion
def is_armstrong(n):
    def get_digits_and_len(num):
        if num == 0: return []
        return get_digits_and_len(num // 10) + [num % 10]
    digits = get_digits_and_len(n)
    length = len(digits)
    def sum_powers(digits_list, power):
        if not digits_list:
            return 0
        return (digits_list[0] ** power) + sum_powers(digits_list[1:], power)    
    return n == sum_powers(digits, length)
print(153, is_armstrong(153))
print(53, is_armstrong(53))
                                                                    