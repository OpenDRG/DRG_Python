from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=["E10.300x034+H36.0*","E10.301+H36.0*","E11.300x011+H36.0*","E11.300x031+H36.0*","E11.301+H36.0*","E14.300x031+H36.0*","E14.300x032+H36.0*","E14.300x071+H36.0*","H35.004"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合CX1入组条件，匹配规则：主诊断匹配')
    
    if MDCC_DRG.CX19_group(record):
      return 'CX19'

    return 'CX1'
  else:
    return ''

