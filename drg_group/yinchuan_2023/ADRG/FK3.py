from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I20.000","I20.801","I21.103","I21.300x004","I25.103","I25.500","I42.100","I42.900","I44.000","I44.100","I44.101","I44.102","I44.200","I44.201","I44.303","I44.602","I45.102","I45.400x001","I45.502","I47.200","I47.203","I48.000","I48.100","I48.100x002","I48.900x004","I49.001","I49.500","I49.900","R00.100x001","R55.x00x002","R94.300x011","Z45.001","Z45.002","Z45.003","Z45.005","Z45.006"]
  adrg_zd1=[]
  adrg_ss=["37.8000x001","37.8000x002","37.8001","37.8101","37.8301","37.8501","37.8701","37.8902","37.8903","37.9401"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FK3入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FK39_group(record):
      return 'FK39'

    return 'FK3'
  else:
    return ''

