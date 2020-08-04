#该代码未能在windows10系统运行成功，估计是路径格式问题
import os


def get_big_file(path, filesize):
    for dirpath, dirnames, filenames in os.walk(path):  #遍历文件
        for filename in filenames:
            target_file = os.path.join(dirpath, filename)
            if not os.path.isfile(target_file):  #排除非文件类型
                continue
            size = os.path.getsize(target_file)
            if size > filesize:
                size = size//(1024 * 1024)  #转换文件大小的格式
                size = '{size}M'.format(size=size)
                print(target_file, size)


if __name__ == '__main__':
    get_big_file('/home/zmq', 100*1024*1024)  #输入路径和文件大小并打印文件路径和文件大小
