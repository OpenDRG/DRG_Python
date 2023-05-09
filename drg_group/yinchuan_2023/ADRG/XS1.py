from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCX_DRG

def group(record):
  adrg_zd=["R11.x01","R11.x02","R11.x03","R17.000","R17.001","R18.x00","R18.x00x001","R18.x00x005","R19.000x008","R19.000x016","R19.001","R19.002","R23.000","R23.101","R52.100","R52.200","R52.900","R52.901","R53.x00x002","R53.x00x009","R54.x01","R60.000","R60.001","R60.100","R60.900","R61.000","R61.900","R61.901","R63.000","R63.400","R64.x00x002","R68.300","R72.x00x002","R74.000x001","R74.800x007","R74.803","R76.000x001","R76.801","R76.802","R77.800x002","R77.800x003","R77.800x006","R77.802","R77.803","R79.800x003","R79.900","R87.900x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合XS1入组条件，匹配规则：主诊断匹配')
    
    if MDCX_DRG.XS11_group(record):
      return 'XS11'

    if MDCX_DRG.XS15_group(record):
      return 'XS15'

    return 'XS1'
  else:
    return ''

