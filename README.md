# Statistical-analysis-using-Python

## Introduction
This project is about the statistical analysis of a heat stress measurement dataset, which is the assignment 1 given by GEO1001 group in the faculty of architecture and the built environment in TU Delft. The data belongs to DOI: 10.4121/12833918.v1. Corresponding to four lessons given by the main python file (geo1001_hw01.py) mainly contains four parts: Lesson A1, A2, A3 and A4. Using the code, you are able to compute and visualize mean statistics (mean, variance and standard deviation),  PMF, PDF, CDF, KDE, correlations and hypothesis test. 


There are 3 python files, i.e., readDATA.py; common_functions.py; geo1001_hw01.py. The geo1001_hw01.py is the main python file that executes all the codes, readDATA.py is used to read all the data from Excel documents in the 'data' folder, and common_functions.py contains all the functions the main python file uses.

## Lesson A1
* Compute mean statistics (mean, variance and standard deviation for each of the sensors variables), what do you observe from the results?
* Create 1 plot that contains histograms for the 5 sensors Temperature values. Compare histograms with 5 and 50 bins, why is the number of bins important?
* Create 1 plot where frequency poligons for the 5 sensors Temperature values overlap in different colors with a legend.
* Generate 3 plots that include the 5 sensors boxplot for: Wind Speed, Wind Direction and Temperature.

To compute mean statistics (mean, variance and standard deviation for each of the sensors variables) for every variables for 5 samples, the functions mean(), var(), std() are used, which were defined at readDATA.py.

``` r
def mean(data):
    mean = data.mean(axis=0)
    return mean

def var(data):
    var = data.var(axis=0)
    return var
    
def std(data):
    std = data.std(axis=0)
    return std
    
```
And the geo1001_hw01.py prints the results, and make numpy print floating point numbers using fixed point notation.
``` r
np.set_printoptions(suppress=True)
print(mean(data_A))
print(mean(data_B))
print(mean(data_C))
print(mean(data_D))
print(mean(data_E))

print(var(data_A))
print(var(data_B))
print(var(data_C))
print(var(data_D))
print(var(data_E))

print(std(data_A))
print(std(data_B))
print(std(data_C))
print(std(data_D))
print(std(data_E))
```
To draw histograms plots, use draw_hist function in readDATA.py:
``` r
def draw_hist(data,xlabel,nb,ax):
    fs= 10
    ax.hist(x=data,bins=nb, facecolor='lightblue', edgecolor = 'black', alpha=0.7)
    ax.set_xlabel(xlabel,fontsize=fs)
    ax.set_ylabel('Frequency',fontsize=fs)
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)
```
The geo1001_hw01.py file focuses on creating 5 subplots for 5 samples respectively, setting bin numbers of histogram and drawing plots.
``` r
## lesson A1.2 # histograms for the 5 sensors Temperature values
fig = plt.figure(figsize=(18,12))
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)

# #change bins
# nb =5
nb = 50

draw_hist(TEMP_A,'A_Temperature ($^\circ$C)',nb,ax1)
draw_hist(TEMP_B,'B_Temperature ($^\circ$C)',nb,ax2)
draw_hist(TEMP_C,'C_Temperature ($^\circ$C)',nb,ax3)
draw_hist(TEMP_D,'D_Temperature ($^\circ$C)',nb,ax4)
draw_hist(TEMP_E,'E_Temperature ($^\circ$C)',nb,ax5)

fig.suptitle('Histograms for 5 sensors Temperature (bins=50)',fontsize=15,y=1)
fig.tight_layout()
# plt.savefig('./figure1.jpg')
plt.show()
```

