from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["A17.000+G01*","A17.803+G05.0*","A17.806+G07*","A23.900x005+G05.0*","A32.102+G05.0*","A52.100x010+G05.0*","A89.x00","B02.200x004+G53.0*","B02.200x008+G63.0*","B02.201+G53.0*","B02.202+G53.0*","B02.203+G53.0*","B02.206+G53.0*","B02.207+G53.0*","G00.200","G00.900","G00.901","G00.902","G03.800","G03.800x004","G03.802","G03.900","G04.800x003","G04.800x008","G04.805","G04.807","G04.900x005","G04.900x010","G04.900x025","G04.904","G04.905","G04.908","G04.911","G04.913","G04.919","G04.921","G06.000x002","G06.000x022","G06.001","G06.006","G06.100x002","G06.101","G06.201","G08.x01","G09.x00x002","G09.x00x003"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BT2入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BT21_group(record):
      return 'BT21'

    if MDCB_DRG.BT23_group(record):
      return 'BT23'

    if MDCB_DRG.BT25_group(record):
      return 'BT25'

    return 'BT2'
  else:
    return ''

