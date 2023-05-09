from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCW_DRG

def group(record):
  adrg_zd=["T21.300x041","T21.300x054","T22.300x002","T22.300x005","T23.300x003","T24.000x002","T24.200x004","T24.300x003","T24.300x004","T25.300","T25.300x003","T29.000","T29.300x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合WJ1入组条件，匹配规则：主诊断匹配')
    
    if MDCW_DRG.WJ19_group(record):
      return 'WJ19'

    return 'WJ1'
  else:
    return ''

