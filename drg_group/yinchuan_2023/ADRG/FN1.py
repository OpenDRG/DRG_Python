from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I20.000","I21.001","I21.003","I21.004","I21.200x018","I21.208","I21.300x004","I21.401","I25.600x001","I70.101","I70.200x021","I70.203","I70.204","I70.214","I71.000x021","I71.005","I71.204","I72.300x006","I72.300x021","I72.300x033","I72.301","I72.303","I72.304","I72.400x123","I72.404","I72.811","I73.100","I74.201","I74.300x030","I74.301","I74.302","I74.307","I74.500x002","I74.801","I77.000x011","I77.013","I77.102","I77.202","I80.104","I80.206","I80.207","I80.300x006","I80.303","I82.203","I83.900x004","I83.902","I87.100x009","I87.111","I87.115","I87.116","I87.118","I87.202","Q25.000","Q25.704","Q26.600","Q28.800x007","T82.800x004","T82.801"]
  adrg_zd1=[]
  adrg_ss=["00.5500x014","00.5501","00.5502","17.5600x001","38.7x04","39.5000x011","39.5000x019","39.5000x025","39.5000x026","39.5000x031","39.5001","39.5002","39.5004","39.5005","39.5007","39.5008","39.5009","39.5011","39.5015","39.5016","39.7900x007","39.7900x019","39.7900x041","39.7900x042","39.7900x043","39.7900x047","39.7900x068","39.7900x809","39.7902","39.7903","39.7904","39.7905","39.7906","39.9000x010","39.9000x011","39.9000x016","39.9000x019","39.9000x026","39.9000x028","39.9000x034","39.9000x035","39.9004","39.9007","39.9008","39.9009","39.9010","39.9016"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FN1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FN11_group(record):
      return 'FN11'

    if MDCF_DRG.FN13_group(record):
      return 'FN13'

    if MDCF_DRG.FN15_group(record):
      return 'FN15'

    return 'FN1'
  else:
    return ''

