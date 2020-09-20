#-- GEO1001.2020--hw01
#-- [Runnan Fu] 
#-- [5213045]

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from readDATA import *
from common_functions import *

#########################################################################################
## lesson A1.1
# np.set_printoptions(suppress=True)
# print(mean(data_A))
# print(mean(data_B))
# print(mean(data_C))
# print(mean(data_D))
# print(mean(data_E))

# print(var(data_A))
# print(var(data_B))
# print(var(data_C))
# print(var(data_D))
# print(var(data_E))

# print(std(data_A))
# print(std(data_B))
# print(std(data_C))
# print(std(data_D))
# print(std(data_E))

#########################################################################################
# ## lesson A1.2 # histograms for the 5 sensors Temperature values
# fig = plt.figure(figsize=(18,12))
# ax1 = fig.add_subplot(321)
# ax2 = fig.add_subplot(322)
# ax3 = fig.add_subplot(323)
# ax4 = fig.add_subplot(324)
# ax5 = fig.add_subplot(325)

# # #change bins
# # nb =5
# nb = 50

# draw_hist(TEMP_A,'A_Temperature ($^\circ$C)',nb,ax1)
# draw_hist(TEMP_B,'B_Temperature ($^\circ$C)',nb,ax2)
# draw_hist(TEMP_C,'C_Temperature ($^\circ$C)',nb,ax3)
# draw_hist(TEMP_D,'D_Temperature ($^\circ$C)',nb,ax4)
# draw_hist(TEMP_E,'E_Temperature ($^\circ$C)',nb,ax5)

# fig.suptitle('Histograms for 5 sensors Temperature (bins=50)',fontsize=15,y=1)
# fig.tight_layout()
## plt.savefig('./figure1.jpg')
# plt.show()

# #########################################################################################
## lesson A1.3 #frequency poligons for the 5 sensors Temperature values overlap
# fig = plt.figure(figsize=(18,6))
# ax = fig.add_subplot(111)
# nb = int(2 * (len(TEMP_A)**(1/3)))

# draw_fp(TEMP_A, 'b.-', 'TEMP_A',nb, ax)
# draw_fp(TEMP_B, 'g.-', 'TEMP_B',nb, ax)
# draw_fp(TEMP_C, 'r.-', 'TEMP_C',nb, ax)
# draw_fp(TEMP_D, 'c.-', 'TEMP_D',nb, ax)
# draw_fp(TEMP_E, 'y.-', 'TEMP_E',nb, ax)

# plt.legend()
# fig.suptitle('Frequency Poligons for 5 sensors Temperature (bins=27)',fontsize=15,y=1)
# fig.tight_layout()
# # plt.savefig('./figure2.jpg')
# plt.show()

# #########################################################################################
##lesson A1.4 boxplot for: Wind Speed, Wind Direction and Temperature.
# fig, ((ax1,ax2,ax3))=plt.subplots(nrows=1,ncols=3,figsize=(18,6))

# draw_boxplot((WS_A, WS_B, WS_C, WS_D, WS_E),'Wind Speed [m/s]',ax1)
# draw_boxplot((WD_A, WD_B, WD_C, WD_D, WD_E),'Wind Direction [$^{\circ}$]',ax2)
# draw_boxplot((TEMP_A, TEMP_B, TEMP_C, TEMP_D, TEMP_E),'Temperature ($^\circ$C)',ax3)

# fig.suptitle('Boxplots for Wind Speed, Wind Direction and Temperature',fontsize=15,y=1)
# fig.tight_layout()
# # plt.savefig('./figure3.jpg')
# plt.show()

# #########################################################################################
# ##lesson A2.1# plot pmf pdf cdf 
# fig = plt.figure(figsize=(18,12))
# ax1 = fig.add_subplot(321)
# ax2 = fig.add_subplot(322)
# ax3 = fig.add_subplot(323)
# ax4 = fig.add_subplot(324)
# ax5 = fig.add_subplot(325)

# # nb = int(2 * (len(TEMP_A)**(1/3)))
# nb = 100

# #plot PMF
# draw_PMF(df_A[5],'A_Temperature ($^\circ$C)',ax1)
# draw_PMF(df_B[5],'B_Temperature ($^\circ$C)',ax2)
# draw_PMF(df_C[5],'C_Temperature ($^\circ$C)',ax3)
# draw_PMF(df_D[5],'D_Temperature ($^\circ$C)',ax4)
# draw_PMF(df_E[5],'E_Temperature ($^\circ$C)',ax5)
# fig.suptitle('PMF for Temperature',fontsize=15,y=1)
# fig.tight_layout()
# # plt.savefig('./figure4.jpg')
# plt.show()

