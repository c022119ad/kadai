from functools import update_wrapper


# def memorize(func):
#     caldict = {}
#     def _func(*args):
#         if not num  in caldict:
#             res  =1
#             for n in range(1,num+1):
#                 res *= n
#             caldict[num] = res
#             print(f"{num}の階乗を計算しますあ",end="")
#             return res
#         else:
#             return caldict[num]
#     return _func

class memorize:
    def __init__(self,func):
        self.func = func
        self.dic = {}
        update_wrapper(self, self.func)
    
    def __call__(self,num):
        if not num in self.dic:
            res = self.func(num)
            # for n in range(1,num+1):
            #     res *=n
            self.dic[num]= res
            # print(f"{num}の階乗を計算しますい",end="")
            return res
        else:
            return self.dic[num]
        # return res

@memorize
def factorial(num):
    print(f"{num}の階乗を計算します：", end="")
    res = 1
    for n in range(1, num+1):
        res *= n
    return res



if __name__ == "__main__":
    lst = [3, 5, 2, 5, 4]
    for num in lst:
        print(factorial(num))