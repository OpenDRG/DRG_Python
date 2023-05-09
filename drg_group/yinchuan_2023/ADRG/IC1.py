from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["M06.900","M17.000","M17.101","M17.900","M17.900x003","M17.900x004","M65.906","M87.800x051","M94.300","T84.000x005","T84.000x006","T84.000x008","T84.002","T84.003","T84.004","T84.201","T84.502","T84.806","Z45.800x011"]
  adrg_zd1=[]
  adrg_ss=["00.7000x001","00.7100x001","00.7300x001","00.7301","00.8000x001","00.8100x001","00.8200x001","00.8201","00.8400x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合IC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCI_DRG.IC19_group(record):
      return 'IC19'

    return 'IC1'
  else:
    return ''

