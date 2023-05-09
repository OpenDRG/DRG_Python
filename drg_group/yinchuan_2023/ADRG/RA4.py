from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["C76.306","C90.000x024","C90.000x026","C90.000x027","C90.000x030","C90.000x036","C90.000x037","C90.001","C90.002","C90.302","C90.303"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合RA4入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RA49_group(record):
      return 'RA49'

    return 'RA4'
  else:
    return ''

