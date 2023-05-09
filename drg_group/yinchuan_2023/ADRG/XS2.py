from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCX_DRG

def group(record):
  adrg_zd=["R74.804","Z00.500x001","Z04.800","Z09.000x001","Z09.400","Z09.801","Z09.804","Z09.900x001","Z51.901"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合XS2入组条件，匹配规则：主诊断匹配')
    
    if MDCX_DRG.XS21_group(record):
      return 'XS21'

    if MDCX_DRG.XS25_group(record):
      return 'XS25'

    return 'XS2'
  else:
    return ''

