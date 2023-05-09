from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCM_DRG

def group(record):
  adrg_zd=["A18.117+N51.1*","A18.118+N51.1*","D29.400","I86.101","N43.300","N43.301","N43.302","N43.400","N44.x00","N44.x01","N45.000","N45.001","N45.903","N45.904","N45.905","N45.906","N45.907","N45.908","N49.204","N49.205","N50.000","N50.802","N50.803","N50.807","N50.810","N50.811","N50.827","N50.901","Q53.100","Q53.101","Q53.102","Q53.200","Q53.201","Q53.202","Q53.900","Q53.901","Q53.902","Q54.900","Q55.202","Q55.606","S30.205","S30.208","S31.300x001","S39.900x007","S39.900x010"]
  adrg_zd1=[]
  adrg_ss=["61.2x01","61.2x02","61.4102","61.9101","61.9200x001","62.0x00x001","62.0x01","62.0x02","62.1200","62.2x00x002","62.2x01","62.3x00","62.3x01","62.3x03","62.3x04","62.4100x004","62.4101","62.4200","62.5x00","62.5x01","62.5x02","62.6100","62.6900x001","63.1x00x003","63.1x01","63.1x02","63.1x03","63.2x00","63.2x01","63.4x00","63.5201","63.5202","63.5203","63.5900","63.9200x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合MD1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCM_DRG.MD13_group(record):
      return 'MD13'

    if MDCM_DRG.MD15_group(record):
      return 'MD15'

    return 'MD1'
  else:
    return ''

