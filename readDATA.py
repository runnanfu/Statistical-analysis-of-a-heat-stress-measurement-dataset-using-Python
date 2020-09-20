#-- GEO1001.2020--hw01
#-- [Runnan Fu] 
#-- [5213045]

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from common_functions import *

##read data
df_A = (pd.read_excel("../data/HEAT - A_final.xls",header=None)).drop(axis=0, index=[0,1,2,3,4], columns = [0])
data_A = df_A.values.astype(float)


df_B = (pd.read_excel("../data/HEAT - B_final.xls",header=None)).drop(axis=0, index=[0,1,2,3,4], columns = [0])
data_B = df_B.values.astype(float)

df_C = (pd.read_excel("../data/HEAT - C_final.xls",header=None)).drop(axis=0, index=[0,1,2,3,4], columns = [0])
data_C = df_C.values.astype(float)

df_D = (pd.read_excel("C:/FRN/TUDELFT/Q1/GEO1001_Mathematics/hw01/data/HEAT - D_final.xls",header=None)).drop(axis=0, index=[0,1,2,3,4], columns = [0])
data_D = df_D.values.astype(float)

df_E = (pd.read_excel("C:/FRN/TUDELFT/Q1/GEO1001_Mathematics/hw01/data/HEAT - E_final.xls",header=None)).drop(axis=0, index=[0,1,2,3,4], columns = [0])
data_E = df_E.values.astype(float)

WD_A = df_A [1].values.astype(float)  
WD_B = df_B [1].values.astype(float)
WD_C = df_C [1].values.astype(float)
WD_D = df_D [1].values.astype(float)
WD_E = df_E [1].values.astype(float)

WS_A = df_A [2].values.astype(float)  
WS_B = df_B [2].values.astype(float)
WS_C = df_C [2].values.astype(float)
WS_D = df_D [2].values.astype(float)
WS_E = df_E [2].values.astype(float)


CS_A = df_A [3].values.astype(float)  
CS_B = df_B [3].values.astype(float)
CS_C = df_C [3].values.astype(float)
CS_D = df_D [3].values.astype(float)
CS_E = df_E [3].values.astype(float)

HS_A = df_A [4].values.astype(float)  
HS_B = df_B [4].values.astype(float)
HS_C = df_C [4].values.astype(float)
HS_D = df_D [4].values.astype(float)
HS_E = df_E [4].values.astype(float)

TEMP_A = df_A [5].values.astype(float)
TEMP_B = df_B [5].values.astype(float)
TEMP_C = df_C [5].values.astype(float)
TEMP_D = df_D [5].values.astype(float)
TEMP_E = df_E [5].values.astype(float)
TEMP = np.hstack((TEMP_A, TEMP_B, TEMP_C, TEMP_D, TEMP_E))
TEMP.sort()

GT_A = df_A [6].values.astype(float)  
GT_B = df_B [6].values.astype(float)
GT_C = df_C [6].values.astype(float)
GT_D = df_D [6].values.astype(float)
GT_E = df_E [6].values.astype(float)

WC_A = df_A [7].values.astype(float)  
WC_B = df_B [7].values.astype(float)
WC_C = df_C [7].values.astype(float)
WC_D = df_D [7].values.astype(float)
WC_E = df_E [7].values.astype(float)

RH_A = df_A [8].values.astype(float)  
RH_B = df_B [8].values.astype(float)
RH_C = df_C [8].values.astype(float)
RH_D = df_D [8].values.astype(float)
RH_E = df_E [8].values.astype(float)

HSI_A = df_A [9].values.astype(float)  
HSI_B = df_B [9].values.astype(float)
HSI_C = df_C [9].values.astype(float)
HSI_D = df_D [9].values.astype(float)
HSI_E = df_E [9].values.astype(float)

DP_A = df_A [10].values.astype(float)  
DP_B = df_B [10].values.astype(float)
DP_C = df_C [10].values.astype(float)
DP_D = df_D [10].values.astype(float)
DP_E = df_E [10].values.astype(float)

PWBT_A = df_A [11].values.astype(float)  
PWBT_B = df_B [11].values.astype(float)
PWBT_C = df_C [11].values.astype(float)
PWBT_D = df_D [11].values.astype(float)
PWBT_E = df_E [11].values.astype(float)

