from drg_group.haerbin_2022.Base import message,intersect,SS_VALID
from drg_group.haerbin_2022.DRG import MDCE_DRG

def group(record):
  adrg_zd=["A36.201","A37.000","A37.100","A37.800x001","A37.900","A37.900x003","A37.900x004","A37.901+J17.0*","J20.000","J20.100","J20.200","J20.300","J20.400","J20.500","J20.600","J20.700","J20.800","J20.900","J20.901","J20.902","J21.000","J21.100","J21.801","J21.900","J21.900x002","J21.901","J39.803","J40.x00","J40.x00x002","J40.x01","J44.800x001","T17.501"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合EX2入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.EX2A_group(record):
      return 'EX2A'

    if MDCE_DRG.EX25_group(record):
      return 'EX25'

    return ''
  else:
    return ''

