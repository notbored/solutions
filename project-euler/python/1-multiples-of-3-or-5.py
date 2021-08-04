"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

(Number A is a multiple of Number B if: A % B == 0)
"""

# First attempt
# for i in range(1001):
#     if i % 5 == 0 or i % 3 == 0:
#         print(i)

# Second attempt: turn into a reusable function
def get_multiples(_factors, _range):
    """
    Will print out all multiples of the integers in list "_factors" within
    the range of "_range".

    Example: get_multiples([3,5],1000)
    """
    for n in range(_range):
        for f in _factors:
            if n % f == 0:
                print(i)


get_multiples([3,5],1000)
