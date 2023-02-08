from drg_group.taizhou_2022.Base import message,intersect,SS_VALID
from drg_group.taizhou_2022.ADRG import NA1,NA2,NB1,NC1,ND1,NE1,NF1,NG1,NJ1,NR1,NS1,NZ1

def group(record):
  mdc_zd=["E28.200","N80.603","N83.207","N88.200x001","N76.500","N83.204","N90.400","N85.810","Q27.816","Q85.900x016","C58.x00","N89.000","Q85.900x045","N86.x00x004","N83.808","Q52.104","N92.000x001","N73.201","T28.300x001","E28.900","N89.502","A18.111+N74.1*","N89.804","N95.900x001","Q52.703","N81.202","N86.x01","N85.814","N80.802","N76.000x004","N87.002","R93.803","C54.100","C52.x00","D25.900","N92.200","C79.800x222","Q56.400","N90.100","B37.300+N77.1*","A59.002+N77.1*","D39.100x003","N80.200","N82.901","S38.200x001","Q51.802","C57.700","N92.400","N88.802","Q52.404","D07.301","Q51.203","N91.400","N92.300","N83.600","N89.300","N83.000","D06.000","N88.808","C55.x00","D18.000x856","N85.300x001","D28.203","N70.900x007","C53.801","N90.800x024","N73.800x002","A18.100x030+N77.0*","D39.201","Q50.401","C54.300","Q51.501","N90.401","N80.100x001","N94.500","Q50.600","Q52.406","N80.601","N90.402","N92.400x001","D39.900x001","C79.600","S37.610","N90.700","N82.502","C79.800x218","N97.902","N85.600x001","Q50.301","N85.401","N83.201","N85.901","N81.301","N80.001","Z01.400x001","Q50.502","N85.402","S37.510","Q52.500x001","D25.100x002","N73.101","R87.400","C77.500x003","N70.901","E28.303","N98.300","N90.805","C54.001","N96.x00x003","D26.700","N90.500","N83.206","N83.700","S30.207","Q51.804","D26.000","Q50.300x101","A54.005","N76.801","N85.000x002","N83.800x015","N97.101","S30.200x008","Z52.800x001","L29.200","N81.800x004","N71.902","N90.301","N92.500","N90.800x010","N92.100x001","A54.201+N74.3*","N85.200","N81.803","Q51.805","N80.401","T83.400x001","C79.800x220","C79.800x202","E89.401","N70.902","N82.900x003","N73.603","B37.302+N77.1*","N82.303","N83.800x012","N72.x00x006","A18.113+N74.1*","D39.202","D39.700x002","N86.x02","Q51.100x001","A56.004","S37.500","C46.700x001","N75.801","N89.901","D26.100x002","N85.403","D28.700x001","N90.800x012","E30.900","N83.601","D39.100x001","Q50.504","C57.803","N92.401","Q50.601","N85.805","N82.000","N90.800x025","N85.808","N95.000","E89.400x001","N85.000","Q52.901","N85.003","N85.800x003","N95.100","N92.400x004","A54.200x004+N74.3*","N82.101","N84.900","N97.800x004","C51.800","N82.902","N85.500","N90.701","N80.303","Q52.601","D28.200x003","N76.100x002","N87.001","N94.804","N82.102","N89.601","Q51.300","D25.200x002","N84.000","D28.206","N73.605","S31.400x002","D25.901","N88.800x010","N95.800","N83.800x021","R87.000","N85.807","S39.902","N83.801","N80.803","N90.101","D39.710","S38.200x006","N94.808","N81.801","N90.802","Q51.000","N91.300","C57.000x002","R87.300","C79.821","Z31.201","N70.000","N83.205","D18.000x824","N99.300","N82.801","N76.401","N94.807","N81.602","C57.400","Q52.403","N76.000","C57.702","N70.904","D28.201","N73.002","N97.000x001","N82.401","N80.808","N85.806","N95.200","A54.102","D25.100x001","N87.000","Q51.800x012","N76.601","N75.900","D39.703","N80.800x010","N89.600x002","N97.901","D39.706","N85.300","N83.500x004","C79.800x211","Q50.000","N76.100x001","N76.600","Q51.201","E28.301","N95.201","Z31.000x001","D39.707","N83.803","D39.903","Q56.000","S37.600","D39.203","N80.602","D28.900","Q51.502","N99.800x010","C79.823","N94.806","N81.500x002","D07.100","N71.101","R87.200","N89.800x009","Q51.900","A54.004","N89.801","C79.800x219","Q52.702","N93.000x001","Q50.100","Q52.000","N93.801","I77.009","N76.301","N81.500","D28.202","D07.302","E28.000","N85.809","N85.811","N70.002","N88.807","S31.402","C79.800x209","S31.400x003","N90.901","T19.202","N83.804","N97.300","C57.701","I89.000x019","N98.200","N82.103","N75.000","A56.100x004+N74.4*","N88.804","N90.501","Q50.000x011","Q52.401","R87.800","Z31.300x002","C57.802","N73.003","D07.100x002","N91.200","N99.800x005","N90.808","M35.202+N77.8*","N71.001","N97.100x003","N98.100","N90.807","Q51.806","N85.801","D39.704","N81.102","Q50.602","C54.900","C54.800","A60.000x003+N77.1*","D39.204","N83.300x001","Q51.400","A56.104+N74.4*","A56.002","N97.200x002","N73.102","N73.601","Q51.100","D25.000","N73.902","N85.404","Q50.303","D39.708","T28.800x001","N89.101","N73.300","Z01.800x003","N80.200x001","N90.601","N90.809","N99.201","Q52.700x005","D39.709","N85.804","C79.814","N76.000x001","N76.001","N70.905","Q51.202","N85.400","N84.301","D25.200","D39.901","N99.801","N94.600","E89.400x002","C79.800x205","Q52.300","D07.200x002","N73.600","N90.806","N85.002","N73.903","N81.200","N71.901","N70.101","N83.504","N85.816","N89.200","B37.300x002+N77.1*","N92.601","R87.600","Q27.814","N80.800x007","N90.300","C79.800x213","N83.100x002","N83.800x016","N80.804","Q52.402","A18.114+N74.1*","N81.203","N73.203","N83.503","C79.812","N83.812","N92.400x003","R93.800x006","T83.303","N89.600","C79.800x223","N73.202","D06.900","N72.x02","C53.900","S37.400","N76.000x006","N89.802","Q51.600","N99.807","N80.800x011","N81.300","E28.200x003","C51.000","C57.200","N90.801","N84.302","S37.810","N90.902","S37.410","N83.809","Q51.800x011","C54.000","A18.100x032","C57.301","D28.200x002","N89.805","C57.801","D28.000","E28.300x001","N88.102","A56.100x003+N74.4*","R93.800x007","N80.501","D26.701","D27.x00","N76.200","D39.000x002","N90.404","N97.801","N73.103","N89.600x001","N81.400","C51.900","N92.101","D06.700","C79.833","N94.803","N84.800x002","Q50.600x903","Q52.200","N32.004","N90.811","N85.812","Q52.700x004","N80.300","N90.804","N88.806","N89.807","A18.100x026+N74.1*","N85.001","Q52.700x003","N83.100","N83.300x002","C58.x00x002","N80.000","N83.100x003","N71.900x001","N83.502","N73.606","N84.100","N94.100","N83.800x013","N88.100","N88.805","N73.104","N90.000","N82.501","N98.000","Q51.801","N94.800x009","S37.710","D39.003","I89.800x033","N89.808","N90.800x009","N81.000","N80.900","N83.802","A18.112+N74.0*","N84.300","N83.401","N80.301","N80.500","N80.807","N89.811","C45.100","C53.800","N89.803","N81.500x003","E28.302","N81.800x005","T83.301","Z31.200x003","N97.400x002","N95.101","N80.600","D39.002","D26.100","N88.000","N87.100","N91.100","N99.800x007","S37.600x002","N81.101","D39.702","N94.000","N72.x03","N89.100","N85.815","N90.800x011","N85.813","Q50.302","D25.000x002","D28.100","N83.800x017","N80.806","N76.400","Q56.200","C57.300","Q51.803","N73.604","Q52.701","A18.115+N74.1*","N83.000x002","N88.201","D17.300x003","T83.302","N76.300x001","C53.000","Q52.400x006","C57.800x005","E28.300x002","C51.001","N75.100","N89.810","Q50.603","Q52.800x004","S30.200x007","D39.001","C56.x00x003","N88.803","N96.x00x002","D20.103","C51.100","N73.001","D18.000x854","N83.102","Q50.400","N85.600","N94.900","N90.810","N93.900","Q51.000x001","C57.900","N90.200","N90.302","N70.100","A18.100x024+N74.1*","N84.001","Q50.503","A18.102","N81.100","N82.200","N72.x00x003","A18.100x019+N77.1*","Q50.501","R87.100","D18.000x853","N73.801","B26.800x009+N74.8*","C57.000","N87.200x001","Q85.900x047","S31.401","D39.701","N89.700","C79.800x228","D39.200x002","N70.001","C79.800x216","N81.601","N85.101","N89.503","N94.200","Q52.400x007","C56.x00","N87.900","N95.300x001","Q50.600x904","N73.600x006","N72.x01","N82.301","C53.100","N83.805","D27.x01","N89.809","N91.200x002","N83.500x007","N73.501","N70.103","N83.811","N71.102","Q50.200","Q51.901","N70.900","S38.200x002","N87.901","I86.300","N91.500","Q52.405","S30.200x010","C54.200","T19.300x001","D39.004","N92.600","A54.003","T83.305","N82.900","D07.200","N81.802","N90.001","N97.400x001","N73.400","N85.803","Q52.407","N94.400","C79.824","N91.000","C57.300x001","D39.005","N70.102","T83.400","N94.805","D07.000","N76.201","C48.100x006","N88.801","N88.400","N83.901","N76.000x003","D39.700x001","C58.x00x003","N97.100x001","I89.000x018","D39.705","N70.903","N90.803","N70.900x003","N76.802","N81.600","D18.000x817","Q27.813","N99.800x003","N90.600","Q51.001","C57.100","N82.300","N83.806","N84.200","D25.900x001","N80.302","N83.810","Z31.100","C57.800x004","D39.000x001","N89.400","C79.800x215","N85.700","C79.822","A56.003","C57.101","N85.802","N81.201","N83.807","D06.100","N97.200x001","C79.800x206","R87.700","N98.800","N82.500","R87.500","N96.x00","C79.800x214","S37.601","D07.303","N75.802","N83.501","E28.300x005","N93.901","C79.813","N73.500","A51.400x009+N74.2*","N82.100x001","N71.002","N80.100","N85.000x004","N80.801","N90.403","N87.101","D48.127","T28.800x002","T28.800x003","E28.800x002","N83.902","Q56.300","D28.205","Q50.000x021","N76.101","A56.101+N74.4*","N83.101","N85.100","S37.602","T83.304","N70.906","N73.602","D28.204","T19.201","D17.700x024","T28.300x002","Q51.800x007","N88.300","Q52.101","N88.101","N92.000x002","I86.200","C76.307","N88.900","N83.903","D07.304","Z31.300x001","N89.501","N97.900","Q51.808","N94.802","Q52.103","D28.000x002","N70.104","N99.200","N89.001","Q52.408","N83.203","C51.200","D39.101","Z31.200","N83.001","N81.900","N94.300","D26.900","N80.805","E28.300x008","B37.301+N77.1*","E28.100","D39.200x001","N80.809","D06.900x002","N98.900","D39.902","S39.901","S31.400x001","I89.800x032","N89.806","T28.300x003","N83.202","D26.702"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd and record.gender==2):
    return ''
  
  message('符合MDCN入组条件，匹配规则：主诊断匹配、女性')

  result=NA1.group(record)
  if result:
    return result
  result=NA2.group(record)
  if result:
    return result
  result=NB1.group(record)
  if result:
    return result
  result=NC1.group(record)
  if result:
    return result
  result=ND1.group(record)
  if result:
    return result
  result=NE1.group(record)
  if result:
    return result
  result=NF1.group(record)
  if result:
    return result
  result=NG1.group(record)
  if result:
    return result
  result=NJ1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合NQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'NQY'

  result=NR1.group(record)
  if result:
    return result

  result=NS1.group(record)
  if result:
    return result

  result=NZ1.group(record)
  if result:
    return result

  message('不符合MDCN的ADRG入组条件')
