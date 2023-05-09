from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCD_DRG

def group(record):
  adrg_zd=["H61.100x009","H61.102","H61.300","H61.803","J34.200","J34.800x009","K13.709","M95.207","S00.001","S00.002","S00.003","S00.004","S00.801","S00.803","S01.000","S01.001","S01.200x031","S01.200x092","S01.300x012","S01.401","S01.500x051","S01.500x052","S01.501","S01.502","S01.503","S01.504","S01.506","S01.802","S02.200","S02.211","S02.400x001","S02.400x003","S02.400x005","S02.600","S02.600x011","S02.802","S08.000","S09.200","S09.900","S09.901","S09.903","S10.003","S10.101","S10.102","S10.801","S10.901","S10.902","S11.900","S13.400","S13.401","S13.402","S13.403","S13.500x009","S13.601","S19.802","S19.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合DU1入组条件，匹配规则：主诊断匹配')
    
    if MDCD_DRG.DU19_group(record):
      return 'DU19'

    return 'DU1'
  else:
    return ''

