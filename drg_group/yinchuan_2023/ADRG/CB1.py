from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=["E10.301+H36.0*","E11.300x031+H36.0*","E11.300x032+H36.0*","E11.300x034+H36.0*","E11.300x053+H36.0*","E11.301+H36.0*","E14.300x034+H36.0*","E14.300x071+H36.0*","H16.000","H20.900x004","H21.400","H21.500x004","H25.000","H25.000x003","H25.100","H25.800","H25.900","H26.200","H26.801","H26.900","H27.000","H27.100","H27.101","H27.102","H30.801","H31.400","H31.800x004","H31.802","H33.000","H33.000x005","H33.000x006","H33.000x007","H33.001","H33.102","H33.200x002","H33.200x004","H33.301","H33.304","H33.400","H33.500","H33.500x008","H33.501","H33.502","H33.504","H33.506","H34.100","H34.202","H34.800x001","H34.801","H34.802","H34.803","H35.005","H35.011","H35.100","H35.200","H35.300x010","H35.300x011","H35.303","H35.305","H35.306","H35.307","H35.501","H35.600","H35.701","H35.800x005","H35.804","H35.807","H40.200","H40.200x006","H40.202","H40.203","H40.300","H40.400","H40.500","H40.500x002","H40.500x009","H40.501","H40.505","H40.600","H40.900","H43.100","H43.200x001","H43.300","H43.800x003","H43.802","H43.803","H43.804","H43.805","H43.900","H44.000x002","H44.000x005","H44.501","H47.000x009","H47.004","H57.002","H59.800x013","Q12.000","Q13.802","S04.000x001","S05.100x004","S05.201","S05.202","S05.205","S05.300x004","S05.500x001","S05.500x002","S05.500x003","S05.601","S05.604","S05.802","S05.806","T85.200x001","T85.202","T85.300x005","T85.303","Z48.801"]
  adrg_zd1=[]
  adrg_ss=["12.1101","12.1202","12.1402","12.1403","12.1404","12.3300","12.3500","12.3504","12.3900x004","14.0200x002","14.0201","14.2102","14.2302","14.2402","14.2900x001","14.2900x002","14.2900x003","14.2900x004","14.2902","14.3101","14.3400","14.3500","14.3901","14.4900x001","14.4901","14.5101","14.5400x001","14.5500","14.5902","14.5903","14.5904","14.5905","14.6x00x001","14.6x02","14.7100x001","14.7201","14.7300x001","14.7401","14.7500x001","14.7500x004","14.7501","14.7901","14.7903","14.7904","14.7905","14.9x00x001","14.9x01","14.9x02","14.9x03","14.9x04","14.9x05","14.9x07","16.9100x002"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合CB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCC_DRG.CB19_group(record):
      return 'CB19'

    return 'CB1'
  else:
    return ''

