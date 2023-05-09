from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCD_DRG

def group(record):
  adrg_zd=["C00.100","G47.300","G47.300x001","G47.300x036","G47.300x037","G47.301","J03.900","J32.803","J34.200","J35.000","J35.200","K04.600","K07.500x002","K09.800x005","K11.503","K11.807","K12.117","K12.206","K13.002","K13.004","K13.010","K13.702","K13.709","Q35.100","Q35.300","Q35.302","Q35.900","Q35.901","Q35.902","Q35.903","Q35.907","Q36.001","Q36.900","Q36.902","Q36.904","Q36.905","Q36.906","R06.501","S01.500x051","S01.500x052","Z42.006","Z42.007"]
  adrg_zd1=[]
  adrg_ss=["27.5302","27.5303","27.5400","27.5401","27.5900x018","27.5903","27.5909","27.5912","27.5913","27.6100","27.6200x003","27.6201","27.6301","27.6900x007","27.6902","27.6906","27.6908","27.9101"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合DB3入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCD_DRG.DB39_group(record):
      return 'DB39'

    return 'DB3'
  else:
    return ''

