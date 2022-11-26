class Files:
    def __init__(self, item):
        self.item = item

    def count_lines(self):
        lines_count = sum(1 for line in open(self.item))
        return lines_count

    def __gt__(self, other):
        return self.count_lines() > other.count_lines()

    def write_file(self, other):
        with open('new_result.txt', 'w', encoding='utf-8') as result, open(self.item, encoding='utf-8') as first_file, \
                open(other.item, encoding='utf-8') as second_file:
            if Files.__gt__(self, other):
                result.write(f'{second_file.name}\n{other.count_lines()}\n{second_file.read()}\n')
                result.write(f'---------\n')
                result.write(f'{first_file.name}\n{self.count_lines()}\n{first_file.read()}')
            else:
                result.write(f'{first_file.name}\n{self.count_lines()}\n{first_file.read()}\n')
                result.write(f'---------\n')
                result.write(f'{second_file.name}\n{other.count_lines()}\n{second_file.read()}')
            first_file.close()
            second_file.close()
            result.close()


first = Files('1.txt')
second = Files('2.txt')
third = Files('3.txt')
forth = Files('4.txt')
first.write_file(forth)

# third.write_file(first)
# forth.write_file(second)
log = open('new_result.txt', encoding='utf-8')
print(log.read())
