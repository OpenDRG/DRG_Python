from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCT_DRG

def group(record):
  adrg_zd=["F41.001","F41.101","F41.102","F41.200x002","F41.201","F41.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合TV1入组条件，匹配规则：主诊断匹配')
    
    if MDCT_DRG.TV19_group(record):
      return 'TV19'

    return 'TV1'
  else:
    return ''

