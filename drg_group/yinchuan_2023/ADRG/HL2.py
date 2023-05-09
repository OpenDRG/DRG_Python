from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["C22.000","C22.001","C22.100","C22.101","C22.700","C22.900","C23.x00","C24.000","C24.000x007","C24.001","C24.002","C24.003","C24.004","C24.100","C24.101","C24.900","C25.000","C25.100","C25.200","C25.300","C25.400","C25.701","C25.800x001","C25.801","C25.802","C25.803","C25.900","C77.203","C78.700","C78.806","C78.808","D01.500x001","D01.501","D01.701","D13.600","K72.100","K80.300x005","K80.301","K80.302","K80.303","K80.304","K80.306","K80.401","K80.402","K80.500x002","K80.501","K80.503","K83.000x007","K83.001","K83.005","K83.107","K83.109","K83.804","K83.817","K83.901","K85.101","K85.102","K85.900","K85.902","K86.800x002","K86.809","K86.810","K92.800x006","K92.800x012"]
  adrg_zd1=[]
  adrg_ss=["51.1000","51.1100","51.1104","51.1105","52.1303"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合HL2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCH_DRG.HL29_group(record):
      return 'HL29'

    return 'HL2'
  else:
    return ''

