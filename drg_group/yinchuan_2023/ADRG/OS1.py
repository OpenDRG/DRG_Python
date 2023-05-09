from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCO_DRG

def group(record):
  adrg_zd=["O15.201","O72.201","O72.202","O72.300","O72.301","O73.000","O73.002","O73.102","O85.x00x006","O85.x01","O85.x03","O86.000","O86.002","O86.201","O86.400x001","O86.401","O86.402","O86.802","O90.300","O90.800x007","O90.800x008","O90.800x009","O90.801","O90.802","O90.900","O91.101","O91.102","O91.201","O99.000x031","O99.200x014","O99.401","O99.402","O99.600x016","Z39.000x001","Z39.000x021"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合OS1入组条件，匹配规则：主诊断匹配')
    
    if MDCO_DRG.OS13_group(record):
      return 'OS13'

    if MDCO_DRG.OS15_group(record):
      return 'OS15'

    return 'OS1'
  else:
    return ''

