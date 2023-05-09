from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=["H20.802","H21.000","H31.401","H33.200x002","H33.200x004","H33.304","H33.400","H33.500x008","H33.501","H33.502","H33.504","H33.506","H35.600","H35.601","H35.602","H43.100","H59.900","S00.100x001","S00.202","S01.000x002","S01.101","S01.102","S02.801","S05.000x002","S05.001","S05.100x004","S05.102","S05.201","S05.300x004","S05.301","S05.302","S05.306","S05.500x002","S05.500x003","S05.601","S05.604","S05.802","S05.806","S05.808","S05.809","T15.000","T26.100x001","T26.602","T26.902","T85.202","T85.300x005","T85.300x008","T85.301"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合CT1入组条件，匹配规则：主诊断匹配')
    
    if MDCC_DRG.CT19_group(record):
      return 'CT19'

    return 'CT1'
  else:
    return ''