SP_A = df_A [12].values.astype(float)  
SP_B = df_B [12].values.astype(float)
SP_C = df_C [12].values.astype(float)
SP_D = df_D [12].values.astype(float)
SP_E = df_E [12].values.astype(float)

BP_A = df_A [13].values.astype(float)  
BP_B = df_B [13].values.astype(float)
BP_C = df_C [13].values.astype(float)
BP_D = df_D [13].values.astype(float)
BP_E = df_E [13].values.astype(float)

AL_A = df_A [14].values.astype(float)  
AL_B = df_B [14].values.astype(float)
AL_C = df_C [14].values.astype(float)
AL_D = df_D [14].values.astype(float)
AL_E = df_E [14].values.astype(float)

DA_A = df_A [15].values.astype(float)  
DA_B = df_B [15].values.astype(float)
DA_C = df_C [15].values.astype(float)
DA_D = df_D [15].values.astype(float)
DA_E = df_E [15].values.astype(float)

NWBT_A = df_A [16].values.astype(float)  
NWBT_B = df_B [16].values.astype(float)
NWBT_C = df_C [16].values.astype(float)
NWBT_D = df_D [16].values.astype(float)
NWBT_E = df_E [16].values.astype(float)

WBGT_A = df_A [17].values.astype(float)  
WBGT_B = df_B [17].values.astype(float)
WBGT_C = df_C [17].values.astype(float)
WBGT_D = df_D [17].values.astype(float)
WBGT_E = df_E [17].values.astype(float)

TWL_A = df_A [18].values.astype(float)  
TWL_B = df_B [18].values.astype(float)
TWL_C = df_C [18].values.astype(float)
TWL_D = df_D [18].values.astype(float)
TWL_E = df_E [18].values.astype(float)

DM_A = df_A [19].values.astype(float)  
DM_B = df_B [19].values.astype(float)
DM_C = df_C [19].values.astype(float)
DM_D = df_D [19].values.astype(float)
DM_E = df_E [19].values.astype(float)

# compute pearson&spearman
TEMP_AB = stats.pearsonr(TEMP_A, equal_size(TEMP_B,TEMP_A))
TEMP_AC = stats.pearsonr(TEMP_A, equal_size(TEMP_C,TEMP_A))
TEMP_AD = stats.pearsonr(TEMP_A, equal_size(TEMP_D,TEMP_A))
TEMP_AE = stats.pearsonr(TEMP_A, equal_size(TEMP_E,TEMP_A))
TEMP_BC = stats.pearsonr(TEMP_B, equal_size(TEMP_C,TEMP_B))
TEMP_BD = stats.pearsonr(TEMP_B, equal_size(TEMP_D,TEMP_B))
TEMP_BE = stats.pearsonr(TEMP_B, equal_size(TEMP_E,TEMP_B))
TEMP_CD = stats.pearsonr(TEMP_C, equal_size(TEMP_D,TEMP_C))
TEMP_CE = stats.pearsonr(TEMP_C, equal_size(TEMP_E,TEMP_C))
TEMP_DE = stats.pearsonr(TEMP_D, equal_size(TEMP_E,TEMP_D))

TEMP_AB_sp = stats.spearmanr(TEMP_A, equal_size(TEMP_B,TEMP_A))
TEMP_AC_sp = stats.spearmanr(TEMP_A, equal_size(TEMP_C,TEMP_A))
TEMP_AD_sp = stats.spearmanr(TEMP_A, equal_size(TEMP_D,TEMP_A))
TEMP_AE_sp = stats.spearmanr(TEMP_A, equal_size(TEMP_E,TEMP_A))
TEMP_BC_sp = stats.spearmanr(TEMP_B, equal_size(TEMP_C,TEMP_B))
TEMP_BD_sp = stats.spearmanr(TEMP_B, equal_size(TEMP_D,TEMP_B))
TEMP_BE_sp = stats.spearmanr(TEMP_B, equal_size(TEMP_E,TEMP_B))
TEMP_CD_sp = stats.spearmanr(TEMP_C, equal_size(TEMP_D,TEMP_C))
TEMP_CE_sp = stats.spearmanr(TEMP_C, equal_size(TEMP_E,TEMP_C))
TEMP_DE_sp = stats.spearmanr(TEMP_D, equal_size(TEMP_E,TEMP_D))

