import os

path = '../file_rewrite'


def rewrite_file(path):
    file_list = os.listdir(path)
    info = {}
    for content in file_list:
        if content.rfind('.txt', -4) >= 0:
            with open(os.path.join(path, content), 'r', encoding='utf-8') as file:
                info[content] = file.readlines()

    with open('../file_rewrite/resulting_file.txt', 'w', encoding='utf-8') as file:
        for file_name, rows in sorted(info.items(), key=lambda x: len(x[1])):
            file.write(file_name + '\n')
            file.write(str(len(rows)) + '\n')
            if '\n' not in rows[-1]:
                rows[-1] += '\n'
                file.write(''.join(rows))


rewrite_file(path)
log = open('../file_rewrite/resulting_file.txt', encoding='utf-8')
print(log.read())
