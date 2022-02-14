"""自定义封装的特殊用途的 时间/日期相关方法"""

import time
from datetime import datetime, timedelta


def daysdelta(from_datetime_day, days: int = 0):
    return (datetime_day + timedelta(days=days)).date()


def somedays_later_bystr(datestr, n):
    """传入字符串日期 2021-05-01 和 间隔几天，得到几天后的日期值（str）"""
    return str(datetime.strptime(datestr, "%Y-%m-%d").date() + timedelta(days=n))


def timestamp_to_str(timestamp):
    """把 rum 中的时间戳（纳米级）转换为年月日时分秒的字符串"""
    timeArray = time.localtime(int(timestamp / 1000000000))
    strtime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    # 另一种实现方式
    # dateArray = datetime.utcfromtimestamp(int(timestamp / 1000000000)
    # otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return strtime


def time2str():
    """根据当前时间，得到时间信息的字符串，通常用于文件命名"""
    s = f"{str(datetime.now())[:19].replace(' ','_').replace(':','').replace('-','')}"
    return s


def countdown_to_ends(endsname, endsday):
    """
    距离 endsday 的剩余时间
    endsname 如何称呼那个终点？比如新年，“80岁”
    endsday "2064-10-05 00:00:00"
    """
    cd = datetime.strptime(endsday, "%Y-%m-%d %H:%M:%S") - datetime.now()
    if cd.days < 0:
        return
    if cd.days >= 365:
        rlt = f"距离 {endsname} {endsday[:10]}\n还剩 {cd.days//365} 年 {cd.days%365} 天"
    elif cd.days >= 7:
        rlt = f"距离 {endsname} {endsday[:10]}\n还剩 {cd.days//7} 周 {cd.days%7} 天"
    elif cd.days >= 3:
        rlt = f"距离 {endsname} {endsday}\n还剩 {cd.days} 天 {cd.seconds//3600} 时"
    elif cd.days > 0 or cd.seconds > 0:
        rlt = f"距离 {endsname} {endsday}\n还剩 {cd.days*24+cd.seconds//3600} 时 {(cd.seconds%3600)//60} 分"
    return rlt


def passed_percent(start, days):
    """
    计算当前占统计时间段内的百分比
    start:str,start_day,like 2022-01-01
    days:int,时间段的总天数
    """
    n = datetime.now() - datetime.strptime(start, "%Y-%m-%d")
    return (24 * 60 * n.days + n.seconds / 60) / (days * 24 * 60)


def view_percent(text, percent, wide=30, is_line=False, is_squre=True, is_ptext=True):
    """
    把百分比转换为可视化进度条字符串
    text:str,文本
    percent:float,百分比数
    wide:进度条宽度
    is_line:只显示取得的进展，不显示占比
    is_squre:是否显示进度条
    is_ptext: 是否显示百分比数值
    """
    l = min(int(abs(percent) * wide), wide)
    if is_line:
        text += "■" * l  # "❀"
    if is_squre:
        text += "■" * l + "□" * (wide - l)
    if is_ptext:
        text += f" {round(percent*100,2)}%"
    return text