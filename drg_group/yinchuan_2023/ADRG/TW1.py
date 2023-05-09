from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCT_DRG

def group(record):
  adrg_zd=["F05.000x001","F05.101","F06.300x020","F06.700","F06.800x021","F06.800x026","F06.800x027","F07.100","F07.200","F07.201","F07.900","F09.x01","F09.x02","F99.x00"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合TW1入组条件，匹配规则：主诊断匹配')
    
    if MDCT_DRG.TW11_group(record):
      return 'TW11'

    if MDCT_DRG.TW13_group(record):
      return 'TW13'

    if MDCT_DRG.TW15_group(record):
      return 'TW15'

    return 'TW1'
  else:
    return ''

