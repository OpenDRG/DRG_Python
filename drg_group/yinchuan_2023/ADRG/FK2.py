from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I21.401","I44.102","I44.200","I44.201","I47.200","Z45.002","Z45.005","Z45.006"]
  adrg_zd1=[]
  adrg_ss=["00.5000x001","00.5000x004","00.5001","00.5002","00.5302"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FK2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FK29_group(record):
      return 'FK29'

    return 'FK2'
  else:
    return ''

