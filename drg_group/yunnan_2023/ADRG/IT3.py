from drg_group.yunnan_2023.Base import message,intersect,SS_VALID
from drg_group.yunnan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["A02.202+M01.3*","A18.000x019+M01.1*","A18.000x046+M68.0*","A18.000x053+M01.1*","A18.002+M01.1*","A18.027+M01.1*","A18.028+M01.1*","A18.029+M01.1*","A18.030+M01.1*","A18.031+M01.1*","A18.032+M49.0*","A18.033+M01.1*","A18.034+M01.1*","A18.035+M01.1*","A18.036+M01.1*","A18.037+M01.1*","A18.038+M01.1*","A18.039+M01.1*","A18.040+M01.1*","A18.043+M01.1*","A18.044+M01.1*","A23.902+M01.3*","A39.804+M01.0*","A39.805+M03.0*","A52.103+M14.6*","A52.706+M01.3*","A54.401+M01.3*","A69.900x002+M01.8*","B06.802+M01.4*","B26.800x001+M01.5*","B37.800x089+M01.6*","B49.x19+M01.6*","M00.000x091","M00.000x092","M00.001","M00.002","M00.003","M00.004","M00.005","M00.006","M00.100x001","M00.100x011","M00.100x021","M00.100x031","M00.100x051","M00.100x061","M00.100x071","M00.100x091","M00.200x001","M00.200x011","M00.200x021","M00.200x031","M00.200x051","M00.200x061","M00.200x071","M00.200x091","M00.900","M00.900x011","M00.900x021","M00.900x031","M00.900x051","M00.900x061","M00.900x071","M00.901"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合IT3入组条件，匹配规则：主诊断匹配')
    
    
    if MDCI_DRG.IT31_group(record):
      return 'IT31'

    if MDCI_DRG.IT33_group(record):
      return 'IT33'

    if MDCI_DRG.IT35_group(record):
      return 'IT35'

    return ''
  else:
    return ''
