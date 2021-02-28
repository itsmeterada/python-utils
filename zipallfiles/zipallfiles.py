#
# Zip all files in the directory as an individual zip file.
#
import sys
import zipfile
from tqdm import tqdm
import multiprocessing
import glob
import pathlib
import time

def zip_file(filetozip):
    tmpname = pathlib.PurePath(filetozip).stem   # 拡張子を取り除く
    zipname = tmpname + '.zip'
    # print(zipname)
    # print(filetozip)
    with zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED) as myzip:
        myzip.write(filetozip)
    

if __name__ == '__main__':
    args = sys.argv
    if 1 == len(args):
        extension = "*"
    else:
        extension = args[1]

    files = list(glob.glob("*." + extension))
    to = len(files)
    print(to)

    start_time = time.time()
    numCpuCore = multiprocessing.cpu_count()
    print(numCpuCore)
    # numCpuCore = 1
    pool = multiprocessing.Pool(processes=numCpuCore)
    with tqdm(total=len(files)) as t:
        for _ in pool.imap_unordered(zip_file, files):
            t.update(1)
    elapse_time = time.time() - start_time
    print("Elapse time = {}".format(elapse_time))

# for file in files:
#     tmpname = pathlib.PurePath(file).stem   # 拡張子を取り除く
#     zipname = tmpname + '.zip'
#     with zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED) as myzip:
#         myzip.write(file)
#     print(zipname)
    




