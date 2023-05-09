from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I33.000x004","I33.002","I33.003","I33.006","T82.703"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合FT2入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FT29_group(record):
      return 'FT29'

    return 'FT2'
  else:
    return ''

