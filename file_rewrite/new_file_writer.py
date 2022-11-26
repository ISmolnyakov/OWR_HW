first = open('1.txt', encoding='utf-8')
second = open('2.txt', encoding='utf-8')
third = open('3.txt', encoding='utf-8')
forth = open('4.txt', encoding='utf-8')

f_list = [first, second, third, forth]
file_info = []


def sort_file_list(file_list):
    for data in file_list:
        lines_count = sum(1 for line in data)
        data_list = []
        data_list.append(lines_count)
        data_list.append(data.name)
        file_info.append(data_list)
    file_info.sort()
    return file_info


def write_file(info):
    with open('resulting_file.txt', 'w', encoding='utf-8') as result:
        for items in info:
            result.write(f'{items[1]}\n{items[0]}\n') # вот тут получается в цикле нужно дописывать содержание текущего
                                                      # элемента списка, который в items, но как сделать в f-строке
                                                      # прочитать содержимое файла? сделать items[1].read() ведь нельзя?

sort_file_list(f_list)
write_file(file_info)
print(first.read()) #после выполнения функции sort_file_list(f_list) данный принт выводит пустую строку
                    #есть sort_file_list(f_list) убрать, то нормально выводится весть текст файла
                    #

print(file_info)
log = open('resulting_file.txt', encoding='utf-8')
print(log.read())