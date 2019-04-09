text = '''                       
The Zen of Python, by Tim Peters
美丽 is better than 丑陋.
清楚 is better than 含糊.
简单 is better than 复杂.
复杂 is better than 难懂.
单一 is better than 嵌套.
稀疏 is better than 稠密.
可读性计数.
Special cases aren't special enough to 打破规则.
即使练习会使得不再纯粹.
但错误不应该用沉默来掩盖.
Unless explicitly silenced.
面对起义，拒绝猜的诱惑.
有且只有一个办法.
Although that way may not be obvious at first unless you're Dutch.
尝试总比从未试过要强.
Although never is often better than *right* now.
如果执行很难被解释，那将是一个很糟的想法.
如果执行很容易解释，这会是一个好点子.
Namespaces are one honking great idea -- 让我们继续为之努力!
'''
import re
dictionary = {}
# 统计参数中每个英文单词出现的次数，最后返还一个按词频降序排列的数组
def stats_text_en(text):
    text=text.replace(',',' ').replace('.',' ').replace('*',' ').replace('--',' ')
    text1=text.split()
    for i in text1:
        dictionary.update({i:text1.count(i)})#通过key:计数函数来更新字典
    return dictionary

#打印统计英文词频的结果
print("统计英文词频的结果为:")
print(sorted(dictionary.items(),key=lambda x:x[1],reverse=True))#sorted()排序;.items()遍历字典(键,值) 元组,


#统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组
cndict = {}#定义一个空字典
def stats_text_cn(text):
    i = re.compile("[ \,，\;；\.。：、\{\}\[\]「」\*—~\-\?？！\!‘\'’“\"”\nA-Za-z0-9]")
    text_rm_symbol = i.sub("", text)
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff': #判断一个unicode是否是汉字
            cndict[i] = text.count(i)
    return cndict

#打印统计中文词频的结果
print("统计中文词频的结果为:")
print(sorted(cndict.items(),key=lambda item:item[1],reverse = True))#为了阅读方便，检索完毕后对字典进行按值从大到小排序                         
def stats_text(text):
    return dict(stats_text_en(text),**stats_text_cn(text))
def main():
    mdict={}
    mdict=stats_text(text)
    print(mdict)

if __name__=='__main__':
    main()      


        