from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["J43.902","J90.x00","J90.x00x002","J90.x00x003","J90.x02","J93.003","J93.100x001","J93.100x002","J93.800x001","J93.900","J94.201","J94.801","J94.802","J94.804","J94.901","J98.201","R09.100"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合EW1入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.EW11_group(record):
      return 'EW11'

    if MDCE_DRG.EW13_group(record):
      return 'EW13'

    if MDCE_DRG.EW15_group(record):
      return 'EW15'

    return 'EW1'
  else:
    return ''

