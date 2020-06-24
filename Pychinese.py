import sys
from library.base import th_list

print(th_list)


def translate(pyc, py):
    f = open(pyc, 'r', encoding='utf-8')
    f_new = open(py, 'w', encoding='utf-8')

    for line in f:
        for i in range(len(th_list)):
            if th_list[i] in line:
                line = line.replace(str(th_list[i]), "1")
        f_new.write(line)  # 将内容写入新文件中
    f.close()
    f_new.close()  # 关闭两个文件


if __name__ == '__main__':
    translate(str(sys.argv[1]), str(sys.argv[2]))
