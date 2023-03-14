from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCT_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True:
    message('符合TB1入组条件，匹配规则：')
    
    if MDCT_DRG.TB19_group(record):
      return 'TB19'

    return 'TB1'
  else:
    return ''

