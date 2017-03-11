A = """2.42    2.14    2.28    2.50    2.44    2.72    2.71    2.74    2.55    2.49    2.13    2.28
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
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style
# matplotlib.style.use('fivethirtyeight')
A = A.split()
A = [float(i) for i in A]
ts = pd.Series(A, index=pd.date_range('1/1960', periods=len(A), freq='M'))
ts.plot()
plt.title("Monthly U.S. passenger air miles")
plt.xlabel('Months')
plt.ylabel('Air miles')
plt.show()





