To draw Frequency polygons for the 5 samples overlap in one plot, use draw_fp function. Firsting ploting histograms, and the collecting the edge values of bins used to plot polygons. Don't forget to hide the histograms otherwise the figure would be messed:
```r
def draw_fp(data, line_color, line_label, nb, ax):
    fs = 10
    y , edges, _  = ax.hist(data, bins=nb, color='w',histtype='step', linewidth=0)
    midpoint = 0.5*(edges[1:]+edges[:-1])
    ax.plot(midpoint,y, line_color, label=line_label, linewidth=1.5, alpha=1)
    ax.set_xlabel('Temperature ($^\circ$C)',fontsize=fs)
    ax.set_ylabel('Frequency',fontsize=fs)
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)
```
Again, The geo1001_hw01.py file focuses on creating subplots, setting bin numbers and drawing plots.
```r
## lesson A1.3 #frequency poligons for the 5 sensors Temperature values overlap
fig = plt.figure(figsize=(18,6))
ax = fig.add_subplot(111)
nb = int(2 * (len(TEMP_A)**(1/3)))

draw_fp(TEMP_A, 'b.-', 'TEMP_A',nb, ax)
draw_fp(TEMP_B, 'g.-', 'TEMP_B',nb, ax)
draw_fp(TEMP_C, 'r.-', 'TEMP_C',nb, ax)
draw_fp(TEMP_D, 'c.-', 'TEMP_D',nb, ax)
draw_fp(TEMP_E, 'y.-', 'TEMP_E',nb, ax)

plt.legend()
fig.suptitle('Frequency Poligons for 5 sensors Temperature (bins=27)',fontsize=15,y=1)
fig.tight_layout()
# plt.savefig('./figure2.jpg')
plt.show()
```

To draw boxplots, the function draw_boxplot is used:
```r
def draw_boxplot(data,ylabel,ax):
    fs = 10
    labels = ['A', 'B', 'C', 'D', 'E']
    ax.boxplot(data,showmeans=True,patch_artist=True,labels=labels)
    ax.set_xlabel('Five separate samples',fontsize=fs)
    ax.set_ylabel(ylabel,fontsize=fs)
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)
```
The geo1001_hw01.py file uses data from 5 samples for 'data' parameter, so that a single subplot can show 5 boxplots.
```r
##lesson A1.4 boxplot for: Wind Speed, Wind Direction and Temperature.
fig, ((ax1,ax2,ax3))=plt.subplots(nrows=1,ncols=3,figsize=(18,6))

draw_boxplot((WS_A, WS_B, WS_C, WS_D, WS_E),'Wind Speed [m/s]',ax1)
draw_boxplot((WD_A, WD_B, WD_C, WD_D, WD_E),'Wind Direction [$^{\circ}$]',ax2)
draw_boxplot((TEMP_A, TEMP_B, TEMP_C, TEMP_D, TEMP_E),'Temperature ($^\circ$C)',ax3)

fig.suptitle('Boxplots for Wind Speed, Wind Direction and Temperature',fontsize=15,y=1)
fig.tight_layout()
# plt.savefig('./figure3.jpg')
plt.show()
```

## Lesson A2
* Plot PMF, PDF and CDF for the 5 sensors Temperature values in independent plots (or subplots). Describe the behaviour of the distributions, are they all similar? what about their tails?
* For the Wind Speed values, plot the pdf and the kernel density estimation. Comment the differences.

