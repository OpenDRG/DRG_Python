from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=["B49.x04+H19.2*","C69.300","D18.000x804","D31.600","D31.601","E05.002+H06.2*","H00.100","H02.000","H02.300","H02.400","H02.802","H02.812","H04.000","H04.003","H04.102","H04.105","H04.900","H04.900x001","H05.101","H05.103","H05.800x003","H05.801","H05.802","H05.900x002","H05.901","H11.401","H15.803","H16.000","H16.001","H16.003","H16.007","H16.205","H18.701","H40.501","H40.900","H44.000x005","H44.501","H44.502","S02.801","S05.201","S05.300x004","S05.400x001","S05.601"]
  adrg_zd1=[]
  adrg_ss=["09.2100","09.2200x001","09.3x00x001","09.3x01","09.3x02","16.0901","16.0904","16.1x01","16.3100x001","16.3900x001","16.4100x002","16.4200x001","16.4900x001","16.5900x001","16.6101","16.6200x001","16.6300x002","16.8100x002","16.8200","16.8903","16.8904","16.9200","16.9201","16.9300x003","76.4501","76.4600x004","76.7900x001","76.9100x009"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合CD2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCC_DRG.CD29_group(record):
      return 'CD29'

    return 'CD2'
  else:
    return ''