WBGT_AB = stats.pearsonr(WBGT_A, equal_size(WBGT_B,WBGT_A))
WBGT_AC = stats.pearsonr(WBGT_A, equal_size(WBGT_C,WBGT_A))
WBGT_AD = stats.pearsonr(WBGT_A, equal_size(WBGT_D,WBGT_A))
WBGT_AE = stats.pearsonr(WBGT_A, equal_size(WBGT_E,WBGT_A))
WBGT_BC = stats.pearsonr(WBGT_B, equal_size(WBGT_C,WBGT_B))
WBGT_BD = stats.pearsonr(WBGT_B, equal_size(WBGT_D,WBGT_B))
WBGT_BE = stats.pearsonr(WBGT_B, equal_size(WBGT_E,WBGT_B))
WBGT_CD = stats.pearsonr(WBGT_C, equal_size(WBGT_D,WBGT_C))
WBGT_CE = stats.pearsonr(WBGT_C, equal_size(WBGT_E,WBGT_C))
WBGT_DE = stats.pearsonr(WBGT_D, equal_size(WBGT_E,WBGT_D))

WBGT_AB_sp = stats.spearmanr(WBGT_A, equal_size(WBGT_B,WBGT_A))
WBGT_AC_sp = stats.spearmanr(WBGT_A, equal_size(WBGT_C,WBGT_A))
WBGT_AD_sp = stats.spearmanr(WBGT_A, equal_size(WBGT_D,WBGT_A))
WBGT_AE_sp = stats.spearmanr(WBGT_A, equal_size(WBGT_E,WBGT_A))
WBGT_BC_sp = stats.spearmanr(WBGT_B, equal_size(WBGT_C,WBGT_B))
WBGT_BD_sp = stats.spearmanr(WBGT_B, equal_size(WBGT_D,WBGT_B))
WBGT_BE_sp = stats.spearmanr(WBGT_B, equal_size(WBGT_E,WBGT_B))
WBGT_CD_sp = stats.spearmanr(WBGT_C, equal_size(WBGT_D,WBGT_C))
WBGT_CE_sp = stats.spearmanr(WBGT_C, equal_size(WBGT_E,WBGT_C))
WBGT_DE_sp = stats.spearmanr(WBGT_D, equal_size(WBGT_E,WBGT_D))

CS_AB = stats.pearsonr(CS_A, equal_size(CS_B,CS_A))
CS_AC = stats.pearsonr(CS_A, equal_size(CS_C,CS_A))
CS_AD = stats.pearsonr(CS_A, equal_size(CS_D,CS_A))
CS_AE = stats.pearsonr(CS_A, equal_size(CS_E,CS_A))
CS_BC = stats.pearsonr(CS_B, equal_size(CS_C,CS_B))
CS_BD = stats.pearsonr(CS_B, equal_size(CS_D,CS_B))
CS_BE = stats.pearsonr(CS_B, equal_size(CS_E,CS_B))
CS_CD = stats.pearsonr(CS_C, equal_size(CS_D,CS_C))
CS_CE = stats.pearsonr(CS_C, equal_size(CS_E,CS_C))
CS_DE = stats.pearsonr(CS_D, equal_size(CS_E,CS_D))

CS_AB_sp = stats.spearmanr(CS_A, equal_size(CS_B,CS_A))
CS_AC_sp = stats.spearmanr(CS_A, equal_size(CS_C,CS_A))
CS_AD_sp = stats.spearmanr(CS_A, equal_size(CS_D,CS_A))
CS_AE_sp = stats.spearmanr(CS_A, equal_size(CS_E,CS_A))
CS_BC_sp = stats.spearmanr(CS_B, equal_size(CS_C,CS_B))
CS_BD_sp = stats.spearmanr(CS_B, equal_size(CS_D,CS_B))
CS_BE_sp = stats.spearmanr(CS_B, equal_size(CS_E,CS_B))
CS_CD_sp = stats.spearmanr(CS_C, equal_size(CS_D,CS_C))
CS_CE_sp = stats.spearmanr(CS_C, equal_size(CS_E,CS_C))
CS_DE_sp = stats.spearmanr(CS_D, equal_size(CS_E,CS_D))