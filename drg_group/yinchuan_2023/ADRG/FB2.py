from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I05.000","I05.000x001","I05.100","I05.200","I05.200x001","I06.000","I06.100","I06.200","I07.100","I08.001","I08.003","I08.005","I08.006","I08.101","I08.102","I08.103","I08.201","I08.300x001","I08.301","I08.302","I08.303","I08.306","I09.900","I25.103","I33.000x004","I33.006","I33.009","I34.000","I34.100","I34.102","I35.000","I35.100","I35.200","I35.808","I36.800x003","I37.000","I50.900x001","I71.000x011","I71.003","I71.200x010","Q21.000","Q22.100","Q23.101","Q25.408"]
  adrg_zd1=[]
  adrg_ss=["35.0100x002","35.0200x003","35.0600x002","35.1101","35.1201","35.1301","35.1400x002","35.1401","35.2100x003","35.2101","35.2200x002","35.2201","35.2300x002","35.2301","35.2400x002","35.2401","35.2701","35.3300x002","35.9500x003","37.3300x017","37.3300x026"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FB2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FB21_group(record):
      return 'FB21'

    if MDCF_DRG.FB25_group(record):
      return 'FB25'

    return 'FB2'
  else:
    return ''

