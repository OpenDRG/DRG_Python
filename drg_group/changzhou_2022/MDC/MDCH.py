from drg_group.changzhou_2022.Base import message,intersect,SS_VALID
from drg_group.changzhou_2022.ADRG import HB1,HC1,HC2,HC3,HC4,HJ1,HK1,HL1,HL2,HR1,HS1,HS2,HS3,HT1,HU1,HZ1,HZ2,HZ3

def group(record):
  mdc_zd=["A01.000x011","A01.000x014","A01.001+K77.0*","A06.400+K77.0*","A18.301","A18.814+K77.0*","A18.815+K87.0*","A18.816+K87.0*","A18.817+K87.1*","A42.803","A50.000x002+K77.0*","A51.400x008+K77.0*","A52.700x007+K77.0*","A52.705+K77.0*","B00.802+K77.0*","B00.803+K77.0*","B01.801","B05.800x003+K77.0*","B15.000","B15.001","B15.002","B15.003","B15.900","B15.901","B15.902","B15.903","B15.905","B16.000","B16.000x001","B16.001","B16.100","B16.100x002","B16.100x003","B16.100x004","B16.101","B16.200","B16.201","B16.202","B16.203","B16.204","B16.901","B16.902","B16.903","B16.904","B16.905","B17.000","B17.100","B17.100x003","B17.100x006","B17.101","B17.102","B17.103","B17.200","B17.200x004","B17.200x005","B17.202","B17.203","B17.204","B17.205","B17.800x001","B17.800x002","B17.800x003","B17.801","B17.803","B17.900","B17.900x002","B17.900x002","B17.900x004","B17.900x005","B17.900x006","B17.902","B17.903","B17.904","B18.000","B18.001","B18.002","B18.003","B18.004","B18.100","B18.100","B18.100","B18.100x007","B18.104","B18.105","B18.106","B18.107","B18.200","B18.200","B18.200","B18.200x009","B18.201","B18.202","B18.203","B18.204","B18.800x001","B18.800x002","B18.800x003","B18.800x004","B18.800x005","B18.801","B18.802","B18.803","B18.804","B18.805","B18.900","B18.900","B18.900","B18.900x006","B18.901","B18.902","B18.903","B19.000","B19.001","B19.002","B19.900","B19.901","B25.100+K77.0*","B25.101+K77.0*","B25.200+K87.1*","B26.300+K87.1*","B26.802+K77.0*","B44.803","B45.800x001","B49.x00x021","B54.x00x003+K77.0*","B58.100+K77.0*","B65.202+K77.0*","B65.900x004+K77.0*","B65.900x010+K77.0*","B65.903+K77.0*","B65.904+I98.2*","B65.906+I98.3*","B65.906+I98.3*","B66.100x001+K77.0*","B66.300","B66.301","B66.300x001","B66.800x007","B66.902","B67.000x001+K77.0*","B67.500x001+K77.0*","B67.800x001+K77.0*","B69.802","B77.800x002","B77.800x004","B77.800x005","B77.803","B83.800x003","C22.000","C22.001","C22.100","C22.101","C22.200","C22.300","C22.301","C22.400","C22.700","C22.900","C23.x00","C24.000","C24.000x007","C24.001","C24.002","C24.003","C24.004","C24.100","C24.101","C24.800","C24.800x001","C24.900","C25.000","C25.100","C25.200","C25.300","C25.400","C25.401","C25.701","C25.800x001","C25.801","C25.802","C25.803","C25.900","C45.704","C77.203","C77.204","C78.700","C78.800x009","C78.806","C78.807","C78.808","D01.500x001","D01.501","D01.502","D01.503","D01.700","D01.701","D13.400","D13.401","D13.500","D13.500x001","D13.500x003","D13.501","D13.600","D13.700x001","D13.701","D17.700x015","D18.000x031","D18.013","D37.600x001","D37.600x002","D37.600x003","D37.600x004","D37.601","D37.602","D37.603","D37.604","D37.605","D37.700x003","D37.705","D37.706","E80.400","E80.500","E80.501","E80.600x005","E80.600x006","E80.600x007","E80.600x008","E80.601","E80.602","E80.603","E83.102","E85.415+K77.8*","I72.800x072","I72.809","I74.800x016","I74.803","I74.804","I77.000x017","I77.100x011","I81.x00","I81.x00x003","I82.000x001","I82.001","I86.808","I86.809","I87.108","I87.109","I87.121","I87.803","K65.007","K70.000","K70.001","K70.100","K70.201","K70.300","K70.301+I98.2*","K70.302+I98.3*","K70.303+I98.2*","K70.304+I98.2*","K70.305+I98.3*","K70.306+I98.3*","K70.400x002","K70.401","K70.402","K70.403","K70.900","K70.901","K71.000x002","K71.001","K71.002","K71.100","K71.100x003","K71.100x005","K71.100x006","K71.100x007","K71.100x008","K71.101","K71.102","K71.103","K71.104","K71.200x001","K71.300x001","K71.400x001","K71.500x001","K71.500x002","K71.600","K71.600x002","K71.601","K71.700","K71.701","K71.702","K71.800","K71.900","K71.900x003","K71.901","K71.902+I98.2*","K71.903+I98.3*","K72.000x004","K72.000x005","K72.000x013","K72.001","K72.002","K72.003","K72.004","K72.005","K72.100","K72.900x001","K72.900x003+G94.3*","K72.902","K72.904","K73.000x001","K73.100","K73.200x002","K73.800x001","K73.801","K73.900","K73.901","K74.000","K74.100","K74.200","K74.300","K74.300x005+I98.2*","K74.300x006+I98.3*","K74.300x007+I98.2*","K74.300x008+I98.3*","K74.301+I98.2*","K74.302+I98.3*","K74.400","K74.500","K74.600","K74.600x002","K74.600x002","K74.600x003","K74.600x003","K74.600x003","K74.600x003","K74.600x003","K74.600x010","K74.600x021","K74.600x025","K74.600x027","K74.600x029","K74.600x030","K74.600x031","K74.600x034","K74.600x036","K74.600x041","K74.600x042","K74.601","K74.601","K74.601","K74.602","K74.603","K74.604","K74.605","K74.606","K74.607","K74.608","K74.610","K74.611","K74.612","K74.613","K74.614","K74.615+I98.3*","K74.616+I98.2*","K74.617+I98.3*","K74.618+I98.3*","K74.619+I98.2*","K74.620+I98.2*","K75.000","K75.000x002","K75.000x003","K75.001","K75.002","K75.003","K75.100","K75.200","K75.300","K75.300x001","K75.400","K75.401","K75.800x001","K75.800x006","K75.801","K75.803","K75.804","K75.805","K75.806","K75.810","K75.901","K76.000","K76.001","K76.101","K76.102","K76.200","K76.300","K76.400","K76.401","K76.500","K76.500x001","K76.500x002","K76.600x002","K76.600x006","K76.600x007","K76.601","K76.602","K76.603","K76.700","K76.700x001","K76.700x003","K76.800x003","K76.800x006","K76.800x007","K76.800x009","K76.800x015","K76.800x021","K76.800x022","K76.800x023","K76.800x026","K76.800x027","K76.801","K76.803","K76.804","K76.805","K76.806","K76.807","K76.808","K76.809","K76.810","K76.811","K76.813","K76.814","K76.815","K76.816","K76.817","K76.818","K76.819","K76.900x002","K76.901","K80.000x002","K80.000x004","K80.001","K80.002","K80.100x001","K80.101","K80.200x001","K80.200x003","K80.201","K80.202","K80.203","K80.300x002","K80.300x005","K80.301","K80.302","K80.303","K80.304","K80.305","K80.306","K80.400","K80.400x004","K80.401","K80.402","K80.403","K80.404","K80.405","K80.406","K80.500x001","K80.500x002","K80.501","K80.502","K80.503","K80.504","K80.505","K80.506","K80.507","K80.800x001","K80.801","K81.000","K81.000x008","K81.001","K81.002","K81.003","K81.004","K81.005","K81.006","K81.007","K81.008","K81.100","K81.101","K81.801","K81.900","K81.900x001","K82.000","K82.000x003","K82.001","K82.100x002","K82.101","K82.200","K82.200x002","K82.300","K82.301","K82.302","K82.303","K82.304","K82.305","K82.306","K82.400","K82.800x002","K82.800x004","K82.800x009","K82.801","K82.802","K82.803","K82.804","K82.805","K82.806","K82.807","K82.808","K82.900x001","K82.900x002","K83.000","K83.000x007","K83.000x012","K83.001","K83.004","K83.005","K83.006","K83.007","K83.008","K83.009","K83.010","K83.011","K83.012","K83.013","K83.014","K83.015","K83.016","K83.017","K83.018","K83.019","K83.100","K83.100x001","K83.100x008","K83.101","K83.102","K83.103","K83.104","K83.105","K83.106","K83.107","K83.108","K83.109","K83.200x001","K83.300","K83.301","K83.302","K83.303","K83.304","K83.305","K83.306","K83.307","K83.400x001","K83.401","K83.501","K83.502","K83.800x009","K83.800x012","K83.800x022","K83.800x023","K83.802","K83.803","K83.804","K83.805","K83.807","K83.808","K83.809","K83.810","K83.811","K83.813","K83.814","K83.815","K83.816","K83.817","K83.818","K83.819","K83.820","K83.901","K83.902","K85.000","K85.001","K85.002","K85.100","K85.101","K85.102","K85.200","K85.201","K85.202","K85.300","K85.301","K85.302","K85.800x001","K85.800x002","K85.800x003","K85.801","K85.802","K85.803","K85.807","K85.808","K85.809","K85.813","K85.814","K85.815","K85.816","K85.817","K85.818","K85.821","K85.822","K85.900","K85.900x002","K85.900x003","K85.901","K85.902","K86.000","K86.100x001","K86.100x002","K86.100x004","K86.101","K86.102","K86.103","K86.104","K86.105","K86.106","K86.107","K86.200","K86.300","K86.800x001","K86.800x002","K86.800x013","K86.800x015","K86.801","K86.802","K86.803","K86.804","K86.805","K86.806","K86.807","K86.808","K86.809","K86.810","K86.811","K86.812","K86.813","K86.814","K86.815","K86.816","K86.817","K86.818","K86.901","K91.500","K91.800x301","K91.800x304","K91.800x401","K91.800x402","K91.800x403","K91.800x407","K91.800x411","K91.806","K91.807","K91.822","K91.823","K91.825","K91.826","K91.827","K91.840","K91.841","K92.800x006","K92.800x009","K92.800x010","K92.800x012","M32.108+K77.8*","M35.003+K77.8*","Q27.304","Q27.800x004","Q27.804","Q27.805","Q44.001","Q44.002","Q44.003","Q44.004","Q44.100x002","Q44.100x003","Q44.101","Q44.102","Q44.200","Q44.200x003","Q44.201","Q44.300","Q44.301","Q44.400","Q44.500x005","Q44.500x006","Q44.500x007","Q44.501","Q44.502","Q44.503","Q44.504","Q44.505","Q44.600","Q44.601","Q44.700x002","Q44.700x003","Q44.700x004","Q44.701","Q44.702","Q44.703","Q44.704","Q44.705","Q45.001","Q45.002","Q45.003","Q45.100","Q45.200","Q45.300x901","Q45.300x902","Q45.300x904","Q45.301","Q45.802","Q85.900x019","Q85.900x044","Q85.911","Q85.912","R16.000x001","R16.200x001","R17.900x001","R17.901","R93.200x001","R93.200x002","R93.201","R93.203","R93.204","R93.205","R93.302","R94.500","S36.100x001","S36.100x011","S36.100x013","S36.100x021","S36.100x031","S36.100x041","S36.100x051","S36.100x081","S36.101","S36.102","S36.103","S36.110","S36.111","S36.112","S36.113","S36.200","S36.200x001","S36.200x011","S36.200x021","S36.200x031","S36.200x091","S36.200x092","S36.201","S36.202","S36.210","T81.800x006","T82.813","T85.800x802","T86.400x001","T86.400x003","T86.400x004","T86.400x005","T86.400x006","T86.400x007","T86.400x009","T86.400x010","T86.400x011","T86.400x012","T86.400x013","T86.400x014","T86.400x015","T86.400x016","T86.400x017","T86.400x018","T86.401","T86.800x021","T86.804","Z52.600x001"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCH入组条件，匹配规则：主诊断匹配')

  result=HB1.group(record)
  if result:
    return result
  result=HC1.group(record)
  if result:
    return result
  result=HC2.group(record)
  if result:
    return result
  result=HC3.group(record)
  if result:
    return result
  result=HC4.group(record)
  if result:
    return result
  result=HJ1.group(record)
  if result:
    return result
  result=HK1.group(record)
  if result:
    return result
  result=HL1.group(record)
  if result:
    return result
  result=HL2.group(record)
  if result:
    return result

  if record.ssList and record.ssList[0] in SS_VALID:
    message('符合HQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'HQY'

  result=HR1.group(record)
  if result:
    return result

  result=HS1.group(record)
  if result:
    return result

  result=HS2.group(record)
  if result:
    return result

  result=HS3.group(record)
  if result:
    return result

  result=HT1.group(record)
  if result:
    return result

  result=HU1.group(record)
  if result:
    return result

  result=HZ1.group(record)
  if result:
    return result

  result=HZ2.group(record)
  if result:
    return result

  result=HZ3.group(record)
  if result:
    return result

  message('不符合MDCH的ADRG入组条件')

