from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["A18.000x015+M01.1*","A18.014+M90.0*","A18.015+M90.0*","A18.021+M90.0*","A18.024+M90.0*","E85.900","K52.913+M07.6*","L40.501+M07.3*","L87.100","M02.800","M05.308","M05.800","M06.003","M06.100","M06.300","M06.901","M06.902","M06.903","M06.904","M06.907","M08.100","M08.900","M11.800x093","M12.300","M30.000","M30.004","M30.100x001","M30.101","M30.300","M30.301","M31.802","M31.900x001","M32.800","M32.900","M33.100x004","M33.101","M33.104","M33.200","M33.900","M34.805","M34.900","M34.900x001","M35.001","M35.101","M35.200","M35.201","M35.203","M35.300","M35.400","M35.800x001","M35.901","M35.906","M35.907","M45.x00","M45.x01","M45.x03+H22.1*","M60.900","M60.901","M60.902","M79.810"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合IT2入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IT21_group(record):
      return 'IT21'

    if MDCI_DRG.IT23_group(record):
      return 'IT23'

    if MDCI_DRG.IT25_group(record):
      return 'IT25'

    return 'IT2'
  else:
    return ''

