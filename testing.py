
# Hyndman, R.J. (n.d.) Time Series Data Library,
# http://robjhyndman.com/TSDL/
# http://robjhyndman.com/tsdldata/data/cryer6.dat


import statsmodels
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels import api as sm

Data = """2.42    2.14    2.28    2.50    2.44    2.72    2.71    2.74    2.55    2.49    2.13    2.28
2.35    1.82    2.40    2.46    2.38    2.83    2.68    2.81    2.54    2.54    2.37    2.54
2.62    2.34    2.68    2.75    2.66    2.96    2.66    2.93    2.70    2.65    2.46    2.59
2.75    2.45    2.85    2.99    2.89    3.43    3.25    3.59    3.12    3.16    2.86    3.22
3.24    2.95    3.32    3.29    3.32    3.91    3.80    4.02    3.53    3.61    3.22    3.67
3.75    3.25    3.70    3.98    3.88    4.47    4.60    4.90    4.20    4.20    3.80    4.50
4.40    4.00    4.70    5.10    4.90    5.70    3.90    4.20    5.10    5.00    4.70    5.50
5.30    4.60    5.90    5.50    5.40    6.70    6.80    7.40    6.00    5.80    5.50    6.40
6.20    5.70    6.40    6.70    6.30    7.80    7.60    8.60    6.60    6.50    6.00    7.60
7.00    6.00    7.10    7.40    7.20    8.40    8.50    9.40    7.10    7.00    6.60    8.00
10.45   8.81    10.61   9.97    10.69   12.40   13.38   14.31   10.90   9.98    9.20    10.94
10.53   9.06    10.17   11.17   10.84   12.09   13.66   14.06   11.14   11.10   10.00   11.98
11.74   10.27   12.05   12.27   12.03   13.95   15.10   15.65   12.47   12.29   11.52   13.08
12.50   11.05   12.94   13.24   13.16   14.95   16.00   16.98   13.15   12.88   11.99   13.13
12.99   11.69   13.78   13.70   13.57   15.12   15.55   16.73   12.68   12.65   11.18   13.27
12.64   11.01   13.30   12.19   12.91   14.90   16.10   17.30   12.90   13.36   12.26   13.93
13.94   12.75   14.19   14.67   14.66   16.21   17.72   18.15   14.19   14.33   12.99   15.19
15.09   12.94   15.46   15.39   15.34   17.02   18.85   19.49   15.61   16.16   14.84   17.04"""


# matplotlib.style.use('fivethirtyeight')
Data = Data.split()
Data = [float(i) for i in Data]
ts = pd.Series(Data, index=pd.date_range('1/1960', periods=len(Data), freq='M'))
ts.plot(figsize=(15,10))
plt.title("Monthly U.S. passenger air miles")
plt.xlabel('Figure 1: Time series plot of monthly U.S. air passenger miles from January 1960 to December 1977')
plt.ylabel('Air miles')
plt.savefig("./Output/1-Original.png")
plt.close()


fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(ts, lags=24, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(ts, lags=24, ax=ax2)
plt.xlabel("Figure 2: ACF and PACF of U.S. monthly air miles")
plt.savefig("./Output/2-OrgAcfPacf.png")
plt.close()


LogData = [math.log(i) for i in Data]
ts1 = pd.Series(LogData, index=pd.date_range('1/1960', periods=len(LogData), freq='M'))
ts1.plot(figsize=(15,10))
plt.title("Log Monthly U.S. passenger air miles")
plt.xlabel('Figure 3: Log transformation of U.S. monthly air miles')
plt.ylabel('Log(Air miles)')
plt.savefig("./Output/3-LogData.png")
plt.close()


ts2 = pd.Series(LogData, index=pd.date_range('1/1960', periods=len(LogData), freq='M'))
ts2 = ts2.diff(periods=1)
ts2.plot(figsize=(15,10))
plt.title("Log air-miles Diff(d=1)")
plt.xlabel('Figure 4: Take the first diff transformation for series')
plt.ylabel('Diff (Log (Air miles))')
plt.ylim((-0.5,0.5))
plt.savefig("./Output/4-DiffLogData.png")
plt.close()

fig5 = plt.figure(figsize=(15,10))
ax1 = fig5.add_subplot(211)
fig5 = sm.graphics.tsa.plot_acf(ts2[1:], lags=60, ax=ax1)
ax2 = fig5.add_subplot(212)
fig5 = sm.graphics.tsa.plot_pacf(ts2[1:], lags=60, ax=ax2)
plt.xlabel("Figure 5: ACF and PACF for the first differentiation of log series")
plt.savefig("./Output/5-FirstDiffAcfPacf.png")
plt.close()

ts3 = pd.Series(ts2[1:], index=pd.date_range('2/1960', periods=len(ts2[1:]), freq='M'))
ts3 = ts3.diff(periods=12)
ts3.plot(figsize=(15,10))
plt.title("Seasonally differenced log series (D=1)(d=1)")
plt.xlabel('Figure 6: Time series plot of seasonally differenced (D=1) for ARIMA(p,d,q)(P,D,Q)')
plt.ylim((-0.5,0.5))
plt.savefig("./Output/6-SeasonalDiffLogData.png")
plt.close()

print(ts3[11:])
fig6 = plt.figure(figsize=(15,10))
ax1 = fig6.add_subplot(211)
fig6 = sm.graphics.tsa.plot_acf(ts3[12:], lags=60, ax=ax1)
ax2 = fig6.add_subplot(212)
fig6 = sm.graphics.tsa.plot_pacf(ts3[12:], lags=60, ax=ax2)
plt.xlabel("Figure 7: ACF and PACF of the seasonally differenced series")
plt.savefig("./Output/7-SeasonalDiffAcfPacf.png")
plt.close()






































