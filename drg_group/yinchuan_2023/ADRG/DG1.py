from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCD_DRG

def group(record):
  adrg_zd=["A18.200x002","C02.100","C02.900","D10.300x007","D11.000","D11.701","D17.001","D18.000x807","D18.100x010","D36.703","D37.010","D37.011","I88.101","K09.801","K10.200","K11.200x009","K11.202","K11.205","K11.206","K11.209","K11.210","K11.211","K11.301","K11.302","K11.503","K11.601","K11.603","K11.605","K11.800","K11.805","K11.901","K11.903","K13.205","K14.901","Q18.002"]
  adrg_zd1=[]
  adrg_ss=["25.2x00","26.0x01","26.2901","26.2903","26.2904","26.2905","26.2906","26.3100x008","26.3100x009","26.3101","26.3102","26.3103","26.3104","26.3201","26.3202","26.3203","26.9900x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合DG1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCD_DRG.DG19_group(record):
      return 'DG19'

    return 'DG1'
  else:
    return ''

