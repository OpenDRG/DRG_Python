from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=["C74.900","D17.700x029","D35.000","D35.001","D44.101","E26.000","E27.801","E27.805","E27.901"]
  adrg_zd1=[]
  adrg_ss=["07.2100","07.2102","07.2200","07.2201","07.2900x003","07.2901","07.2902"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合KB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCK_DRG.KB19_group(record):
      return 'KB19'

    return 'KB1'
  else:
    return ''

