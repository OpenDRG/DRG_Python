from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["C44.900","D17.000x004","D17.100x001","D17.200x004","D17.300x005","D17.900x002","D18.006","D22.900x002","L02.200","L57.000","L72.000","L72.101","L72.105","L72.902","L81.400","L82.x00","L85.801","L90.500x016","L90.502","L91.001","L98.701","R22.005","R22.902"]
  adrg_zd1=[]
  adrg_ss=["08.2000x005","08.2000x006","08.2001","08.5900x004","08.5900x005","08.5902","08.6101","18.7100x001","27.5903","27.5911","27.5913","27.9900x005","86.8201","86.8300x031","86.8300x032","86.8301","86.8900x002","86.8901"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合JC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCJ_DRG.JC19_group(record):
      return 'JC19'

    return 'JC1'
  else:
    return ''

