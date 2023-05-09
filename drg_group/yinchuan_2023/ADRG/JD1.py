from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["C44.506","C44.900","D24.x00","L05.000","L05.900","L08.900","L08.901","L08.902","L08.903","L08.904","L08.910","L08.911","L66.900","L85.900x001","L89.200","L89.300","L89.308","L90.500x006","L90.500x010","L90.500x048","L90.500x052","L90.500x061","L90.500x062","L90.501","L90.502","L91.001","L91.800","L97.x00","M31.000x005","N60.201","N60.400","S60.000x001","S60.100x001","S60.202","T14.001","T14.101","Z42.300x001","Z42.302","Z42.304"]
  adrg_zd1=[]
  adrg_ss=["86.6101","86.6200x002","86.6304","86.6701","86.6900x010","86.6901","86.6902","86.6906","86.700x0013","86.700x0014","86.7101","86.7102","86.7105","86.7303","86.7400x026","86.7400x031","86.7503","86.7504","86.9100x002","86.9301"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合JD1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCJ_DRG.JD11_group(record):
      return 'JD11'

    if MDCJ_DRG.JD13_group(record):
      return 'JD13'

    if MDCJ_DRG.JD15_group(record):
      return 'JD15'

    return 'JD1'
  else:
    return ''

