from drg_group.linfen_2022.Base import message,intersect,SS_VALID
from drg_group.linfen_2022.ADRG import EB1,EB2,EC1,EC2,ED1,EJ1,ER1,ER2,ER3,ES1,ES2,ES3,ET1,ET2,EU1,EV1,EW1,EX1,EX2,EZ1

def group(record):
  mdc_zd=["A01.000x005+J17.0*","A02.201+J17.0*","A06.500+J99.8*","A06.500x002+J99.8*","A06.501+J99.8*","A06.502+J17.3*","A15.000x001","A15.000x001","A15.000x001","A15.000x002","A15.000x003","A15.000x010","A15.000x012","A15.000x014","A15.000x016","A15.000x018","A15.000x020","A15.000x022","A15.000x024","A15.000x026","A15.000x028","A15.001","A15.002","A15.003","A15.004","A15.005","A15.006","A15.007","A15.100x001","A15.100x001","A15.100x001","A15.100x002","A15.100x003","A15.100x004","A15.100x005","A15.100x006","A15.100x007","A15.100x008","A15.100x009","A15.100x010","A15.100x011","A15.101","A15.102","A15.103","A15.104","A15.105","A15.106","A15.107","A15.200x001","A15.200x001","A15.200x001","A15.200x002","A15.201","A15.202","A15.203","A15.204","A15.205","A15.206","A15.207","A15.300x001","A15.301","A15.302","A15.303","A15.304","A15.305","A15.306","A15.307","A15.400x001","A15.401","A15.402","A15.403","A15.404","A15.405","A15.406","A15.407","A15.408","A15.409","A15.500x001","A15.500x002","A15.500x003","A15.500x004","A15.500x010","A15.500x011","A15.500x012","A15.500x013","A15.500x014","A15.500x015","A15.500x016","A15.500x017","A15.500x018","A15.500x019","A15.500x020","A15.500x021","A15.500x022","A15.500x023","A15.500x024","A15.500x025","A15.500x026","A15.500x027","A15.500x028","A15.500x029","A15.501","A15.502","A15.503","A15.504","A15.505","A15.506","A15.507","A15.508","A15.509","A15.601","A15.602","A15.603","A15.604","A15.605","A15.606","A15.607","A15.608","A15.609","A15.701","A15.702","A15.703","A15.800x001","A15.801","A15.802","A15.803","A15.804","A15.805","A15.806","A15.807","A15.808","A15.809","A15.810","A15.811","A15.812","A15.813","A15.814","A15.900","A15.901","A16.000x001","A16.000x002","A16.001","A16.002","A16.003","A16.004","A16.005","A16.006","A16.007","A16.008","A16.009","A16.010","A16.011","A16.012","A16.013","A16.014","A16.015","A16.016","A16.017","A16.018","A16.019","A16.020","A16.021","A16.022","A16.023","A16.024","A16.025","A16.026","A16.027","A16.028","A16.029","A16.030","A16.031","A16.032","A16.033","A16.034","A16.035","A16.036","A16.037","A16.038","A16.100x001","A16.101","A16.102","A16.103","A16.104","A16.105","A16.106","A16.107","A16.108","A16.109","A16.200x002","A16.200x002","A16.200x002","A16.200x007","A16.200x012","A16.200x013","A16.200x013","A16.200x014","A16.200x015","A16.201","A16.202","A16.203","A16.204","A16.205","A16.206","A16.207","A16.210","A16.300x002","A16.300x003","A16.300x007","A16.301","A16.302","A16.303","A16.304","A16.305","A16.400x005","A16.400x010","A16.400x011","A16.401","A16.402","A16.402","A16.402","A16.403","A16.405","A16.406","A16.500x001","A16.500x004","A16.500x004","A16.500x008","A16.500x009","A16.500x010","A16.501","A16.503","A16.504","A16.505","A16.700x001","A16.700x002","A16.700x002","A16.800x002","A16.800x003","A16.801","A16.802","A16.803","A16.804","A16.805","A16.806","A16.807","A16.900x001","A16.900x002","A16.900x003","A16.900x023","A19.000","A19.000x001","A19.000x002","A19.000x003","A19.000x004","A19.000x005","A19.000x006","A19.000x007","A19.000x008","A19.000x009","A19.000x010","A19.000x011","A19.000x012","A19.000x013","A19.000x014","A19.000x015","A19.000x016","A19.000x017","A19.000x018","A19.000x019","A19.000x020","A19.001","A19.801","A19.802","A19.803","A21.201+J17.0*","A22.102+J17.0*","A36.201","A37.000","A37.100","A37.800x001","A37.900","A37.900x003","A37.900x004","A37.901+J17.0*","A43.000x001+J99.8*","A52.704+J99.8*","A54.806+J17.0*","B01.200+J17.1*","B05.200+J17.1*","B06.800","B06.801+J17.1*","B25.000+J17.1*","B33.400x001+J17.1*","B37.100","B37.101+J17.2*","B37.800x083","B37.803","B38.000","B38.000x001+J17.2*","B38.100","B38.100x001+J17.2*","B38.200","B38.200x001+J17.2*","B39.000","B39.000x001+J17.2*","B39.100","B39.100x001+J17.2*","B39.200","B39.200x001+J17.2*","B40.000","B40.100","B40.200","B41.000","B42.000+J99.8*","B44.000x001+J99.8*","B44.101+J99.8*","B44.102+J17.2*","B45.000","B45.000x002+J99.8*","B46.000x001+J99.8*","B48.500+J17.2*","B48.501+J17.2*","B48.502+J17.2*","B49.x00x011","B49.x13","B49.x14+J99.8*","B58.300+J17.3*","B65.902+J99.8*","B65.907+I52.1*","B66.401+J99.8*","B67.100x001+J99.8*","B77.801+J17.3*","C33.x00","C34.000","C34.000x002","C34.000x003","C34.001","C34.100x003","C34.100x004","C34.101","C34.102","C34.201","C34.300x003","C34.300x004","C34.301","C34.800","C34.800x001","C34.800x002","C34.800x003","C34.801","C34.802","C34.803","C34.900x001","C34.900x004","C34.900x005","C34.900x006","C34.900x008","C34.901","C34.902","C37.x00","C38.100","C38.200","C38.300","C38.400","C38.400x003","C38.401","C38.800","C39.800","C39.900x001","C45.000","C45.700","C45.701","C45.702","C46.701","C49.300x001","C49.300x003","C49.302","C76.100","C76.100x003","C77.100","C77.100x004","C77.101","C77.102","C77.103","C77.104","C77.105","C78.000","C78.000x003","C78.001","C78.002","C78.003","C78.100","C78.200","C78.201","C78.304","C78.306","C79.800x809","C79.800x829","C79.800x838","C79.807","C79.810","D02.100","D02.200x002","D02.201","D02.400","D14.200","D14.300x001","D14.301","D14.302","D14.400","D15.000","D15.200","D15.200x001","D15.200x002","D15.700","D15.701","D15.900","D17.400x001","D17.400x002","D17.400x003","D17.400x004","D17.400x005","D17.700x019","D17.700x023","D18.000x800","D18.000x814","D18.000x857","D18.011","D18.100x015","D18.100x025","D18.100x026","D19.000","D21.302","D36.700x008","D36.700x013","D36.706","D36.717","D38.100x001","D38.100x002","D38.100x003","D38.101","D38.102","D38.103","D38.104","D38.105","D38.200x001","D38.201","D38.300x001","D38.300x002","D38.300x003","D38.301","D38.400x001","D38.401","D38.600x001","D38.601","D48.115","D48.700x019","D48.709","D48.710","D86.000","D86.200","E32.000","E32.000x003","E32.001","E32.002","E32.100","E32.800x001","E32.800x004","E32.800x005","E32.801","E32.802","E32.900","E83.104+J99.8*","E84.001","E85.400x005","E85.404","E85.407","E85.412+J99.8*","E89.802","G47.300x034","I00.x00x007+J17.8*","I26.900x001","I26.900x002","I26.900x003","I26.900x005","I26.900x006","I26.900x007","I26.900x008","I26.900x009","I26.900x010","I26.900x011","I26.900x012","I26.900x013","I26.900x015","I26.900x016","I26.900x017","I26.900x018","I26.901","I26.902","I28.800x010","I88.106","I88.107","I88.900x008","I89.000x016","I89.000x027","I89.000x028","I89.000x029","I89.003","I89.800x002","I89.800x007","I89.800x016","I89.800x017","I89.800x018","I89.800x021","I89.800x023","I89.804","I89.807","I97.800x018","J09.x00","J09.x01","J09.x02","J10.000","J10.000x001","J10.001","J10.100x005","J11.000x001","J11.100x005","J12.000","J12.100","J12.200","J12.300","J12.800","J12.900","J13.x00","J14.x00","J15.000","J15.000x002","J15.100","J15.101","J15.200","J15.300","J15.400","J15.402","J15.500","J15.600x002","J15.600x003","J15.600x005","J15.600x006","J15.601","J15.602","J15.700","J15.800x001","J15.800x002","J15.900","J15.901","J15.902","J15.903","J16.000","J16.800x001","J18.000","J18.000x001","J18.000x002","J18.001","J18.002","J18.100","J18.200","J18.800x001","J18.800x002","J18.800x004","J18.800x006","J18.800x012","J18.801","J18.802","J18.803","J18.900","J18.901","J18.902","J18.903","J20.000","J20.100","J20.200","J20.300","J20.400","J20.500","J20.600","J20.700","J20.800","J20.900","J20.901","J20.902","J21.000","J21.100","J21.801","J21.900","J21.900x002","J21.901","J22.x00","J39.801","J39.802","J39.803","J39.804","J39.805","J39.806","J39.807","J39.808","J39.810","J40.x00","J40.x00x002","J40.x01","J41.000","J41.100","J41.800","J42.x00","J42.x00x001","J42.x00x003","J42.x00x004","J42.x00x005","J42.x00x006","J42.x01","J43.000","J43.000x003","J43.001","J43.100","J43.101","J43.200","J43.800x001","J43.900","J43.900x001","J43.901","J43.902","J43.903","J43.904","J44.000","J44.100","J44.800x001","J44.800x001","J44.801","J44.802","J44.803","J44.805","J44.806","J44.807","J44.900","J44.900x002","J44.900x003","J44.900x004","J44.900x005","J45.000","J45.000x001","J45.000x003","J45.002","J45.003","J45.004","J45.005","J45.006","J45.007","J45.100","J45.100x002","J45.100x003","J45.800","J45.900","J45.900x001","J45.900x002","J45.900x011","J45.900x012","J45.900x013","J45.900x021","J45.900x023","J45.900x031","J45.900x041","J45.901","J45.902","J45.903","J46.x00x002","J46.x00x003","J46.x00x006","J46.x00x008","J46.x00x009","J46.x00x010","J46.x01","J46.x02","J47.x00","J47.x01","J47.x02","J47.x03","J60.x00","J60.x00x002","J60.x00x003","J60.x00x004","J60.x00x005","J60.x01","J61.x00x001","J61.x00x002","J61.x00x003","J61.x01","J62.000x001","J62.000x002","J62.000x003","J62.001","J62.800x002","J62.800x003","J62.800x004","J62.800x005","J62.800x006","J62.800x007","J62.800x008","J62.801","J62.802","J62.803","J62.804","J63.000","J63.000x001","J63.000x002","J63.000x003","J63.001","J63.100","J63.200","J63.201","J63.300x001","J63.300x002","J63.300x003","J63.301","J63.400","J63.500","J63.800","J63.800x001","J63.800x003","J63.800x005","J63.800x009","J63.800x010","J63.800x011","J63.800x012","J63.800x013","J63.800x014","J63.800x015","J63.800x016","J63.800x017","J63.800x018","J63.800x019","J63.800x020","J63.800x021","J63.800x022","J63.800x023","J63.800x024","J63.800x025","J63.800x026","J63.801","J63.802","J63.803","J64.x00","J65.x00","J66.000","J66.100","J66.200","J66.800","J67.000","J67.100","J67.200","J67.200x002","J67.200x003","J67.300","J67.400","J67.400x002","J67.500","J67.600","J67.600x001","J67.700x001","J67.700x002","J67.800x001","J67.800x002","J67.800x003","J67.800x004","J67.800x005","J67.900","J68.000x001","J68.000x002","J68.001","J68.002","J68.101","J68.201","J68.301","J68.400","J68.800","J68.900","J69.000","J69.000x002","J69.000x004","J69.001","J69.100x001","J69.101","J69.800x001","J70.001","J70.101","J70.200","J70.200x002","J70.300","J70.400","J70.800","J70.900","J80.x00","J80.x01","J81.x00","J81.x00x002","J82.x00x001","J82.x00x002","J82.x00x004","J82.x00x005","J82.x01","J84.000x003","J84.001","J84.002","J84.100x006","J84.100x007","J84.100x008","J84.101","J84.102","J84.103","J84.104","J84.105","J84.108","J84.109","J84.110","J84.800x003","J84.800x004","J84.800x005","J84.800x006","J84.800x007","J84.800x008","J84.801","J84.802","J84.803","J84.804","J84.805","J84.900","J85.000x002","J85.001","J85.002","J85.100","J85.200","J85.300","J86.000","J86.000x006","J86.000x012","J86.000x013","J86.001","J86.002","J86.003","J86.004","J86.005","J86.006","J86.007","J86.008","J86.009","J86.010","J86.011","J86.012","J86.013","J86.014","J86.015","J86.016","J86.017","J86.018","J86.019","J86.020","J86.901","J86.902","J86.903","J90.x00","J90.x00x002","J90.x00x003","J90.x00x004","J90.x00x005","J90.x01","J90.x02","J92.000","J92.900x002","J92.901","J93.003","J93.100x001","J93.100x002","J93.800x001","J93.900","J94.101","J94.200","J94.201","J94.800x003","J94.800x004","J94.800x010","J94.801","J94.802","J94.804","J94.805","J94.806","J94.807","J94.900x001","J94.901","J95.100","J95.200","J95.300","J95.401","J95.800x004","J95.800x009","J95.800x010","J95.800x012","J95.800x016","J95.800x021","J95.801","J95.802","J95.804","J95.808","J95.810","J95.811","J95.900","J96.000","J96.100","J96.900x001","J96.900x002","J96.900x003","J98.000x009","J98.000x011","J98.000x012","J98.000x013","J98.001","J98.002","J98.003","J98.004","J98.005","J98.006","J98.007","J98.008","J98.009","J98.010","J98.011","J98.100","J98.101","J98.102","J98.200","J98.201","J98.300","J98.400x001","J98.400x005","J98.400x008","J98.400x012","J98.400x013","J98.400x016","J98.400x019","J98.401","J98.402","J98.403","J98.404","J98.405","J98.407","J98.408","J98.409","J98.410","J98.411","J98.412","J98.413","J98.414","J98.415","J98.416","J98.417","J98.418","J98.500x001","J98.500x007","J98.500x008","J98.501","J98.502","J98.503","J98.504","J98.505","J98.506","J98.507","J98.508","J98.600x001","J98.601","J98.602","J98.700","J98.800x001","J98.800x003","J98.800x004","J98.800x006","J98.800x007","J98.800x009","J98.800x014","J98.800x016","J98.800x018","J98.801","J98.802","J98.901","M05.100+J99.0*","M05.101+J99.0*","M05.102+J99.0*","M05.103+J99.0*","M31.300x002","M31.302+J99.1*","M31.304+J99.1*","M32.103+J99.1*","M33.001+J99.1*","M33.103+J99.1*","M33.201+J99.1*","M33.901+J99.1*","M34.800x001+J99.1*","M34.801+J99.1*","M35.002+J99.1*","M35.904+J99.1*","Q32.102","Q32.200","Q32.300","Q32.400x002","Q32.400x004","Q32.400x005","Q32.401","Q32.402","Q33.000","Q33.002","Q33.003","Q33.100","Q33.100","Q33.200","Q33.301","Q33.400","Q33.500","Q33.600","Q33.800x001","Q33.800x002","Q33.900","Q34.000","Q34.100","Q34.900","Q79.000","Q79.101","Q79.102","Q79.103","Q85.900x015","Q85.901","Q85.904","Q85.908","Q89.209","Q89.800x910","R04.200","R04.800x002","R04.800x004","R04.802","R04.900","R05.x00","R05.x01","R05.x02","R06.000","R06.000x002","R06.000x003","R06.100","R06.200","R06.300","R06.301","R06.400","R06.600","R06.800x005","R06.801","R06.802","R06.803","R06.804","R06.805","R06.806","R09.000","R09.100","R09.100x002","R09.101","R09.200","R09.201","R09.300","R09.800x091","R09.800x092","R09.800x093","R09.800x094","R09.800x095","R09.801","R59.009","R84.000","R84.100","R84.200","R84.300","R84.400","R84.500","R84.600","R84.700","R84.800","R84.903","R84.904","R91.x00x001","R91.x00x005","R91.x01","R91.x03","R91.x04","R93.801","R93.804","R93.805","R94.200","R94.201","R94.202","R94.204","S24.200","S25.401","S27.000","S27.010","S27.100","S27.110","S27.200","S27.210","S27.300x012","S27.301","S27.302","S27.303","S27.310","S27.311","S27.312","S27.313","S27.400","S27.401","S27.410","S27.500","S27.501","S27.510","S27.600","S27.610","S27.700","S27.710","S27.800x013","S27.801","S27.802","S27.803","S27.804","S27.805","S27.806","S27.807","S27.808","S27.810","S27.811","S27.812","S27.900","S27.910","S28.000","S28.100","S29.700","S29.800","S29.900","T17.400","T17.500","T17.501","T17.801","T17.802","T17.803","T17.804","T17.900","T17.901","T27.200x001","T27.300","T27.500x001","T27.600x001","T27.600x001","T27.600x001","T27.700","T79.800x007","T81.400x009","T84.200x004","T85.608","T85.700x804","T86.800x011","T86.803","U04.900","U07.000","U07.100x001","U07.100x002","U07.100x003","Z03.800x001"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCE入组条件，匹配规则：主诊断匹配')

  result=EB1.group(record)
  if result:
    return result
  result=EB2.group(record)
  if result:
    return result
  result=EC1.group(record)
  if result:
    return result
  result=EC2.group(record)
  if result:
    return result
  result=ED1.group(record)
  if result:
    return result
  result=EJ1.group(record)
  if result:
    return result

  if record.ssList and record.ssList[0] in SS_VALID:
    message('符合EQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'EQY'

  result=ER1.group(record)
  if result:
    return result

  result=ER2.group(record)
  if result:
    return result

  result=ER3.group(record)
  if result:
    return result

  result=ES1.group(record)
  if result:
    return result

  result=ES2.group(record)
  if result:
    return result

  result=ES3.group(record)
  if result:
    return result

  result=ET1.group(record)
  if result:
    return result

  result=ET2.group(record)
  if result:
    return result

  result=EU1.group(record)
  if result:
    return result

  result=EV1.group(record)
  if result:
    return result

  result=EW1.group(record)
  if result:
    return result

  result=EX1.group(record)
  if result:
    return result

  result=EX2.group(record)
  if result:
    return result

  result=EZ1.group(record)
  if result:
    return result

  message('不符合MDCE的ADRG入组条件')