# # plot PDF
# draw_PDF(TEMP_A,'A_Temperature ($^\circ$C)',nb, ax1)
# draw_PDF(TEMP_B,'B_Temperature ($^\circ$C)',nb, ax2)
# draw_PDF(TEMP_C,'C_Temperature ($^\circ$C)',nb, ax3)
# draw_PDF(TEMP_D,'D_Temperature ($^\circ$C)',nb, ax4)
# draw_PDF(TEMP_E,'E_Temperature ($^\circ$C)',nb, ax5)
# fig.suptitle('PDF for Temperature',fontsize=15,y=1)
# plt.legend()
# fig.tight_layout()
# # plt.savefig('./figure5.jpg')
# plt.show()

# # plot CDF
# draw_CDF(TEMP_A,'A_Temperature ($^\circ$C)',nb,ax1)
# draw_CDF(TEMP_B,'B_Temperature ($^\circ$C)',nb,ax2)
# draw_CDF(TEMP_C,'C_Temperature ($^\circ$C)',nb,ax3)
# draw_CDF(TEMP_D,'D_Temperature ($^\circ$C)',nb,ax4)
# draw_CDF(TEMP_E,'E_Temperature ($^\circ$C)',nb,ax5)
# fig.suptitle('CDF for Temperature',fontsize=15,y=1)
# fig.tight_layout()
# # plt.savefig('./figure6.jpg')
# plt.show()

# #########################################################################################
# ##lesson A2.2# WS PDF&kernel
# fig = plt.figure(figsize=(18,12))
# ax1 = fig.add_subplot(321)
# ax2 = fig.add_subplot(322)
# ax3 = fig.add_subplot(323)
# ax4 = fig.add_subplot(324)
# ax5 = fig.add_subplot(325)
# nb = int(2 * (len(TEMP_A)**(1/3)))

# #PDF
# draw_PDF(WS_A,'A_Wind Speed [m/s]',nb, ax1)
# draw_PDF(WS_B,'B_Wind Speed [m/s]',nb, ax2)
# draw_PDF(WS_C,'C_Wind Speed [m/s]',nb, ax3)
# draw_PDF(WS_D,'D_Wind Speed [m/s]',nb, ax4)
# draw_PDF(WS_E,'E_Wind Speed [m/s]',nb, ax5)

# #kernel
# draw_KDE(WS_A,'A_Wind Speed [m/s]',ax1)
# draw_KDE(WS_B,'B_Wind Speed [m/s]',ax2)
# draw_KDE(WS_C,'C_Wind Speed [m/s]',ax3)
# draw_KDE(WS_D,'D_Wind Speed [m/s]',ax4)
# draw_KDE(WS_E,'E_Wind Speed [m/s]',ax5)

# fig.suptitle('PDF & KDE for Wind Speed',fontsize=15,y=1)
# fig.tight_layout()
# # plt.savefig('./figure7.jpg')
# plt.show()

# #########################################################################################
# ##lesson A3.1# scatter plot for Temperature, Wet Bulb Globe Temperature (WBGT), Crosswind Speed. 
# fig = plt.figure(figsize=(20,6))

# ax1 = fig.add_subplot(251)
# ax2 = fig.add_subplot(252)
# ax3 = fig.add_subplot(253)
# ax4 = fig.add_subplot(254)
# ax5 = fig.add_subplot(255)
# ax6 = fig.add_subplot(256)
# ax7 = fig.add_subplot(257)
# ax8 = fig.add_subplot(258)
# ax9 = fig.add_subplot(259)
# ax10 = fig.add_subplot(2,5,10)

# # TEMP
# draw_scatter(TEMP_A,TEMP_B,ax1,'TEMP_A','TEMP_B','($^\circ$C)')
# draw_scatter(TEMP_A,TEMP_C,ax2,'TEMP_A','TEMP_C','($^\circ$C)')
# draw_scatter(TEMP_A,TEMP_D,ax3,'TEMP_A','TEMP_D','($^\circ$C)')
# draw_scatter(TEMP_A,TEMP_E,ax4,'TEMP_A','TEMP_E','($^\circ$C)')
# draw_scatter(TEMP_B,TEMP_C,ax5,'TEMP_B','TEMP_C','($^\circ$C)')
# draw_scatter(TEMP_B,TEMP_D,ax6,'TEMP_B','TEMP_D','($^\circ$C)')
# draw_scatter(TEMP_B,TEMP_E,ax7,'TEMP_B','TEMP_E','($^\circ$C)')
# draw_scatter(TEMP_C,TEMP_D,ax8,'TEMP_C','TEMP_D','($^\circ$C)')
# draw_scatter(TEMP_C,TEMP_E,ax9,'TEMP_C','TEMP_E','($^\circ$C)')
# draw_scatter(TEMP_D,TEMP_E,ax10,'TEMP_D','TEMP_E','($^\circ$C)')
# fig.suptitle('Temperature Scatter Plot',fontsize=13,y=1)
# fig.tight_layout()
## plt.savefig('./figure8.jpg')
# # plt.show()

