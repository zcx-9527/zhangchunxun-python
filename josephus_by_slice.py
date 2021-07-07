#约瑟夫环问题#

def josephus_by_slice(n,m):
    list = [x for x in range(1,n+1)]
    key = m-1
    print(list)
#如果n或m等于1.直接返回列表的最后一位
    if n == 1 or m == 1:
        return list[-1]
    
    while True:
#当m<列表长度,直接切片
        if m < len(list):
            print(list[key])
            list = list[key+1:] + list[:key]
            print(list)
#当m=列表长度，去掉列表的最后一位
        if m == len(list):
            list.pop(-1)
            print(list)

        if m > len(list):
            if len(list) == 1:
                return list[0]
#当 m>m时，取余数
            s=m%len(list)
            list = list[s:] + list[:s-1]
            print(list)

if __name__ == '__main__':
    n,m=10,3
    print(josephus_by_slice(n,m))