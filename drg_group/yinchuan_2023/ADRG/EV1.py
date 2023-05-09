from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["R04.200","R04.800x002","R04.900","R05.x00","R05.x01","R06.000","R06.200","R06.400","R06.600","R06.801","R06.802","R06.804","R06.805","R09.000","R09.801","R91.x00x001","R91.x03","R94.204"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合EV1入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.EV11_group(record):
      return 'EV11'

    if MDCE_DRG.EV13_group(record):
      return 'EV13'

    if MDCE_DRG.EV15_group(record):
      return 'EV15'

    return 'EV1'
  else:
    return ''

