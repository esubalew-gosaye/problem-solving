def swap_case(string):
    swapped = ""
    for chr in string:
        if chr.isalpha():
            swapped+=(chr.lower() if chr.isupper() else chr.upper())
        else:
          swapped += chr
    return swapped
