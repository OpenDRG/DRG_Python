from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCQ_DRG

def group(record):
  adrg_zd=["C78.805","D18.100x002","D18.100x006","D18.100x024","D18.103","D18.104","D21.900x015","D53.100","D64.901","D64.903","D73.100","D73.300","D86.100","I88.900x005","I88.900x006","L04.202","L04.900","L04.900x002","L04.901","L04.902","N18.500x001+D63.8*","R16.100x001","R59.005","R59.014","S36.002"]
  adrg_zd1=[]
  adrg_ss=["20.5100x002","26.2901","26.3203","27.4902","27.9902","34.0401","39.7904","40.0x00x001","40.2400","40.2900x002","40.2900x019","40.2900x020","40.2910","40.3x00x002","40.4100","40.5400x001","40.5914","40.9x00x016","41.1x00","51.2300","54.1101","54.2100","54.3x03","54.4x02","54.4x15","68.2912"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合QJ1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCQ_DRG.QJ13_group(record):
      return 'QJ13'

    if MDCQ_DRG.QJ15_group(record):
      return 'QJ15'

    return 'QJ1'
  else:
    return ''

