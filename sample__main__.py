from sample__name__ import cool_func
# cool.py 中的主程式在被引用的時候也被執行了
print('Call it remotely')
cool_func()
print('__name__:', __name__)

