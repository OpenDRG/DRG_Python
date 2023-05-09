from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.ADRG import AH1

def group(record):
  mdc_zd=[]
  dept_list=[]
  if not (True and record.ssList and record.ssList[0] in SS_VALID):
    return ''
  
  message('符合MDCA入组条件，匹配规则：存在手术')

  result=AH1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合AQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'AQY'

  message('不符合MDCA的ADRG入组条件')

