from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["S06.200x011","S06.202","S06.204","S06.300x031","S06.400","S06.401","S06.500","S06.500x002","S06.502","S06.700x002","S06.700x003","S06.700x004","S06.802"]
  adrg_zd1=[]
  adrg_ss=["01.2400x005","01.2400x013","01.2405","01.2408","01.2413","01.3104","01.3105","01.3108","01.3900x009","01.3904","01.3910","02.1209"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合BB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCB_DRG.BB11_group(record):
      return 'BB11'

    if MDCB_DRG.BB13_group(record):
      return 'BB13'

    if MDCB_DRG.BB15_group(record):
      return 'BB15'

    return 'BB1'
  else:
    return ''

