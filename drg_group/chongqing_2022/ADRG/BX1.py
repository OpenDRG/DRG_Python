from drg_group.chongqing_2022.Base import message,intersect,SS_VALID
from drg_group.chongqing_2022.DRG import MDCB_DRG

def group(record):
  adrg_zd=["F01.000","F01.100","F01.102","F01.200","F01.300","F01.800x001","F01.900","F01.901","F01.902","F03.x00","F03.x01","G10.x00","G10.x01+F02.2*","G93.804","M30.005+F02.8*","N18.502+F02.8*"]
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

    return ''
  else:
    return ''
