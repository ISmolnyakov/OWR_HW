# file_obj = open("result.txt", 'rb', encoding='utf-8')

class Files:
    def __init__(self, item):
        self.item = item

    def count_lines(self):
        lines_count = sum(1 for line in open(self.item))
        return lines_count

    def __gt__(self, other):
        return self.count_lines() > other.count_lines()

    def __lt__(self, other):
        return self.count_lines() < other.count_lines()

    def write_file(self, other):
        with open('new_result.txt', 'w', encoding='utf-8') as result, open(self.item, encoding='utf-8') as first, \
                open(other.item, encoding='utf-8') as second:
            if Files.__lt__:
                result.write(f'{second.name}\n{other.count_lines()}\n{second.read()}\n')
                result.write(f'\n')
                result.write(f'{first.name}\n{self.count_lines()}\n{first.read()}\n')
            else:
                result.write(f'{first.name}\n{self.count_lines()}\n{first.read()}\n')
                result.write(f'\n')
                result.write(f'{second.name}\n{other.count_lines()}\n{second.read()}\n')
            first.close()
            second.close()
            result.close()

    # if file_one > file_two:
    #     with open('new_result.txt', 'a', encoding='utf-8') as result:
    #         result.write(f'{file_one.file}\n{file_one.count_lines()}\n{file_one.read()}')
    #         result.write(f'{file_two.file}\n{file_two.count_lines()}\n{file_two.read()}')
    # else:
    #     with open('new_result.txt', 'a', encoding='utf-8') as result:
    #         result.write(f'{file_two.file}\n{file_two.count_lines()}\n{file_two.read()}')
    #         result.write(f'{file_one.file}\n{file_one.count_lines()}\n{file_one.read()}')
    # return


first = Files('1.txt')
second = Files('2.txt')
first.count_lines()
second.count_lines()

first.write_file(second)
log = open('new_result.txt', encoding='utf-8')
print(first.__gt__(second))
print(log.read())

# print(f"Number of lines in {first.file} {'>' if first.count_lines() > second.count_lines() else '<'} "
#       f"than in {second.file} and equal to { {first.count_lines()} if first.count_lines() > second.count_lines() else second.count_lines() } lines")









