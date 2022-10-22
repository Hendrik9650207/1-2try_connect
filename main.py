import requests
from bs4 import BeautifulSoup


def main():
    url1 = 'http://blog.castman.net/web-crawler-tutorial/ch1/connect.html'
    bad_url = 'http://non-existed.domain/connect.html'
    text1 = get_tag_text(url1, 'h1')
    print(text1)
    text2 = get_tag_text(url1, 'h2')
    print(text2)


def get_tag_text(url, tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup.find(tag).text
    except Exception as e:
        print('Exception: %s' % e)
    return None


'''
https://medium.com/pycone/7bf6b9b8244b
當 Python 檔案（模組、module）被引用的時候，檔案內的每一行都會被 Python 直譯器讀取並執行
Python 直譯器執行程式碼時，有一些內建、隱含的變數，__name__就是其中之一，其意義是「模組名稱」。
如果該檔案是被引用，其值會是模組名稱；但若該檔案是(透過命令列)直接執行，其值會是 “__main__”。

要怎麼讓檔案在被引用時，不該執行的程式碼不被執行？當然就是靠 __name__ == “__main__”做判斷！

之所以常看見這樣的寫法，是因為該程式可能有「單獨執行」（例如執行一些本身的單元測試）與「被引用」兩種情況，因此用上述判斷就可以將這兩種情況區分出來。
'''
if __name__ == '__main__':
    main()
