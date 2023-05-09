from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I05.000","I05.000x001","I05.100","I05.200","I05.200x001","I05.900x001","I06.000","I06.100","I06.200","I07.100","I07.100x001","I07.200","I08.000","I08.000x001","I08.001","I08.002","I08.003","I08.004","I08.005","I08.006","I08.007","I08.008","I08.100","I08.100x001","I08.101","I08.102","I08.103","I08.200x001","I08.201","I08.300","I08.300x001","I08.301","I08.302","I08.303","I08.304","I08.306","I08.901","I33.009","I34.000","I34.000x001","I34.001","I34.100","I34.102","I34.202","I34.802","I35.000","I35.100","I35.200","I35.200x001","I35.804","I35.806","I35.808","I35.900","I36.100","I36.800x002","I36.800x003","I37.000","I37.100","I38.x00x002","I38.x01"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合FT3入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FT31_group(record):
      return 'FT31'

    if MDCF_DRG.FT35_group(record):
      return 'FT35'

    return 'FT3'
  else:
    return ''

