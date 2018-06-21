# -*- coding:utf8 -*-
from tushare.util import dateu as du
import datetime

import tushare as ts
import pandas as pd

#返回上一交易日（字符串格式）
def lastTddate(strdate):
    date=None
    try:
        date = datetime.datetime.strptime(strdate, "%Y-%m-%d").date()
        while du.is_holiday(str(date))==True:
            date=date-datetime.timedelta(days=1)
        return str(date)
    except:
        print("日期输入有误")

#获取每日龙虎榜信息，并修改成指定格式，返回一个dataframe
def getLastData(strdate):
    date=lastTddate(strdate)
    dfLastTradeDay=ts.top_list(lastTddate(date))

    strIndex=date.replace("-","")
    listIndex = []
    for i in range(len(dfLastTradeDay)):
        listIndex.append(strIndex + "{:0>2}".format(i))
    dfLastTradeDay.index = listIndex
    return dfLastTradeDay


