from drg_group.xian_2020.Base import message,intersect,SS_VALID
from drg_group.xian_2020.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.5000x004","00.5000x005","00.5201","00.5202","00.5302","37.7000","37.7100","37.7200","37.7300","37.7401","37.7402","37.7501","37.7600x002","37.7701","37.7800","37.7900x003","37.7900x004","37.7901","37.7902","37.8000x002","37.8501","37.8601","37.8701","37.8901","37.8902","37.8903","39.6400"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FK2入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FK29_group(record):
      return 'FK29'

    return 'FK2'
  else:
    return ''

