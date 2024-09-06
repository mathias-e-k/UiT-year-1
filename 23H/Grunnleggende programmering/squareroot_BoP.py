
def guess(A, d):
    return A - d//2

def newtons_sqrt(x0: int, S: int) -> int:
    """Takes an initial guess x0 and a number S and finds the square root of S using newtons method."""
    iterations = 0
    xn = round(x0)
    S = round(S)
    previous = -1

    while xn != previous:
        print(f"x{iterations}: {xn}")

        previous = xn
        xn = xn - (xn*xn - S) // (2*xn)

        iterations += 1

    print(f"x{iterations}: {xn}")
    print(f"found square root in {iterations} iterations")
    return xn


if __name__ == "__main__":
    distance = int(input("Avstand: "))
    vertical_distance = int(input("Dybde: "))

    x0 = guess(distance, vertical_distance)
    horizontal_distance_squared = distance*distance - vertical_distance*vertical_distance
    horizontal_distance = newtons_sqrt(x0, horizontal_distance_squared)


    print(f"Horisontal avstand er {horizontal_distance}")


