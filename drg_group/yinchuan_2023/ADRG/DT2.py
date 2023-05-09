from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCD_DRG

def group(record):
  adrg_zd=["J04.000","J04.000x004","J04.001","J04.002","J04.100","J05.000","J05.100","J06.000","J36.x00","J36.x00x001","J36.x00x003","J37.000","J37.001","J37.003","J37.005","J38.704","J38.714"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合DT2入组条件，匹配规则：主诊断匹配')
    
    if MDCD_DRG.DT29_group(record):
      return 'DT29'

    return 'DT2'
  else:
    return ''

