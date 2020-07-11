import sys
import os

from library.base import base_list
from library.base import th_list

# print(len(base_list))
# print(len(th_list))


def translate(pc):
    f = open(pc, 'r', encoding='utf-8')
    local = os.path.abspath(".") + "run.py"
    local = str(local)
    f_new = open(local, "w", encoding='utf-8')
    for line in f:
        for i in range(len(base_list)):
            if base_list[i] in line:
                line = line.replace(str(base_list[i]), str(th_list[i]))
        f_new.write(line)  # 将内容写入新文件中
    f.close()
    f_new.close()  # 关闭两个文件


def run():
    local = os.path.abspath(".") + "run.py"
    local = str(local)
    os.system(f"python3 {local}")
    # os.remove(local)


def index_error():
    print("请输入要执行的.pc文件！")


if __name__ == '__main__':
    try:
        translate(sys.argv[1])
        run()
    except IndexError:
        index_error()
