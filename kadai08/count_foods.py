from collections import defaultdict
import sys
from pprint import pprint 

def read_foods(file_path):
    lst = list()
    with open(file_path, "r", encoding="utf-8") as rfo:
        for row in rfo:
            name, cate, make, brnd, date, prce = row.rstrip().split("\t")
            lst.append((make, brnd))
    return lst


if __name__ == "__main__":
    maker_brand_lst = read_foods(sys.argv[1])
 
    maker_brand_dict = defaultdict(lambda :defaultdict(int))
    for maker in maker_brand_lst:
        a = maker[0]
        b = maker[1]
        maker_brand_dict[a][b] += 1
    memo_dic = {}

    dic2 =sorted(({(f,t):v for f, dct in maker_brand_dict.items() for t, v in dct.items()}.items()), 
       key=lambda tpl:tpl[0], 
        reverse=True)

    for i, wow in enumerate(dic2):
        if wow[0][0] not in  memo_dic:
            memo_dic[wow[0][0]] = wow[1]
        else:
            memo_dic[wow[0][0]] += wow[1]
    sortdic = (sorted(memo_dic.items(),key=lambda x:x[1],reverse=True))
    count = 0
    top10_maker   = []
    top5_bra = []
    for l in  sortdic :
        search = sorted(maker_brand_dict[l[0]].items(),key=lambda x:x[1],reverse=True)
        top10_maker.append(l[0])
        count += 1
        nyan = 0
        memo = []
        for m in search:
            
            memo.append([m[0],m[1]])
            nyan += 1
            if nyan == 5:
                break
        top5_bra.append(memo)
        if count == 10:
            break
    for o in top10_maker:
        print(o) 
    for p in top5_bra:
        for q in p:
            print(q[0],q[1])
    range_counter = 0
    for r in top10_maker:
        for s in top5_bra[range_counter]:
            print(r,s[0],s[1])
        range_counter += 1