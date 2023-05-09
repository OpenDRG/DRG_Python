from drg_group.liaocheng_2022.Base import message,intersect,SS_VALID
from drg_group.liaocheng_2022.DRG import MDCE_DRG

def group(record):
  adrg_zd=["J68.101","J80.x00","J80.x01","J81.x00","J81.x00x002","J95.100","J95.200","J95.300","J95.800x004","J95.811","J96.000","J96.100","J96.900x001","J96.900x002","J96.900x003"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合ER3入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.ER35_group(record):
      return 'ER35'

    if MDCE_DRG.ER31_group(record):
      return 'ER31'

    if MDCE_DRG.ER33_group(record):
      return 'ER33'

    return 'ER3'
  else:
    return ''

