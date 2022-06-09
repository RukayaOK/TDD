# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def convertnumber(input):
    if input in range(1, 5):
        return ''.join([char*len(input) for char in input])
    elif input == 5:
        return 'V'
    elif input == 10:
        return 'X'
    elif input == 50:
        return 'L'
    elif input == 100:
        return 'C'
    elif input == 500:
        return 'D'
    elif input == 1000:
        return 'M'




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    output = convertnumber(1)
    print(output)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
