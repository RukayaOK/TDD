# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

keys = {
    5: 'V',
    10: 'X',
    15: 'XV',
    20: 'XX'
}

def convertnumber(input):
   output = ""

   for key, value in keys.items():
       if input == key:
           output = value
       elif input == key - 1:
           output = 'I' + value
       elif input in range(1, 5):
           output = 'I'*input
       elif input in range(5, 10):
            output = value + 'I'*(input-5)
       elif input in range(10, 15):
           output = value + 'I'*(input-10)
       elif input in range(16, 20):
           output = value + 'I'*(input-15)
       else:
           "not handled"

   return input, output


for i in range(1,21):
    results = convertnumber(i)
    print(f'input: {results[0]} and output: {results[1]}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