# # WBGT
# draw_scatter(WBGT_A,WBGT_B,ax1,'WBGT_A','WBGT_B','($^\circ$C)')
# draw_scatter(WBGT_A,WBGT_C,ax2,'WBGT_A','WBGT_C','($^\circ$C)')
# draw_scatter(WBGT_A,WBGT_D,ax3,'WBGT_A','WBGT_D','($^\circ$C)')
# draw_scatter(WBGT_A,WBGT_E,ax4,'WBGT_A','WBGT_E','($^\circ$C)')
# draw_scatter(WBGT_B,WBGT_C,ax5,'WBGT_B','WBGT_C','($^\circ$C)')
# draw_scatter(WBGT_B,WBGT_D,ax6,'WBGT_B','WBGT_D','($^\circ$C)')
# draw_scatter(WBGT_B,WBGT_E,ax7,'WBGT_B','WBGT_E','($^\circ$C)')
# draw_scatter(WBGT_C,WBGT_D,ax8,'WBGT_C','WBGT_D','($^\circ$C)')
# draw_scatter(WBGT_C,WBGT_E,ax9,'WBGT_C','WBGT_E','($^\circ$C)')
# draw_scatter(WBGT_D,WBGT_E,ax10,'WBGT_D','WBGT_E','($^\circ$C)')

# fig.suptitle('Wet Bulb Globe Temperature (WBGT) Scatter Plot',fontsize=13,y=1)
# fig.tight_layout()
## plt.savefig('./figure9.jpg')
# # plt.show()

# # CS
# draw_scatter(CS_A,CS_B,ax1,'CS_A','CS_B','($^\circ$C)')
# draw_scatter(CS_A,CS_C,ax2,'CS_A','CS_C','($^\circ$C)')
# draw_scatter(CS_A,CS_D,ax3,'CS_A','CS_D','($^\circ$C)')
# draw_scatter(CS_A,CS_E,ax4,'CS_A','CS_E','($^\circ$C)')
# draw_scatter(CS_B,CS_C,ax5,'CS_B','CS_C','($^\circ$C)')
# draw_scatter(CS_B,CS_D,ax6,'CS_B','CS_D','($^\circ$C)')
# draw_scatter(CS_B,CS_E,ax7,'CS_B','CS_E','($^\circ$C)')
# draw_scatter(CS_C,CS_D,ax8,'CS_C','CS_D','($^\circ$C)')
# draw_scatter(CS_C,CS_E,ax9,'CS_C','CS_E','($^\circ$C)')
# draw_scatter(CS_D,CS_E,ax10,'CS_D','CS_E','($^\circ$C)')
# fig.suptitle('Crosswind Speed Scatter Plot',fontsize=13,y=1)
# fig.tight_layout()
## plt.savefig('./figure10.jpg')
# # plt.show()

# #########################################################################################
# # ##lesson A3.1# plot pearson&spearman
# fig = plt.figure(figsize=(18,6))
# ax1 = fig.add_subplot(131)
# ax2 = fig.add_subplot(132)
# ax3 = fig.add_subplot(133)
# fs = 10

