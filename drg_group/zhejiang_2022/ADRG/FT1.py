from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=["E11.502+I79.2*","E14.500x031+I43.8*","E14.500x032+I43.8*","E63.901+I43.2*","E83.103","E88.907+I43.1*","I25.500","I42.000x001","I42.001","I42.100","I42.200x002","I42.201","I42.401","I42.500x001","I42.501","I42.600","I42.701","I42.800x002","I42.800x004","I42.800x005","I42.800x006","I42.800x007","I42.800x008","I42.802","I42.803","I42.900","I42.901","I42.902","I42.904","I42.905","I51.500x006","M32.104+I43.8*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and (not record.ssList or not record.ssList[0] in SS_VALID):
    message('符合FT1入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FT11_group(record):
      return 'FT11'

    if MDCF_DRG.FT13_group(record):
      return 'FT13'

    if MDCF_DRG.FT15_group(record):
      return 'FT15'

    return ''
  else:
    return ''

