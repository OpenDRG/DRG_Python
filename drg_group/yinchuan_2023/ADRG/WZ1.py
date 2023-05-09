from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCW_DRG

def group(record):
  adrg_zd=["T20.000x003","T20.003","T20.200","T20.200x002","T20.200x003","T20.201","T21.000","T21.000x031","T21.200","T21.200x021","T21.200x031","T21.200x041","T21.200x042","T21.200x055","T21.200x057","T21.600x054","T22.000x002","T22.000x003","T22.000x005","T22.200x001","T22.200x002","T22.200x003","T22.200x005","T23.000x001","T23.000x003","T23.000x004","T23.000x006","T23.200","T23.200x002","T23.200x003","T23.600x003","T24.000x003","T24.000x004","T24.100x003","T24.200x001","T24.200x003","T24.200x004","T25.000","T25.000x002","T25.000x003","T25.200","T25.200x002","T25.200x003","T25.600x003","T29.000","T29.200x001","T30.000","T30.200"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合WZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCW_DRG.WZ13_group(record):
      return 'WZ13'

    if MDCW_DRG.WZ15_group(record):
      return 'WZ15'

    return 'WZ1'
  else:
    return ''