# x = ['A-B','A-C','A-D','A-E','B-C','B-D','B-E','C-D','C-E','D-E']
# TEMP_person = [TEMP_AB[0],TEMP_AC[0],TEMP_AD[0],TEMP_AE[0],TEMP_BC[0],TEMP_BD[0],TEMP_BE[0],TEMP_CD[0],TEMP_CE[0],TEMP_DE[0]]
# TEMP_spearman = [TEMP_AB_sp[0],TEMP_AC_sp[0],TEMP_AD_sp[0],TEMP_AE_sp[0],TEMP_BC_sp[0],TEMP_BD_sp[0],TEMP_BE_sp[0],TEMP_CD_sp[0],TEMP_CE_sp[0],TEMP_DE_sp[0]]
# WBGT_person = [WBGT_AB[0],WBGT_AC[0],WBGT_AD[0],WBGT_AE[0],WBGT_BC[0],WBGT_BD[0],WBGT_BE[0],WBGT_CD[0],WBGT_CE[0],WBGT_DE[0]]
# WBGT_spearman = [WBGT_AB_sp[0],WBGT_AC_sp[0],WBGT_AD_sp[0],WBGT_AE_sp[0],WBGT_BC_sp[0],WBGT_BD_sp[0],WBGT_BE_sp[0],WBGT_CD_sp[0],WBGT_CE_sp[0],WBGT_DE_sp[0]]
# CS_person = [CS_AB[0],CS_AC[0],CS_AD[0],CS_AE[0],CS_BC[0],CS_BD[0],CS_BE[0],CS_CD[0],CS_CE[0],CS_DE[0]]
# CS_spearman = [CS_AB_sp[0],CS_AC_sp[0],CS_AD_sp[0],CS_AE_sp[0],CS_BC_sp[0],CS_BD_sp[0],CS_BE_sp[0],CS_CD_sp[0],CS_CE_sp[0],CS_DE_sp[0]]

# a1_p = ax1.scatter(x,TEMP_person, c = 'b')
# a1_sp = ax1.scatter(x,TEMP_spearman, c = 'r')
# ax1.set_xlabel('Correlation between sensors with Temperature',fontsize=fs)
# ax1.tick_params(labelsize=fs)
# ax1.xaxis.grid(True)
# ax1.yaxis.grid(True)

# a2_p = ax2.scatter(x,WBGT_person, c = 'b')
# a2_sp = ax2.scatter(x,WBGT_spearman, c = 'r')
# ax2.set_xlabel('Correlation between sensors with Wet Bulb Globe Temperature',fontsize=fs)
# ax2.tick_params(labelsize=fs)
# ax2.xaxis.grid(True)
# ax2.yaxis.grid(True)

# a3_p = ax3.scatter(x,CS_person, c = 'b')
# a3_sp = ax3.scatter(x,CS_spearman, c = 'r')
# ax3.set_xlabel('Correlation between sensors with Crosswind Speed',fontsize=fs)
# ax3.tick_params(labelsize=fs)
# ax3.xaxis.grid(True)
# ax3.yaxis.grid(True)
# ax3.legend((a3_p,a3_sp),('pearson','spearman'),bbox_to_anchor=(1, 1),fontsize=fs-2)

# fig.suptitle('Scatter plot with Pearson’s  and Spearmann’s rank coefficients between 5 sensors ',fontsize=15,y=1)
# fig.tight_layout()
# # plt.savefig('./figure11.jpg')
# plt.show()

# #########################################################################################
# ## lesson A4.1 # CDF for all the sensors and for variables Temperature and Wind Speed
# fig = plt.figure(figsize=(18,18))
# ax1 = fig.add_subplot(521)
# ax2 = fig.add_subplot(522)
# ax3 = fig.add_subplot(523)
# ax4 = fig.add_subplot(524)
# ax5 = fig.add_subplot(525)
# ax6 = fig.add_subplot(526)
# ax7 = fig.add_subplot(527)
# ax8 = fig.add_subplot(528)
# ax9 = fig.add_subplot(529)
# ax10 = fig.add_subplot(5,2,10)
    
# # sensor A
# draw_CDF(WS_A, 'A_Wind Speed [m/s]',50,ax1)
# draw_interval(WS_A, ax1)
# draw_CDF(TEMP_A, 'A_Temperature [($^\circ$C)]',50,ax2)
# draw_interval(TEMP_A, ax2)

# # sensor B
# draw_CDF(WS_B, 'B_Wind Speed [m/s]',50,ax3)
# draw_interval(WS_B, ax3)
# draw_CDF(TEMP_B, 'B_Temperature [($^\circ$C)]',50,ax4)
# draw_interval(TEMP_B, ax4)

# # sensor C
# draw_CDF(WS_C, 'C_Wind Speed [m/s]',50,ax5)
# draw_interval(WS_C, ax5)
# draw_CDF(TEMP_C, 'C_Temperature [($^\circ$C)]',50,ax6)
# draw_interval(TEMP_C, ax6)

# # sensor D
# draw_CDF(WS_D, 'D_Wind Speed [m/s]',50,ax7)
# draw_interval(WS_D, ax7)
# draw_CDF(TEMP_D, 'D_Temperature [($^\circ$C)]',50,ax8)
# draw_interval(TEMP_D, ax8)

# # sensor E
# draw_CDF(WS_E, 'E_Wind Speed [m/s]',50,ax9)
# draw_interval(WS_E, ax9)
# draw_CDF(TEMP_E, 'E_Temperature [($^\circ$C)]',50,ax10)
# draw_interval(TEMP_E, ax10)

