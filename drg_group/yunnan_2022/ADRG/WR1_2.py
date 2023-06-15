from drg_group.yunnan_2022.Base import message,intersect,SS_VALID
from drg_group.yunnan_2022.DRG import MDCW_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=["T31.300","T31.400","T31.500","T31.600","T31.700","T31.800","T31.900","T32.300","T32.400","T32.500","T32.600","T32.700","T32.800","T32.900"]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and intersect(record.zdList[1:],adrg_zd1):
    message('符合WR1_2入组条件，匹配规则：其他诊断匹配')
    
    
    if MDCW_DRG.WR11_group(record):
      return 'WR11'

    if MDCW_DRG.WR15_group(record):
      return 'WR15'

    return ''
  else:
    return ''
