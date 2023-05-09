from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["F01.100","F01.200","F01.900","F03.x00","F03.x01","G30.000x002","G30.100x003+F00.1*","G30.800","G30.800x001","G30.800x003+F00.2*","G30.900","G30.901+F00.9*","G31.000x005+F02.8*","G31.805+F02.8*","G31.900x009"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BX1入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BX11_group(record):
      return 'BX11'

    if MDCB_DRG.BX13_group(record):
      return 'BX13'

    if MDCB_DRG.BX15_group(record):
      return 'BX15'

    return 'BX1'
  else:
    return ''

