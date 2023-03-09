from drg_group.lanzhou_2022.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2022.DRG import MDCT_DRG

def group(record):
  adrg_zd=["F40.000","F40.100","F40.200x001","F40.200x002","F40.200x003","F40.200x004","F40.800","F40.900","F40.901","F41.000","F41.001","F41.100","F41.101","F41.102","F41.200","F41.200x002","F41.201","F41.300x001","F41.800","F41.900","F42.000","F42.001","F42.003","F42.100","F42.101","F42.200","F42.800","F42.800x001","F42.900","F42.901"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合TV1入组条件，匹配规则：主诊断匹配')
    
    if MDCT_DRG.TV19_group(record):
      return 'TV19'

    return 'TV1'
  else:
    return ''

