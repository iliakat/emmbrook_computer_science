def cel_to_far(temp):
    answ = round((temp * 9/5) + 32, 2)
    return f"\tYour answer:\n\t{temp} °C = {answ} °F"

def far_to_cel(temp):
    answ = round((temp - 32) * 5/9, 2)
    return f"\tYour answer:\n\t{temp} °F = {answ} °C"

def main():
    print('\n')
    temp_str = str(input('Enter yor temperature (20C/20 C): ')).split(' ')
    print('\n')
    if len(temp_str) == 2:
        if temp_str[-1].lower() == 'c':
            return cel_to_far(int(temp_str[0]))
        elif temp_str[-1].lower() == 'f':
            return far_to_cel(int(temp_str[0]))
        else: print('Error!\nPlease put text in correct format')
    elif len(temp_str) == 1:
        temp_str = temp_str[0]
        if temp_str[0].lower() == 'break' or temp_str[0].lower() == 'exit' or temp_str[0].lower() == 'stop':
            return 'break'
        elif temp_str[-1].lower() == 'c':
            return cel_to_far(int(temp_str[0:-1]))
        elif temp_str[-1].lower() == 'f':
            return far_to_cel(int(temp_str[0:-1]))
        else: print('Error!\nPlease put text in correct format')
    else: return 'Error!\nPlease put text in correct format'

if __name__ == '__main__':
    while True:
        output = main()
        if output == 'break':
            print('\tThank you for using my calculator.\n\tBye!')
        else: print(output)