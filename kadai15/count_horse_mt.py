from collections import defaultdict
from glob import glob
from time import time, sleep
import pickle
from pprint import pprint
import threading


def file_open(file_path, ddct,lck):
    
    print(f"処理中：{file_path}")
    with open(file_path, "rb") as rfo:
        pkl = pickle.load(rfo)
    lck.acquire()
    for horse_name in pkl["h_name"].values():
        
        ddct[horse_name] += 1
    lck.release()
    sleep(0.5)
    
    


if __name__ == "__main__":
    bgn = time()
    names = defaultdict(int)
    files = glob("data/netkeiba/*.pkl")
    lck = threading.Lock()
    print(f"{len(files)}ファイル")
    for file_path in files:
        th = threading.Thread(target=file_open,args=(file_path,names,lck))
        #file_open(file_path, names,lck)
        th.start()
    for th in threading.enumerate():
        if th.name == "MainThread":
            continue
        th.join()
    end = time()
    print(f"累積時間：{end-bgn:.2f}秒")
    sorted_lst = sorted(names.items(), key=lambda tpl:tpl[1], reverse=True)
    pprint(sorted_lst[:10])