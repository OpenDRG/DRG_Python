from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=["B49.x04+H19.2*","H04.300x004","H04.302","H04.303","H04.401","H04.503","H04.509","H04.602","H05.801","H11.000","H11.807","H20.000x004","H20.101","H20.900x004","H25.100","H31.800x004","H34.801","H34.803","H35.307","H40.200","S05.500x001"]
  adrg_zd1=[]
  adrg_ss=["08.5200","09.8100","09.9900x003","10.9100","11.3100x001","11.9900x004","15.7x00","16.1x00x001","16.9100"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合CJ1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCC_DRG.CJ19_group(record):
      return 'CJ19'

    return 'CJ1'
  else:
    return ''

