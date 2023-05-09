from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["Z51.000x003","Z51.000x008","Z51.001","Z51.002","Z51.003"]
  adrg_zd1=[]
  adrg_ss=["92.2001","92.2100","92.2400x002","92.2400x003","92.2400x004","92.2400x005","92.2500","92.2700x002","92.2700x004","92.2800","92.2801","92.2900x001","92.2900x003","92.3101","92.3102","92.3201","92.3300"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合RC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCR_DRG.RC19_group(record):
      return 'RC19'

    return 'RC1'
  else:
    return ''

