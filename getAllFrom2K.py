#coding:UTF-8
import tushare as ts
import sys
today = date.today()

# 如何使用: python -W ignore getAllFrom2K.py 002188 005688
# 结果将会保存在当前文件夹的xlsx里面,并用股票代码作为xlsx文件名
if len(sys.argv)<2:
	print 'python -W ignore getAllFrom2K.py 股票代码 [股票代码]'
	return 

for i in range(1, len(sys.argv)):
	result = ts.get_h_data(sys.argv[i], start='2000-01-01', end=today.strftime("%Y-%m-%d"))
	result.to_excel('./xlsx/'+sys.argv[i]+'.xlsx')
