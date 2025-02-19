
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    """
    Calculate the square root of a non-negative number using the bisection method.

    This function attempts to find the square root of `square_target` by iteratively
    narrowing down the interval in which the square root lies using the bisection method.
    The process continues until the difference between the square of the midpoint and
    `square_target` is within `tolerance` or until `max_iterations` is reached.

    Parameters:
    square_target (float): The number to find the square root of. Must be non-negative.
    tolerance (float): The precision tolerance of the result. Default is 1e-7.
    max_iterations (int): The maximum number of iterations to perform. Default is 100.

    Returns:
    float: The approximate square root of `square_target`.

    Raises:
    ValueError: If `square_target` is negative.

    Note:
    The function prints the result or a failure message if the solution does not converge
    within the specified number of iterations.
    """

    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {round(root, 1)}')
    
    return root

n = float(input("Enter a number: "))

square_root_bisection(n)