# fig.suptitle('CDF for Temperature and Wind Speed',fontsize=13,y=1)
# fig.tight_layout()
## plt.savefig('./figure12.jpg')
# # plt.show()

# #########################################################################################
# # lesson A4.1 # save 95% confidence intervals to csv
# df_A = creat_df(np.row_stack((WS_A, TEMP_A)),'A')
# df_B = creat_df(np.row_stack((WS_B, TEMP_B)),'B')
# df_C = creat_df(np.row_stack((WS_C, TEMP_C)),'C')
# df_D = creat_df(np.row_stack((WS_D, TEMP_D)),'D')
# df_E = creat_df(np.row_stack((WS_E, TEMP_E)),'E')

# result = (((df_A.join(df_B)).join(df_C)).join(df_D)).join(df_E)

# result.index=['Wind speed [m/s]','Temperature [deg C]']

# outputpath= 'C:/FRN/TUDELFT/Q1/GEO1001_Mathematics/hw01/FRN/confidence_interval.csv'
# result.to_csv(outputpath,index=True,header=True)

# #########################################################################################
# # lesson A4.2  # Test the hypothesis
# print('P-value for sensors E & D for temperature =', hy_test(TEMP_E,TEMP_D))
# print('P-value for sensors E & D for Wind Speed =', hy_test(WS_E,WS_D))

# print('P-value for sensors D & C for temperature =', hy_test(TEMP_D,TEMP_C))
# print('P-value for sensors D & C for Wind Speed =', hy_test(WS_D,WS_C))

# print('P-value for sensors C & B for temperature =', hy_test(TEMP_C,TEMP_B))
# print('P-value for sensors C & B for Wind Speed =', hy_test(WS_C,WS_B))

# print('P-value for sensors B & A for temperature =', hy_test(TEMP_B,TEMP_A))
# print('P-value for sensors B & A for Wind Speed =', hy_test(WS_B,WS_A))

# #########################################################################################
# # Bonus question
import time
df_A = (pd.read_excel("../data/HEAT - A_final.xls",header=None)).drop(axis=0, index=[0,1,2,3,4])
df_B = (pd.read_excel("../data/HEAT - B_final.xls",header=None)).drop(axis=0, index=[0,1,2,3,4])
df_C = (pd.read_excel("../data/HEAT - C_final.xls",header=None)).drop(axis=0, index=[0,1,2,3,4])
df_D = (pd.read_excel("../data/HEAT - D_final.xls",header=None)).drop(axis=0, index=[0,1,2,3,4])
df_E = (pd.read_excel("../data/HEAT - E_final.xls",header=None)).drop(axis=0, index=[0,1,2,3,4])
df_ABCDE = pd.concat([df_A,df_B,df_C,df_D,df_E],sort=True)

def find_day(dataframe, label):
    data_TIME = dataframe[0].values.astype(str)
    df_TEMP =  pd.DataFrame(dataframe[5].values.astype(float))
    df_TEMP.columns = ['TEMP']

    TIME_A = []
    for i in data_TIME:
        timeArray = time.strptime(i, "%Y-%m-%d %H:%M:%S")
        dt_new = time.strftime("%Y%m%d-%H:%M:%S",timeArray)
        NEW_i = dt_new[ :8]
        TIME_A.append(NEW_i)  
    df_TIME = pd.DataFrame(TIME_A)
    df_TIME.columns = ['TIME']

    df = df_TIME.join(df_TEMP)

    gp_col = 'TIME'
    df_mean = df.groupby(gp_col)['TEMP'].mean()
    df_mean = pd.DataFrame(df_mean.reset_index())
    array_TIME = np.array(df_mean['TIME'])
    array_MEAN = np.array(df_mean['TEMP'])

    data_mean = np.vstack((array_TIME,array_MEAN))

    hottest_line = np.where(data_mean == np.max(data_mean[1]))
    hottest_day = data_mean[0,hottest_line[1]]
    coolest_line = np.where(data_mean == np.min(data_mean[1]))
    coolest_day = data_mean[0,coolest_line[1]]
    print(label,'the hottest_day:',hottest_day)
    print(label,'the coolest_day:',coolest_day)
    
find_day(df_A, 'Sensor A')  
find_day(df_B, 'Sensor B')
find_day(df_C, 'Sensor C')
find_day(df_D, 'Sensor D')
find_day(df_E, 'Sensor E')
find_day(df_ABCDE, 'All Sensors')