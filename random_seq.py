#第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？#

import random
SEQ='qwewrwqsdazcherw012356789'
SEQ_LEN=len(SEQ)-1

def generate_random_seq(len=5):
    random_seq=''
    for j in range(len):
        index=random.randint(0,SEQ_LEN)
        random_seq+=SEQ[index]
    print(random_seq)
    return random_seq

def number_of_random_seq(number,len):
    total_random_seq=[]
    for i in range(number):
        random_seq=generate_random_seq(len)
        total_random_seq.append(random_seq)
    return total_random_seq


if __name__ == '__main__':
    number=200
    len=5
    total_random_seq=number_of_random_seq(number,len)
    print(total_random_seq)