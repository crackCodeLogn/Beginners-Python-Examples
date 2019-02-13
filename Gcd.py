# @author Vivek
# @version 1.0
# @since 13-02-2019

def gcd(a, b):
    """
    Recursive function for getting the gcd ~ greatest common divisor OR the highest common factor (HCF)
    :param a: the divisor
    :param b: the dividend
    :return:  the gcd
    """
    mod = b % a
    if mod == 0:
        return a
    return gcd(mod, a)


if __name__ == '__main__':
    print("Enter -1 in either of numbers to quit!")
    while True:
        first = int(input('First num : '))
        second = int(input('Second num : '))

        if first == -1 or second == -1:
            quit()

        # swapping numbers if the first number is larger than second number
        if first > second:
            first, second = second, first

        print("GCD : " + str(gcd(first, second)))
