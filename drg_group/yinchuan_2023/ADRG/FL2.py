from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I20.000","I25.102","I42.200x002","I45.600","I45.600x003","I45.600x004","I45.600x005","I47.100x004","I47.100x005","I47.101","I47.102","I47.104","I47.106","I47.108","I47.200","I47.200x005","I47.200x007","I47.201","I47.203","I48.000","I48.100","I48.100x003","I48.900x003","I48.900x004","I49.100x001","I49.300x002","I49.301","I49.401","I49.500","R94.300x011"]
  adrg_zd1=[]
  adrg_ss=["37.3401","37.3402"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FL2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FL21_group(record):
      return 'FL21'

    if MDCF_DRG.FL23_group(record):
      return 'FL23'

    if MDCF_DRG.FL25_group(record):
      return 'FL25'

    return 'FL2'
  else:
    return ''

