from drg_group.yunnan_2023.Base import message,intersect,SS_VALID
from drg_group.yunnan_2023.ADRG import MA1,MB1,MC1,MD1,MJ1,MR1,MS1,MZ1

def group(record):
  mdc_zd=["A06.800x004+N51.2*","A18.100x018+N51.8*","A18.100x020+N51.8*","A18.109+N51.0*","A18.110+N51.8*","A18.116+N51.8*","A18.117+N51.1*","A18.118+N51.1*","A18.119+N51.8*","A54.202+N51.0*","A54.203+N51.1*","A54.204+N51.1*","A56.102+N51.1*","A56.103+N51.1*","A59.000x003+N51.0*","A60.000x004+N51.8*","A60.003+N51.8*","B26.000+N51.1*","B37.402+N51.2*","C60.000","C60.100","C60.200","C60.201","C60.800","C60.900","C60.901","C61.x00","C62.000","C62.001","C62.100","C62.900","C62.901","C63.000","C63.100","C63.200","C63.201","C63.700","C63.701","C63.702","C63.800","C63.801","C63.900","C79.800x228","C79.800x231","C79.800x233","C79.815","C79.816","C79.817","C79.818","C79.819","C79.820","D07.400","D07.401","D07.402","D07.500","D07.601","D07.602","D07.603","D17.600x001","D17.700x033","D17.700x034","D18.000x815","D18.000x818","D18.000x855","D18.108","D29.000","D29.001","D29.100","D29.200","D29.300","D29.400","D29.401","D29.700x004","D29.700x005","D29.701","D29.702","D29.703","D29.900","D40.000x001","D40.001","D40.100x002","D40.101","D40.700x001","D40.700x002","D40.700x003","D40.701","D40.702","D40.703","D40.704","D40.900x001","D40.901","D48.127","E29.000","E29.000x002","E29.001","E29.002","E29.100","E29.100x002","E29.100x004","E29.101","E29.102","E29.103","E29.104","E29.105","E29.106","E29.800","E29.900","E89.501","I86.100","I86.101","I86.200","I87.120","I87.804","I89.000x022","I89.000x023","I89.000x024","I89.008","I89.800x010","N36.801","N40.x00","N40.x01","N41.000","N41.100","N41.101","N41.200","N41.300","N41.800","N41.900x001","N41.900x002","N42.000","N42.101","N42.102","N42.200","N42.300","N42.301","N42.801","N42.802","N42.901","N43.000","N43.001","N43.100","N43.101","N43.201","N43.300","N43.301","N43.302","N43.400","N44.x00","N44.x01","N44.x02","N45.000","N45.001","N45.002","N45.901","N45.902","N45.903","N45.904","N45.905","N45.906","N45.907","N45.908","N46.x00","N46.x00x007","N46.x01","N46.x02","N47.x00x001","N47.x01","N47.x02","N47.x03","N48.000","N48.000x003","N48.001","N48.100","N48.101","N48.102","N48.201","N48.202","N48.203","N48.204","N48.300","N48.301","N48.400","N48.400x005","N48.400x006","N48.400x007","N48.400x008","N48.401","N48.402","N48.403","N48.500","N48.600","N48.800x005","N48.800x009","N48.801","N48.802","N48.803","N48.804","N48.805","N48.806","N48.807","N48.808","N48.809","N48.810","N48.811","N48.812","N48.813","N48.901","N49.001","N49.002","N49.101","N49.102","N49.103","N49.104","N49.201","N49.202","N49.203","N49.204","N49.205","N49.800","N49.900","N50.000","N50.100x001","N50.101","N50.102","N50.103","N50.800","N50.800x001","N50.800x002","N50.800x012","N50.800x014","N50.800x016","N50.800x023","N50.800x024","N50.800x025","N50.800x027","N50.800x028","N50.800x038","N50.800x041","N50.800x042","N50.801","N50.802","N50.803","N50.804","N50.805","N50.806","N50.807","N50.808","N50.809","N50.810","N50.811","N50.812","N50.813","N50.814","N50.815","N50.816","N50.817","N50.818","N50.819","N50.820","N50.821","N50.822","N50.823","N50.824","N50.825","N50.826","N50.827","N50.900x005","N50.900x006","N50.900x007","N50.900x008","N50.901","N50.902","N50.903","Q53.000","Q53.000x002","Q53.000x003","Q53.100","Q53.100x001","Q53.101","Q53.102","Q53.200","Q53.200x001","Q53.201","Q53.202","Q53.900","Q53.901","Q53.902","Q54.000","Q54.001","Q54.100","Q54.200","Q54.300","Q54.400","Q54.800","Q54.900","Q54.901","Q55.001","Q55.002","Q55.003","Q55.004","Q55.100x002","Q55.101","Q55.200x901","Q55.201","Q55.202","Q55.203","Q55.300","Q55.400x006","Q55.400x008","Q55.401","Q55.402","Q55.403","Q55.404","Q55.405","Q55.501","Q55.502","Q55.600x007","Q55.600x008","Q55.600x009","Q55.601","Q55.602","Q55.603","Q55.604","Q55.605","Q55.606","Q55.800","Q55.800x001","Q55.801","Q55.802","Q55.900","Q55.901","Q56.000","Q56.001","Q56.002","Q56.100","Q56.300","Q56.400","Q85.900x032","Q85.900x047","R86.000","R86.100","R86.200","R86.300","R86.400","R86.500","R86.600","R86.700","R86.800","R86.900x003","R86.901","R86.902","R86.903","R93.802","S30.202","S30.203","S30.205","S30.206","S30.208","S31.200","S31.300x001","S31.300x002","S31.301","S31.501","S37.801","S37.802","S37.804","S37.811","S37.910","S38.000","S38.001","S38.200x003","S38.200x004","S38.200x005","S39.900x007","S39.900x009","S39.900x010","S39.904","T19.800x002","T83.401","T83.600","T83.601","Z31.000x004","Z41.200"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd and record.gender=="1"):
    return ''
  
  message('符合MDCM入组条件，匹配规则：主诊断匹配、男性')

  result=MA1.group(record)
  if result:
    return result
  result=MB1.group(record)
  if result:
    return result
  result=MC1.group(record)
  if result:
    return result
  result=MD1.group(record)
  if result:
    return result
  result=MJ1.group(record)
  if result:
    return result

  if record.ssList and record.ssList[0] in SS_VALID:
    message('符合MQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'MQY'

  result=MR1.group(record)
  if result:
    return result

  result=MS1.group(record)
  if result:
    return result

  result=MZ1.group(record)
  if result:
    return result

  message('不符合MDCM的ADRG入组条件')

