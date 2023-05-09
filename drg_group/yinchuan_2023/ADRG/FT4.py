from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["A18.808+I32.0*","A18.809+I32.0*","I30.103","I30.900","I31.100","I31.200x001","I31.300","I31.901","M32.105+I32.8*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合FT4入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FT43_group(record):
      return 'FT43'

    if MDCF_DRG.FT45_group(record):
      return 'FT45'

    return 'FT4'
  else:
    return ''

