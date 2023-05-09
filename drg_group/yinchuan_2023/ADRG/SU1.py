from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCS_DRG

def group(record):
  adrg_zd=["A97.000","A98.400","B00.901","B00.902","B01.900x001","B02.700","B02.900x002","B02.900x003","B05.800x010","B06.900x001","B08.401","B25.900x001","B25.900x002","B27.001","B27.100","B27.800","B27.900x001","B34.100","B34.400x002","B34.800x002","B34.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合SU1入组条件，匹配规则：主诊断匹配')
    
    if MDCS_DRG.SU19_group(record):
      return 'SU19'

    return 'SU1'
  else:
    return ''

