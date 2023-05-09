from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["C79.900x001","C97.x00","C97.x01","D47.401","Z08.000","Z51.003","Z51.102","Z51.103","Z51.800x092","Z51.800x097","Z51.801","Z51.806"]
  adrg_zd1=[]
  adrg_ss=["32.2400x001","39.7900x019","39.7900x020","39.7900x025","39.7903","39.7904","39.7906","50.2301","50.2302","50.2401","50.2402","50.2403","50.2404","68.2500x001","99.2501"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合RD1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCR_DRG.RD11_group(record):
      return 'RD11'

    if MDCR_DRG.RD13_group(record):
      return 'RD13'

    if MDCR_DRG.RD15_group(record):
      return 'RD15'

    return 'RD1'
  else:
    return ''

