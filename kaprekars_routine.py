
# Kaprekar's Routine (Recursive)

def kasperkars_routine_recursive(number: str, verbose=True, steps=0, seen=None):
    if seen is None:
        seen = set()

    # Pad to 4 digits with zeros
    number = number.zfill(4)

    # Base case: if all digits are the same
    if len(set(number)) == 1:
        if verbose:
            print(f"{number} will not reach 6174 (all digits are the same).")
        return False

    if number == '6174':
        if verbose:
            print(f"Reached 6174 in {steps} steps!")
        return True

    if number in seen:
        if verbose:
            print("Cycle detected. Aborting.")
        return False
    seen.add(number)

    digits = list(number)
    big = int("".join(sorted(digits, reverse=True)))
    small = int("".join(sorted(digits)))
    result = str(big - small).zfill(4)

    if verbose:
        print(f"{big} - {small} = {result}")

    return kasperkars_routine_recursive(result, verbose, steps + 1, seen)
