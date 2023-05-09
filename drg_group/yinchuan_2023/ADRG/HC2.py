from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["B67.800x001+K77.0*","C23.x00","C24.101","C25.900","D13.501","K75.000","K75.001","K75.003","K80.000x002","K80.000x004","K80.001","K80.002","K80.100x001","K80.101","K80.200x001","K80.200x003","K80.201","K80.203","K80.300x002","K80.300x005","K80.301","K80.302","K80.303","K80.304","K80.305","K80.401","K80.402","K80.404","K80.500x002","K80.501","K80.801","K81.000","K81.002","K81.003","K81.006","K81.100","K81.900","K82.200","K82.802","K82.803","K82.807","K83.000x007","K83.001","K83.005","K83.109","K85.101","K85.102","K85.807","K85.900","K85.902","K86.100x004"]
  adrg_zd1=[]
  adrg_ss=["51.2100","51.2101","51.2200","51.2200x004","51.2201","51.2300","51.2301","51.2400","51.2401"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合HC2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCH_DRG.HC29_group(record):
      return 'HC29'

    return 'HC2'
  else:
    return ''