To plot PMF, PDF and CDF for the 5 sensors Temperature values in independent plots, the functions draw_PMF, draw_PDF and draw_CDF are used. For draw_PDF, the code is similar with draw_fp, since in this project, I make pdf a continuous version of the density histogram for deliberately distinguishing between KDE and pdf. The bin number is recommended to be set larger, which in my cases is 100. The draw_kde function uses kdeplot method from seaborn.
```r
#lesson A2 #pdf、cdf、pmf、kde
def draw_PMF(data,xlabel,ax):
    fs = 10
    def pmf(sample):
        c = sample.value_counts()
        p = c/len(sample)
        return p
    df = pmf(data)
    df1 = df.to_frame()
    df1.reset_index(inplace=True)
    df1 = df1.astype(float)
    c = df1.sort_values(by=['index'])
    ax.bar(c.iloc[ : ,0],c.iloc[ : ,1],width=0.1, facecolor='lightblue',edgecolor='k', alpha=0.5)
    # df = pmf(data.astype(float))
    # c = df.sort_index()
    # ax.bar(c.index,c,width=0.1, color='blue', alpha=0.5)
    ax.set_xlabel(xlabel,fontsize=fs)
    ax.set_ylabel('PMF',fontsize=fs)
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)
    
def draw_PDF(data,xlabel,nb,ax):
    fs = 10
    y , edges, _  =ax.hist(x=data, bins=nb, density=True,color='lightblue', alpha=0.7,label = 'Histogram with Densities')
    midpoint = 0.5*(edges[1:]+edges[:-1])
    ax.plot(midpoint,y, color='blue', linewidth=1.5, alpha=0.7, label = 'PDF')
    #sns.distplot(data, bins=nb, color='b',ax=ax)
    ax.set_xlabel(xlabel, fontsize=fs)
    ax.set_ylabel('Probability Density')
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)

def draw_CDF(data,xlabel,nb,ax):
    fs = 10
    a=ax.hist(x=data, bins=nb, density=True, cumulative=True, color='lightblue', alpha=0.7)
    ax.plot(a[1][1:]-(a[1][1:]-a[1][:-1])/2,a[0], color='k')
    ax.set_xlabel(xlabel,fontsize=fs)
    ax.set_ylabel('CDF',fontsize=fs)
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)
    
def draw_KDE(data,xlabel,ax):
    fs = 10
    sns.kdeplot(data, ax=ax ,color='r',label = 'KDE')
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)
```
And in geo1001_hw01.py, I draw 3 different plots, so don't forget to use '#' to hide other codes when you want to view a single function.
```r
##lesson A2.1# plot pmf pdf cdf 
fig = plt.figure(figsize=(18,12))
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)

# nb = int(2 * (len(TEMP_A)**(1/3)))
nb = 100

#plot PMF
draw_PMF(df_A[5],'A_Temperature ($^\circ$C)',ax1)
draw_PMF(df_B[5],'B_Temperature ($^\circ$C)',ax2)
draw_PMF(df_C[5],'C_Temperature ($^\circ$C)',ax3)
draw_PMF(df_D[5],'D_Temperature ($^\circ$C)',ax4)
draw_PMF(df_E[5],'E_Temperature ($^\circ$C)',ax5)
fig.suptitle('PMF for Temperature',fontsize=15,y=1)
fig.tight_layout()
# plt.savefig('./figure4.jpg')
plt.show()

# plot PDF
draw_PDF(TEMP_A,'A_Temperature ($^\circ$C)',nb, ax1)
draw_PDF(TEMP_B,'B_Temperature ($^\circ$C)',nb, ax2)
draw_PDF(TEMP_C,'C_Temperature ($^\circ$C)',nb, ax3)
draw_PDF(TEMP_D,'D_Temperature ($^\circ$C)',nb, ax4)
draw_PDF(TEMP_E,'E_Temperature ($^\circ$C)',nb, ax5)
fig.suptitle('PDF for Temperature',fontsize=15,y=1)
plt.legend()
fig.tight_layout()
# plt.savefig('./figure5.jpg')
plt.show()

# plot CDF
draw_CDF(TEMP_A,'A_Temperature ($^\circ$C)',nb,ax1)
draw_CDF(TEMP_B,'B_Temperature ($^\circ$C)',nb,ax2)
draw_CDF(TEMP_C,'C_Temperature ($^\circ$C)',nb,ax3)
draw_CDF(TEMP_D,'D_Temperature ($^\circ$C)',nb,ax4)
draw_CDF(TEMP_E,'E_Temperature ($^\circ$C)',nb,ax5)
fig.suptitle('CDF for Temperature',fontsize=15,y=1)
fig.tight_layout()
# plt.savefig('./figure6.jpg')
plt.show()
```

To facilitate comparison, in geo1001_hw01.py,I make the pdf and the kernel density estimation overlapped in one figure using different color.
```r
#kernel
draw_KDE(WS_A,'A_Wind Speed [m/s]',ax1)
draw_KDE(WS_B,'B_Wind Speed [m/s]',ax2)
draw_KDE(WS_C,'C_Wind Speed [m/s]',ax3)
draw_KDE(WS_D,'D_Wind Speed [m/s]',ax4)
draw_KDE(WS_E,'E_Wind Speed [m/s]',ax5)

fig.suptitle('PDF & KDE for Wind Speed',fontsize=15,y=1)
fig.tight_layout()
# plt.savefig('./figure7.jpg')
plt.show()
```

## Lesson A3
* Compute the correlations between all the sensors for the variables: Temperature, Wet Bulb Globe Temperature (WBGT), Crosswind Speed. Perform correlation between sensors with the same variable, not between two different variables; for example, correlate Temperature time series between sensor A and B. Use Pearson’s and Spearmann’s rank coefficients. Make a scatter plot with both coefficients with the 3 variables.

