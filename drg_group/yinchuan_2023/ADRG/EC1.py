from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["A15.000x001","A15.814","A16.402","A16.501","A16.504","C34.000","C34.300x004","C37.x00","C38.100","C38.300","C38.400","C45.000","C49.300x003","C76.100","C76.100x003","C77.103","C79.800x809","D15.000","D15.200","D15.200x001","D15.200x002","D15.701","D17.400x001","D17.400x005","D36.717","D38.300x002","D38.301","D38.400x001","D38.401","D48.115","E32.001","E32.801","J16.000","J39.804","J39.805","J86.902","J94.800x004","J98.011","J98.417","J98.504","J98.505","J98.507","J98.901","Q85.900x015","R93.805"]
  adrg_zd1=[]
  adrg_ss=["07.8000","07.8001","07.8300","07.8300x002","07.8400","07.8401","31.5x00x012","31.5x04","34.3x02","34.3x04","34.3x05","34.4x01","34.5902","34.5904","34.8101","37.3102","53.8000x001","96.5601"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合EC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCE_DRG.EC11_group(record):
      return 'EC11'

    if MDCE_DRG.EC13_group(record):
      return 'EC13'

    if MDCE_DRG.EC15_group(record):
      return 'EC15'

    return 'EC1'
  else:
    return ''

