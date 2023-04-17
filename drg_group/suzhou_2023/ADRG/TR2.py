from drg_group.suzhou_2023.Base import message,intersect,SS_VALID
from drg_group.suzhou_2023.DRG import MDCT_DRG

def group(record):
  adrg_zd=["F22.000","F22.001","F22.002","F22.003","F22.800","F22.800x001","F22.900","F23.000","F23.001","F23.002","F23.200x003","F23.200x011","F23.300x001","F23.300x002","F23.300x003","F23.301","F23.800","F23.900","F23.901","F23.902","F23.903","F24.x00","F28.x00x002","F28.x00x011","F28.x00x012","F28.x01","F28.x02"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合TR2入组条件，匹配规则：主诊断匹配')
    
    if MDCT_DRG.TR29_group(record):
      return 'TR29'

  return ''

