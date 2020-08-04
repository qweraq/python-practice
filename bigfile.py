import os


def get_big_file(path, filesize):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            target_file = os.path.join(dirpath, filename)
            if not os.path.isfile(target_file):
                continue
            size = os.path.getsize(target_file)
            if size > filesize:
                size = size//(1024 * 1024)
                size = '{size}M'.format(size=size)
                print(target_file, size)


if __name__ == '__main__':
    get_big_file('/home/zmq', 100*1024*1024)
