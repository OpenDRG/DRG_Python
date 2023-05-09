from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I70.204","I70.214","I73.100","I74.302","I74.500x002","I74.504","I74.902","I77.800x022","I80.206","I80.207","I80.303","I82.203","I83.100x001","I83.900x004","I83.903","I87.115","I87.116","I87.201","I87.202","Q28.800x007","T82.811"]
  adrg_zd1=[]
  adrg_ss=["00.5502","38.0602","38.0701","38.0800x002","38.0801","38.0802","38.0900x001","38.0901","38.1800x001","38.1800x002","38.4802","38.5901","38.5902","38.6000x012","38.7x04","38.8604","38.9800x801","38.9900x901","39.2907","39.3100x004","39.4900x005","39.5000x011","39.5000x026","39.5000x029","39.5000x031","39.5005","39.5007","39.5900x004","39.5900x019","39.5900x021","39.7900x043","39.7900x809","39.7902","39.9000x011","39.9000x016","39.9004","39.9009","39.9010","88.4202","88.4204","88.4403","88.4705","88.4800x005","88.4801","88.5102","88.6600x002","88.6601","88.6703","99.1001","99.1002","99.1003"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FF2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FF21_group(record):
      return 'FF21'

    if MDCF_DRG.FF23_group(record):
      return 'FF23'

    if MDCF_DRG.FF25_group(record):
      return 'FF25'

    return 'FF2'
  else:
    return ''

