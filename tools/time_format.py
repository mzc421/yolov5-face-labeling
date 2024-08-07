# -*- coding:utf-8 -*-
# @author: 牧锦程
# @微信公众号: AI算法与电子竞赛
# @Email: m21z50c71@163.com
# @VX：fylaicai


import sys


# 判断时间格式
def is_time(preTime):
    if preTime <= 0:
        print("时间格式不正确！程序结束！")
        sys.exit()


# 时间格式化
def time_format(preTime):
    is_time(preTime)  # 判断时间格式
    m, s = divmod(preTime, 60)  # 获取秒
    h, m = divmod(m, 60)  # 获取时、分
    h = int(h)  # 转整型
    m = int(m)  # 转整型

    if 0 < s < 1:
        time_str = f"{s:.3f}秒"
        return time_str
    elif h == 0 and m == 0 and s >= 1:
        time_str = f"{s:.3f}秒"
        return time_str
    elif h == 0 and m > 0:
        time_str = f"{m}分{s:.3f}秒"
        return time_str
    elif h > 0:
        if h >= 24:
            d = int(h / 24)  # 以天为单位
            h2 = h - 24
            time_str = f"{d}天{h2}时{m}分{s:.3f}秒"
        else:
            time_str = f"{h}时{m}分{s:.3f}秒"
        return time_str
    else:
        print("时间格式化失败！程序结束！")
        sys.exit()
