from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCN_DRG

def group(record):
  adrg_zd=["C45.100","C51.800","C51.900","C52.x00","C53.100","C53.801","C53.900","C54.100","C54.200","C54.900","C55.x00","C56.x00","C57.000","C57.803","C58.x00","C58.x00x002","C79.814","C79.821","D06.000","D06.100","D06.900","D06.900x002","D07.000","D07.100x002","D07.200x002"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合NR1入组条件，匹配规则：主诊断匹配')
    
    if MDCN_DRG.NR11_group(record):
      return 'NR11'

    if MDCN_DRG.NR13_group(record):
      return 'NR13'

    if MDCN_DRG.NR15_group(record):
      return 'NR15'

    return 'NR1'
  else:
    return ''