To compute the correlations, I use pearsonr method from Scipy to processed data, you can find the code in the readDATA.py, here is a sample:
```r
# compute pearson&spearman
TEMP_AB = stats.pearsonr(TEMP_A, equal_size(TEMP_B,TEMP_A))
```
Also, when processing data, since different dataset might have different length, you need to interpolate to equal samples size. This function is name equal_size which you can find in common_functions.py:
```r
def equal_size(data1,data2):
    return np.interp(np.linspace(0,len(data2),len(data2)),np.linspace(0,len(data1),len(data1)),data1)
```
Then, a function named draw_scatter is used to draw scatter plots:
```r
def draw_scatter(data1,data2,ax,xlabel,ylabel,unit):
    fs = 10
    data1 = equal_size(data1,data2)
    ax.scatter(data1, data2, c='b',marker='.',s=1)
    ax.set_xlabel(xlabel+unit,fontsize=fs)
    ax.set_ylabel(ylabel+unit,fontsize=fs)
    ax.set_title(xlabel+' vs '+ylabel,fontsize=fs+3)
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)
```
In geo1001_hw01.py, I first draw a number of scatter plots to judge whether there are linear relations between all the sensors for the 3 variables. Here I will not show this part of the code in geo1001_hw01.py, because it's too long and it is mainly focus on creating subplots and drawing plots. Then I make a scatter plot with both coefficients with 3 variables. The most important idea is making the number of x-array and y-array consistent, and having a reasonable one-to-one correspondence:
```r
fig = plt.figure(figsize=(18,6))
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)
fs = 10

x = ['A-B','A-C','A-D','A-E','B-C','B-D','B-E','C-D','C-E','D-E']
TEMP_person = [TEMP_AB[0],TEMP_AC[0],TEMP_AD[0],TEMP_AE[0],TEMP_BC[0],TEMP_BD[0],TEMP_BE[0],TEMP_CD[0],TEMP_CE[0],TEMP_DE[0]]
TEMP_spearman = [TEMP_AB_sp[0],TEMP_AC_sp[0],TEMP_AD_sp[0],TEMP_AE_sp[0],TEMP_BC_sp[0],TEMP_BD_sp[0],TEMP_BE_sp[0],TEMP_CD_sp[0],TEMP_CE_sp[0],TEMP_DE_sp[0]]
WBGT_person = [WBGT_AB[0],WBGT_AC[0],WBGT_AD[0],WBGT_AE[0],WBGT_BC[0],WBGT_BD[0],WBGT_BE[0],WBGT_CD[0],WBGT_CE[0],WBGT_DE[0]]
WBGT_spearman = [WBGT_AB_sp[0],WBGT_AC_sp[0],WBGT_AD_sp[0],WBGT_AE_sp[0],WBGT_BC_sp[0],WBGT_BD_sp[0],WBGT_BE_sp[0],WBGT_CD_sp[0],WBGT_CE_sp[0],WBGT_DE_sp[0]]
CS_person = [CS_AB[0],CS_AC[0],CS_AD[0],CS_AE[0],CS_BC[0],CS_BD[0],CS_BE[0],CS_CD[0],CS_CE[0],CS_DE[0]]
CS_spearman = [CS_AB_sp[0],CS_AC_sp[0],CS_AD_sp[0],CS_AE_sp[0],CS_BC_sp[0],CS_BD_sp[0],CS_BE_sp[0],CS_CD_sp[0],CS_CE_sp[0],CS_DE_sp[0]]

a1_p = ax1.scatter(x,TEMP_person, c = 'b')
a1_sp = ax1.scatter(x,TEMP_spearman, c = 'r')
ax1.set_xlabel('Correlation between sensors with Temperature',fontsize=fs)
ax1.tick_params(labelsize=fs)
ax1.xaxis.grid(True)
ax1.yaxis.grid(True)

a2_p = ax2.scatter(x,WBGT_person, c = 'b')
a2_sp = ax2.scatter(x,WBGT_spearman, c = 'r')
ax2.set_xlabel('Correlation between sensors with Wet Bulb Globe Temperature',fontsize=fs)
ax2.tick_params(labelsize=fs)
ax2.xaxis.grid(True)
ax2.yaxis.grid(True)

a3_p = ax3.scatter(x,CS_person, c = 'b')
a3_sp = ax3.scatter(x,CS_spearman, c = 'r')
ax3.set_xlabel('Correlation between sensors with Crosswind Speed',fontsize=fs)
ax3.tick_params(labelsize=fs)
ax3.xaxis.grid(True)
ax3.yaxis.grid(True)
ax3.legend((a3_p,a3_sp),('pearson','spearman'),bbox_to_anchor=(1, 1),fontsize=fs-2)

fig.suptitle('Scatter plot with Pearson’s  and Spearmann’s rank coefficients between 5 sensors ',fontsize=15,y=1)
fig.tight_layout()
# plt.savefig('./figure11.jpg')
plt.show()
```

