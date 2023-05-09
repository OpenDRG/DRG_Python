from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I15.200x001","I15.900","I48.000","I70.101","I70.204","I70.211","I73.100","I74.200x001","I74.300x030","I74.300x232","I74.301","I74.302","I77.013","I77.100x004","I80.206","I80.207","I80.300x006","I80.303","I82.203","I83.900x004","I87.001","I87.116","I87.118","I87.202","Q27.818","R57.101","R57.200","T82.800x407","T82.811"]
  adrg_zd1=[]
  adrg_ss=["88.4500","88.4705","88.4800x005","88.4801","88.4901","88.4904","88.5102","88.6600x002","88.6601","88.6703","99.1000x007","99.1000x009","99.1001","99.1003"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FN2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FN21_group(record):
      return 'FN21'

    if MDCF_DRG.FN25_group(record):
      return 'FN25'

    return 'FN2'
  else:
    return ''

