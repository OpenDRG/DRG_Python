from drg_group.anyang_2021.Base import message,intersect,SS_VALID
from drg_group.anyang_2021.DRG import MDCZ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and not intersect(record.ssList,SS_VALID):
    message('符合ZZ1入组条件，匹配规则：无手术')
    
    if MDCZ_DRG.ZZ11_group(record):
      return 'ZZ11'

    if MDCZ_DRG.ZZ1B_group(record):
      return 'ZZ14'

    return ''
  else:
    return ''

