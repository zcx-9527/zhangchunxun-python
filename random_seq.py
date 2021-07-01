#第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？#

import random
seq='qwewrwqsdazcherw012356789'
seq_len=len(seq)-1

for i in range(2):
    random_seq=''
    for j in range(5):
        index=random.randint(0,seq_len)
        random_seq+=seq[index]
    print(random_seq)