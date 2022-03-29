# adapted from Alex Martelli's example in "Re-learning Python"
# http://www.aleax.it/Python/accu04_Relearn_Python_alex.pdf
# (slide 41) Ex: lines-by-word file index

# BEGIN INDEX0
"""Build an index mapping word -> list of occurrences"""

import sys
import re

# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象(re.RegexObject对象)，
# 供 match() 和 search() 这两个函数使用
WORD_RE = re.compile(r'\w+')  # 不转义使用真实字符例如r'\t'就是输出\t 否则是一个制表符

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    """
    将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    list(enumerate(seasons, start=1))  # 下标从 1 开始
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
    """
    for line_no, line in enumerate(fp, 1):
        # 和findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
        # 迭代器生成的是re.MatchObject对象
        # 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
        for match in WORD_RE.finditer(line):
            # re.MatchObject的group() 返回被 RE 匹配的字符串。
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 这其实是一种很不好的实现，这样写只是为了证明论点
            # this is ugly; coded like this to make a point
            occurrences = index.get(word, [])  # <1> 提取 word 出现的情况，如果还没有它的记录，返回 []。
            occurrences.append(location)  # <2> 把单词新出现的位置添加到列表的后面。
            index[word] = occurrences  # <3> 把新的列表放回字典中，这又牵扯到一次查询操作。

"""
sorted(iterable[, cmp[, key[, reverse]]])
iterable -- 可迭代对象。
cmp -- 自定义比较函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。默认值为None。
key -- 指定一个函数，该函数只有一个参数。这个函数用于从Iterable中每个元素中提取一个用于比较的关键字。默认值为None。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
"""
for word in sorted(index, key=str.upper):  # <4>
    print(word, index[word])
# END INDEX0
