import tinify
import os
tinify.key = "YOUR_API_KEY"


def tinify_all_pic(rootdir):
    _files = []
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isdir(path):
            tinify_all_pic(path)
        if os.path.isfile(path):
            suffix = os.path.splitext(path)[-1]
            if suffix == '.png' or suffix == '.jpg':
                print(path)
                source = tinify.from_file(path)
                source.to_file(path)


tinify_all_pic(r"themes\hexo-theme-matery\source")
