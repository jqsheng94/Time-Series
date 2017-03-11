
# Data Analysis of U.S Monthly Air Passenger Miles

## 1. Introduction
### 1.1 Background
Since the Wright brothers invented the airplane, it has a great influence on human’s life. People can arrive in a faraway place in a short time by plane, which brings a lot of convenience for daily life. At the same time, the airline companies benefit a lot from the increasing number of passengers. In this way, it’s important for companies to consider about the situation of flight in order to make the arrangement. In this paper, we are going to analyze the data of air miles for U.S passengers from Jan.1960 to Dec.1977.

### 1.2 Original Data

![11](https://github.com/jqsheng94/Time-Series/blob/master/Output/1-Original.png)

![21](https://github.com/jqsheng94/Time-Series/blob/master/Output/2-OrgAcfPacf.png)


The time series plot (Figure 1) of the monthly air miles of the US from Jan. 1960 to the end of 1977 shows that the mean of this process changes over time, also the variance is not constant (it fluctuates greatly from the year of 1970). Therefore, this process is non-stationary. Also, the ACF of this process series decays very slowly, which gives the support that the time series is not stationary. 

## 2. Transformation
### 2.1 Log-transformation

Since it is a non-stationary problem, first of all, we try to take a log transformation for the U.S air miles series to eliminate the non constant variance.

![21](https://github.com/jqsheng94/Time-Series/blob/master/Output/3-LogData.png)

After taking the log transformation, we can clearly see that the time series plot of the log U.S air miles (Figure 3) is stationary in variance, but the mean is still changing over time, for this problem we can try to take the first difference.

### 2.2 First differenced-transformation

![221](https://github.com/jqsheng94/Time-Series/blob/master/Output/4-DiffLogData.png)

The first differenced of log time series plot (Figure 4) seems stationary. But we need to test it with ACF and PACF. Here are ACF and PACF of the first differenced of the log series: 

![222](https://github.com/jqsheng94/Time-Series/blob/master/Output/5-FirstDiffAcfPacf.png)

The ACF for the first differencing of log U.S air miles (Figure 5) shows that there is a very clearly periodic component at lag 12, 24, 36…, and decays very slowly at each period, not exponentially but say in linear fashion. Thus, we conclude this is a seasonal non-stationary process. Then let’s try taking a difference of order 12 to solve this seasonal non-stationary process.

### 2.3 Seasonal differenced-transformation

The following plot (Figure 6) is the seasonally differenced (lag=12) of the first differenced of the log series:

![231](https://github.com/jqsheng94/Time-Series/blob/master/Output/6-SeasonalDiffLogData.png)


The time series plot of seasonally differenced ( Figure 6) reveals that the data becomes stationary, but only a few extreme values in data points around 1967 and 1968.

![232](https://github.com/jqsheng94/Time-Series/blob/master/Output/7-SeasonalDiffAcfPacf.png)

Figure 7 is the ACF and PACF of the seasonally differenced of the first differenced of log U.S air miles. Since we are under the seasonally differenced, we do not need to pay attention to the lags which are between each period. Only the lag 12, 24, 36 … we need to consider. Thus, the ACF cuts off after the first season which is at lag 12 and PACF is infinite in extent, it is give us the seasonal ARIMA ( P,D,Q) model where P=0, Q=1and D=1. Within the seasonal lags, it appears that the ACF tails off and the PACF cuts off after lag2 or tails off, which we need to test with fitted model.

Combined all of the information what we have already got:  d=1, D=1, P=0, Q=1 to give the full seasonal ARIMA (p, d, q) x (P, D, Q)s = ARIMA(p, 1, q) x (0, 1, 1)s=12.

## 3. Model Selection

After collecting data from both ACF and PACF, the ACF cuts off after seasonal lag 1 and PACF decreases exponentially fast. Our initial guess for seasonal component is (0, 1, 1). When considering ordinary part, it seems that both ACF and PACF are tailing off. Hence, both p and q are greater than 0. Ordinary component could be (1, 1, 1). There is another guess for ordinary component is ACF is tailing off and PACF cuts off after lag 2. In this case, ordinary component is (2, 1, 0)
We have tried 10 different models which are combinations of our guess or some similar models. Here are 4 simplest models;

```
Model 1: ARIMA(1, 1, 1) x (0, 1, 1)s=12.
Model 2: ARIMA(1, 1, 1) x (1, 1, 1)s=12.
Model 3: ARIMA(2, 1, 0) x (0, 1, 1)s=12.
Model 4: ARIMA(2, 1, 0) x (1, 1, 1)s=12.
```

Then we have to check diagnostics of each model. 
The diagnostics for model 1 is listed below:  

```
                                 Statespace Model Results                                 
==========================================================================================
Dep. Variable:                                  y   No. Observations:                  216
Model:             SARIMAX(1, 1, 1)x(0, 1, 1, 12)   Log Likelihood                 280.556
Date:                            Fri, 10 Mar 2017   AIC                           -553.112
Time:                                    23:28:28   BIC                           -539.611
Sample:                                01-31-1960   HQIC                          -547.657
                                     - 12-31-1977                                         
Covariance Type:                              opg                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ar.L1          0.4652      0.119      3.918      0.000       0.233       0.698
ma.L1         -0.7686      0.092     -8.376      0.000      -0.948      -0.589
ma.S.L12      -0.7357      0.050    -14.628      0.000      -0.834      -0.637
sigma2         0.0035      0.000     16.955      0.000       0.003       0.004
===================================================================================
Ljung-Box (Q):                       26.67   Jarque-Bera (JB):               591.99
Prob(Q):                              0.95   Prob(JB):                         0.00
Heteroskedasticity (H):               0.25   Skew:                             0.01
Prob(H) (two-sided):                  0.00   Kurtosis:                        11.37
===================================================================================
```

![31](https://github.com/jqsheng94/Time-Series/blob/master/Output/8-residualts.png)

![32](https://github.com/jqsheng94/Time-Series/blob/master/Output/9-SRfAcfPacf.png)

In figure 8, residuals look stationary except few outliers. These outliers are extreme values from original database. It shows that residuals are uncorrelated in time. In figure 9,  ACF of residuals fluctuate in the band close to 0. It indicates that residuals are independent. None of the residuals are individually significant. Residuals also look like white noise with mean 0 and variance constant. This model is adequate and fits data very well.

The diagnostics for model 2 is almost the same as model 1. For model 3 and 4, p-values for Ljung-Box statistic are below the blue line which is quite small. We can reject model 3 and 4 since we do not consider about inadequate models. 

Then we can compare about AIC for both model 1 and model 2.

```
AIC for model 1: -553.11
AIC for model 2: -552.37
![3e1](https://github.com/jqsheng94/Time-Series/blob/master/Output/CodeCogsEqn%201.gif)
```


Since model 1 has smaller AIC and less parameters, we choose model 1 as our final model. Actually, AIC for model 1 is also the smallest among 10 models we have tried before. 

## 4. Residual test

![41](https://github.com/jqsheng94/Time-Series/blob/master/Output/10-QQandHistogram.png)

```
W = 0.8789, p-value = 3.981e-12
```

Both normal Q-Q plot and histogram show that residuals are approximately normally distributed. In the normal Q-Q plot, some residuals in the left corner and right corner of the graph departure from normality. These values are some extreme values from original data. Although these two graphs indicate that residuals are somewhat close to normality, we run a Shapiro-Wilks test to show the normality. This test gives a very small p-value 3.981e-12. We can make the conclusion that residuals are not normally distributed. 

## 5. Final model  
```
ARIMA(1, 1, 1) x (0, 1, 1)s=12.

AIC=-553.11
```
This is our final model, and AIC is the smallest among all those 10 models we have tried before.  
We can use this model to predict future values. 

## 6. Forecast

![61](https://github.com/jqsheng94/Time-Series/blob/master/Output/11-prediction.png)

Here is the prediction for next 5 years. As we all can see, the 6th, 7th, 8th, points are relatively high within each cycle compare to other points. For some reasons like temperature or weather,   passengers are more willing to travel on summer than other seasons. There is an obvious positive trend in this graph. Although there are many cycles in the time series plots, monthly air passenger miles increase from 10 to 16 over 7 year periods. More and more passengers choose to use transportation airplane to go to other places. So our prediction for next 5 years will increase significantly compare to the year 1977.

## 7. Conclusion

The monthly air passenger miles follow yearly data. Finally, we choose **ARIMA(1, 1, 1) x (0, 1, 1)s=12**  as our best model. This model shows that passengers are more likely to travel on summer. There is an increasing number of people choose transportation airplane. But one problem of our data is , maybe for some reason, data ended in Dec 1977. This data is so old and we cannot use this data to get meaningful prediction.

## Reference 

Hyndman, R.J. (n.d.) Time Series Data Library,

"http://robjhyndman.com/TSDL/"

"http://robjhyndman.com/tsdldata/data/cryer6.dat"


