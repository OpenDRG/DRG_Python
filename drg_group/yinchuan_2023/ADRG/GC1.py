from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCG_DRG

def group(record):
  adrg_zd=["C15.400","C15.500","C16.000","C16.100","C16.200","C16.900","C17.000","C78.401","C78.801","D13.000","D13.100","D13.200","D13.301","D17.500x003","D17.500x008","D37.100x002","D37.101","D37.202","D37.203","I86.401","I86.800x014","K22.000x002","K22.205","K22.601","K25.100x001","K25.400x001","K25.500x001","K25.501","K25.900x001","K25.903","K26.000","K26.100","K26.200x002","K26.400x003","K26.401","K26.500x001","K26.501","K27.500","K27.503","K28.100","K28.900x001","K31.100x002","K31.500","K31.800x806","K31.808","K31.812","K31.814","K35.800x001","K57.003","K57.200x001","K63.101","K63.103","K63.104","K63.105","K63.107","K63.108","K65.002","K65.003","K91.800x106","K91.809","K91.819","K92.210","Q39.600","Q40.204","Q41.003","Q43.301","S36.901","T18.100","T28.600"]
  adrg_zd1=[]
  adrg_ss=["42.0901","42.0902","42.3201","42.8200","42.8501","42.9100x002","42.9200x007","43.0x00x003","43.0x01","43.0x03","43.1900x003","43.1900x005","43.4900","43.8201","44.0100","44.1500","44.2200x001","44.2200x003","44.4000","44.4100x008","44.4101","44.4102","44.4200x001","44.4200x003","44.4201","44.4202","44.4400x001","44.4400x005","44.4401","44.4402","44.4403","44.4901","44.6100x003","44.6500x002","44.6901","44.6902","44.9101","44.9201","45.3101","45.6202","46.7901","46.7902","46.7904","97.5901","98.0200x001","98.0201"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCG_DRG.GC11_group(record):
      return 'GC11'

    if MDCG_DRG.GC13_group(record):
      return 'GC13'

    if MDCG_DRG.GC15_group(record):
      return 'GC15'

    return 'GC1'
  else:
    return ''

