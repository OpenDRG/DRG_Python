from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCX_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True:
    message('符合XJ1入组条件，匹配规则：')
    
    if MDCX_DRG.XJ19_group(record):
      return 'XJ19'

    return 'XJ1'
  else:
    return ''

