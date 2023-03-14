from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.ADRG import YC1,YR1,YR2

def group(record):
  mdc_zd=["B20.000x001","B20.001","B20.002","B20.003","B20.004","B20.005","B20.006","B20.100x001","B20.200x001","B20.300x001","B20.301","B20.400x001","B20.500x001","B20.600x001","B20.700x001","B20.801","B20.901","B21.000x001","B21.100x001","B21.200x001","B21.300","B21.700","B21.800","B21.900","B22.000x001","B22.000x003","B22.000x004","B22.000x005","B22.001+F02.4*","B22.100","B22.200","B22.700","B22.701","B23.000","B23.100","B23.100x001","B23.100x002","B23.200","B23.201","B23.800","B23.800x001","B23.800x002","B23.801","B24.x01","I33.000x018","O98.700","R75.x00x001","Z20.600","Z21.x00x001"]
  dept_list=[]
  if not (True and intersect(record.zdList,mdc_zd)):
    return ''
  
  message('符合MDCY入组条件，匹配规则：某一诊断匹配')

  result=YC1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合YQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'YQY'

  result=YR1.group(record)
  if result:
    return result

  result=YR2.group(record)
  if result:
    return result

  message('不符合MDCY的ADRG入组条件')