## Lesson A4
* Plot the CDF for all the sensors and for variables Temperature and Wind Speed, then compute the 95% confidence intervals for variables Temperature and Wind Speed for all the sensors and save them in a table (txt or csv form).
* Test the hypothesis: the time series for Temperature and Wind Speed are the same for sensors: 1) E, D; 2) D, C; 3) C, B; 4) B, A.

Since we have already mentioned CDF, here I will not show this part of the code in geo1001_hw01.py. Let's focus on computing the 95% confidence intervals and how to save them in a table. The draw_interval, save_interval functions defined at common_function.py are used respectively to draw 95% confidence intervals lines in plots and to save the intervals data in a table:
```r
#Lesson A4
def draw_interval(data, ax):
#   xquantx = ((np.quantile(data, 0.05), np.quantile(data, 0.95)))
    data_mean = data.mean()
    data_std = np.std(data, ddof = 1)
    # n=len(data)
    # data_se = data_std/np.sqrt(n)
    confi_inte = stats.norm.interval(0.95, data_mean, data_std)
    ax.axvline(confi_inte[0],color='r',linewidth = 0.5)
    ax.axvline(confi_inte[1],color='r',linewidth = 0.5)

def save_interval(data):
    data_mean = data.mean(axis=1)
    data_std = np.std(data,ddof = 1,axis=1)
    # n=data.shape[0]
    # data_se = data_std/np.sqrt(n)
    confi_inte = stats.norm.interval(0.95,  data_mean, data_std)
    return confi_inte
```
In the geo1001_hw01.py, I first draw CDF and 95% CI for all the sensors for variables Temperature and Wind Speed, this part of code will not be shared here since you can easily find and understand them. Here I show the code for saving 95% confidence intervals to csv:
```r
# lesson A4.1 # save 95% confidence intervals to csv
df_A = creat_df(np.row_stack((WS_A, TEMP_A)),'A')
df_B = creat_df(np.row_stack((WS_B, TEMP_B)),'B')
df_C = creat_df(np.row_stack((WS_C, TEMP_C)),'C')
df_D = creat_df(np.row_stack((WS_D, TEMP_D)),'D')
df_E = creat_df(np.row_stack((WS_E, TEMP_E)),'E')

result = (((df_A.join(df_B)).join(df_C)).join(df_D)).join(df_E)

result.index=['Wind speed [m/s]','Temperature [deg C]']

outputpath= 'C:/FRN/TUDELFT/Q1/GEO1001_Mathematics/hw01/FRN/confidence_interval.csv'
result.to_csv(outputpath,index=True,header=True)
```
I first use row_stack method from numpy to combine WS and TEMP data, then use the combined data as an argument to creat_df function. Then the outputs of the funtion are joined together, which creates a DataFrame containing intervels boundaries for all sensors for WS and Temperature variables. For the creat_df function, it is used to convert numpy array data like WS_A and TEMP_A to a DataFrame, which is easier to be exported as a CSV file:
```r
def creat_df(data,label):
    a=[] 
    b=[]
    for i in save_interval(data)[0]:
        a.append(i)    
    for i in save_interval(data)[1]:
        b.append(i)
    c ={label+"_lower boundary" : a,
       label+"_upper boundary" : b}
    return pd.DataFrame(c)
```
To test the hypothesises, the hy_test function is used, and the return value is a two-tail P-value:
```r
def hy_test(data1,data2):
    t, p_two= stats.ttest_ind(data1, data2, equal_var=False)
    return p_two
```
Then the coresponding part of code in geo1001_hw01.py prints the result:
```r
# lesson A4.2  # Test the hypothesis
print('P-value for sensors E & D for temperature =', hy_test(TEMP_E,TEMP_D))
print('P-value for sensors E & D for Wind Speed =', hy_test(WS_E,WS_D))

print('P-value for sensors D & C for temperature =', hy_test(TEMP_D,TEMP_C))
print('P-value for sensors D & C for Wind Speed =', hy_test(WS_D,WS_C))

print('P-value for sensors C & B for temperature =', hy_test(TEMP_C,TEMP_B))
print('P-value for sensors C & B for Wind Speed =', hy_test(WS_C,WS_B))

print('P-value for sensors B & A for temperature =', hy_test(TEMP_B,TEMP_A))
print('P-value for sensors B & A for Wind Speed =', hy_test(WS_B,WS_A))
```
