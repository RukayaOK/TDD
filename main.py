# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

keys = {
    5: 'V',
    10: 'X'
}

def convertnumber(input):
   output = ""

   for key, value in keys.items():

    while len(output) == 0:
       if input == key - 1:
           output = 'I' + value
       elif input < 5:
           output = 'I'*input
       elif input == key:
           output = value
       elif input > 5:
            output = value + 'I'*(input-5)
       else:
           "not handled"


    return input, output


results = convertnumber(1)
print(f'input: {results[0]} and output: {results[1]}')
results = convertnumber(2)
print(f'input: {results[0]} and output: {results[1]}')
results = convertnumber(3)
print(f'input: {results[0]} and output: {results[1]}')
results = convertnumber(4)
print(f'input: {results[0]} and output: {results[1]}')
results = convertnumber(5)
print(f'input: {results[0]} and output: {results[1]}')
results = convertnumber(6)
print(f'input: {results[0]} and output: {results[1]}')
results = convertnumber(7)
print(f'input: {results[0]} and output: {results[1]}')
results = convertnumber(8)
print(f'input: {results[0]} and output: {results[1]}')
results = convertnumber(9)
print(f'input: {results[0]} and output: {results[1]}')





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
