from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["A18.000x046+M68.0*","A18.000x053+M01.1*","A18.027+M01.1*","A18.028+M01.1*","A18.029+M01.1*","A18.031+M01.1*","A18.034+M01.1*","A18.036+M01.1*","A18.044+M01.1*","A23.902+M01.3*","A52.103+M14.6*","A54.401+M01.3*","M00.004","M00.005","M00.200x001","M00.200x091","M00.900","M00.900x011","M00.900x051","M00.900x061","M00.901"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合IT3入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IT39_group(record):
      return 'IT39'

    return 'IT3'
  else:
    return ''

