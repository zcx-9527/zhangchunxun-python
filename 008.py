#第 0008 题： 一个HTML文件，找出里面的正文#


from bs4 import BeautifulSoup

with open(r"..\test_html\test_1.html", "r", encoding="utf-8") as f:

    file_of_html = f.read()
    # 使用 beautifulsoup 解析功能，解析器使用lxml
    soup = BeautifulSoup(file_of_html, "html.parser")
    # 输出标题
    print(soup.title)
    # 输出p标签的内容
    print(soup.p)
    # 输出a连接
    print(soup.a)
    # 输出body标签的内容即正文
    print(soup.find_all("body"))
    # 输出整个文件
    print(soup.get_text)