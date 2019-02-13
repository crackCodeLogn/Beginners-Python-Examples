import Gcd


def find_lcm(first, second):
    """
    Recursive function to find lcm of two numbers

    The formula used => first * second = gcd * lcm
                     => lcm = (first * second) / gcd(first, second)

    :param first: first number
    :param second: second number
    :return: LCM
    """
    return int((first * second) / Gcd.gcd(first, second))


if __name__ == "__main__":
    # Main code
    while True:
        startOrEnd = str(input('Count lcm or End : '))
        if startOrEnd == 'Count lcm':
            first = int(input('First num : '))
            second = int(input('Second num : '))
            if first > second:
                first, second = second, first
            print("LCM : " + str(find_lcm(first, second)))
        else:
            quit()
