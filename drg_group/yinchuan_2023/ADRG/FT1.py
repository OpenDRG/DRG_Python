from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["E05.900x004+I43.8*","E10.502+I79.2*","E11.502+I79.2*","E14.500x031+I43.8*","E63.901+I43.2*","E74.006+K77.8*","E85.416+I43.1*","E88.907+I43.1*","I09.000","I25.500","I40.000x005","I40.001","I40.900","I42.001","I42.100","I42.200x002","I42.201","I42.500x001","I42.800x002","I42.800x006","I42.800x007","I42.803","I42.900","I50.906","I51.400","I51.403","M32.104+I43.8*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合FT1入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FT11_group(record):
      return 'FT11'

    if MDCF_DRG.FT13_group(record):
      return 'FT13'

    if MDCF_DRG.FT15_group(record):
      return 'FT15'

    return 'FT1'
  else:
    return ''

