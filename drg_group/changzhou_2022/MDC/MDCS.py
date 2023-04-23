from drg_group.changzhou_2022.Base import message,intersect,SS_VALID
from drg_group.changzhou_2022.ADRG import SB1,SR1,SS1,ST1,SU1,SV1,SZ1

def group(record):
  mdc_zd=[]
  dept_list=[]
  if not (True):
    return ''
  
  message('符合MDCS入组条件，匹配规则：无限制条件')

  result=SB1.group(record)
  if result:
    return result

  if False and record.ssList and record.ssList[0] in SS_VALID:
    message('符合SQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'SQY'

  result=SR1.group(record)
  if result:
    return result

  result=SS1.group(record)
  if result:
    return result

  result=ST1.group(record)
  if result:
    return result

  result=SU1.group(record)
  if result:
    return result

  result=SV1.group(record)
  if result:
    return result

  result=SZ1.group(record)
  if result:
    return result

  message('不符合MDCS的ADRG入组条件')

