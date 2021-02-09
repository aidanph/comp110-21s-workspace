"""An exercise in remainders and boolean logic."""

__author__ = "730400485"


# Begin your solution here...

n = int(input("Enter an int: "))
if (n % 2) == 0 and (n % 7) == 0:
    print("TAR HEELS")
else:
    if (n % 7) == 0:
        print("HEELS")
    else:
        if (n % 2) == 0:
            print ("TAR")
        else:
            print("CAROLINA")