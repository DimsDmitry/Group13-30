# напиши код для выполнения заданий здесь
# задание 1
count = 0
with open('my_file.txt', 'r') as file:
    for string in file:
        string_list = string.split(' ')
        #print(string_list)
        for symbol in string_list:
            if int(symbol) == 1:
                count += 1
print('В файле содержится', count, 'единиц')

# задание 2
with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    second_line = lines[13].split(' ')
    elem = int(second_line[7])
    print(elem)
