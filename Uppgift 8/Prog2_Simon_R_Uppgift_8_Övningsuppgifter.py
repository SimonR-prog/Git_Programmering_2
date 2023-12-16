# https://christianaberg.files.wordpress.com/2020/07/dva128___kompendium.pdf

# 14.1:

"""Make function that, based on input, turns km into miles and vice versa."""

def transfer(amount, string):
    if string.lower() == "miles":
        return int(amount) * 1.609344
    elif string.lower() == "km":
        return int(amount) * 0.621371192
    else:
        print("Invalid input.")

transform = input("Amount and current measurement. > ")
x = transform.split()

print(transfer(x[0],x[1]))


# 1.609344 miles to km
# 0.621371192 km to miles


