from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=["C73.x00","C73.x00x003","C74.900","C75.900","C79.700","D17.700x029","D34.x00","D34.x00x005","D35.000","D35.001","D35.100","D35.200","D35.200x004","D35.200x007","D35.200x008","D35.200x009","D35.200x010","D44.001","D44.101","D44.301","D44.802"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合KR1入组条件，匹配规则：主诊断匹配')
    
    if MDCK_DRG.KR19_group(record):
      return 'KR19'

    return 'KR1'
  else:
    return ''

