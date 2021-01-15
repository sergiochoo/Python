# МФУ kyocera для каждого сканирования создает папку и кладет в нее файл scan.tif
# при сканировании фотоальбома получается огромное количество папок, в каждом из которых
# содержится файл scan.tif
# данный скрипт позволяет упорядочить все файлы в одном каталоге

import os
import shutil

dir_src = "/Users/sergiochoo/Pictures/Source"
dir_dst = "/Users/sergiochoo/Pictures/Scans"

i = 1

for dirname in os.listdir(dir_src):
    dirpath = os.path.join(dir_src, dirname)
    if not os.path.isdir(dirpath):
        continue
    for filename in os.listdir(dirpath):
        if filename == "scan.tif":
            src_file = os.path.join(dirpath, filename)
            dst_file = os.path.join(dir_dst, f"scan_{i:03}.tif")
            print("src_file: ", src_file)
            print("dst_file: ", dst_file)
            shutil.copyfile(src_file, dst_file)
            i += 1