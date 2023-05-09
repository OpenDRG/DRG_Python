from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCG_DRG

def group(record):
  adrg_zd=["C15.000","C15.100","C15.100x002","C15.100x003","C15.100x004","C15.200","C15.300","C15.400","C15.500","C15.800x002","C15.801","C15.802","C15.900","C16.000","C16.000x003","C16.001","C16.002","C16.100","C16.200","C16.301","C16.402","C16.500","C16.600","C16.800","C16.801","C16.802","C16.803","C16.804","C16.900","C16.900x003","C16.902","C16.903","C17.000","C17.900","C18.000","C18.001","C18.100","C18.200","C18.300","C18.400","C18.500","C18.600","C18.700","C18.800x002","C18.801","C18.802","C18.900","C19.x00","C19.x01","C20.x00","C21.100","C21.802","C26.800","C26.900","C26.901","C45.703","C48.000","C48.100","C48.104","C48.200","C48.201","C48.800","C76.200","C76.304","C77.106","C78.401","C78.500x004","C78.500x008","C78.501","C78.504","C78.600x004","C78.601","C78.602","C78.802","C78.809","C79.800x834","C79.809","D00.100","D00.200","D00.200x002","D01.000","D01.200"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合GR1入组条件，匹配规则：主诊断匹配')
    
    if MDCG_DRG.GR11_group(record):
      return 'GR11'

    if MDCG_DRG.GR13_group(record):
      return 'GR13'

    if MDCG_DRG.GR15_group(record):
      return 'GR15'

    return 'GR1'
  else:
    return ''

