from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCV_DRG

def group(record):
  adrg_zd=["S51.000","S61.000x001","S61.000x002","S61.100x001","S61.100x002","S61.700","S61.800x012","S67.801","S68.100x002","S69.900x001","S69.900x003","S69.900x004","S81.000","S81.800x081","S91.300x002","S91.300x003","S98.100x001","T01.902","T81.800x017","T81.811","T81.813"]
  adrg_zd1=[]
  adrg_ss=["86.6101","86.6200x002","86.6202","86.6303","86.6304","86.6701","86.6900x010","86.6902","86.6906","86.7100x009","86.7105","86.7200x001","86.7300x003","86.7300x004","86.7301","86.7400x026","86.7400x036","86.7401","86.7402","86.7500x001","86.7500x011","86.7503"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合VB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCV_DRG.VB19_group(record):
      return 'VB19'

    return 'VB1'
  else:
    return ''

