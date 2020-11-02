"""

base10 = (user input)
target_base = (user input)

Require that the base is positive
and less than 63

if target_base is 1, return "1" repeated base10 times

else if base10 is 0, return 0

else

    q = base10
    output

    while q is not zero

        p = q % target_base
        output = (digit for p) + output
        q = floor(q / target_base)

    end while

    print output

end if

"""

import sys

base10 = int(input("Enter number: "))
target_base = int(input("Enter base: "))

if target_base < 1:
    print("Base must be positive")
    sys.exit(1)

# I'm not sure what the standard representation
# for digits beyond the 62nd, so am not supporting
# them for now.
if target_base > 62:
    print("62 is the largest supported base")
    sys.exit(1)

if target_base == 1:

    # The method of quotient and remainders
    # goes nowhere if the target base is one, 
    # so we treat this separately
    print("1"*base10)

elif base10 == 0:

    # 0 is always zero except in the unary case,
    # where it is the lack of any ones
    print("0")

else:

    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    q = base10
    output = ""

    while q != 0:
        p = q % target_base
        output = chars[p] + output
        q = q // target_base

    print(output)