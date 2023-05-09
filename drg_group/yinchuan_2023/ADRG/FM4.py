from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I27.202","I70.002","I71.000x002","I71.000x003","I71.000x008","I71.000x011","I71.000x021","I71.000x025","I71.000x029","I71.004","I71.005","I71.007","I71.202","I71.204","I71.300","I71.400x002","I71.401","I71.402","I71.801","I71.902","I72.300x022","I72.303","I74.302","I77.800x021","I77.800x022","I77.802","I77.803","I80.207","I80.303","I82.203","I87.202","Q25.100","R57.901","S35.001","T82.900x002"]
  adrg_zd1=[]
  adrg_ss=["39.4902","39.5000x015","39.7100x004","39.7101","39.7102","39.7103","39.7300x003","39.7301","39.7302","39.7303","39.7800x001","39.7800x002","39.7800x006","39.9002"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FM4入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FM41_group(record):
      return 'FM41'

    if MDCF_DRG.FM43_group(record):
      return 'FM43'

    if MDCF_DRG.FM45_group(record):
      return 'FM45'

    return 'FM4'
  else:
    return ''

