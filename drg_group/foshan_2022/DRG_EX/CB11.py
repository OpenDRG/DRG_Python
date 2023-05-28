from drg_group.foshan_2022.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["14.0201","14.2102","14.2202","14.2302","14.2402","14.2500","14.2602","14.2900X001","14.2900X002","14.2900X003","14.2902","14.3101","14.3200X002","14.3300","14.3400","14.3500","14.4902","14.4903","14.5101","14.5200X001","14.5300X001","14.5400X001","14.5500","14.5902","14.5903","14.5904","14.5905","14.7100X001","14.7300X001","14.7401","14.9X01","14.9X02","14.9X03","14.9X05","14.9X06","14.9X08","13.1900X006","13.1900X008","13.1901","13.1902","13.3X01","13.4100X001","13.4101","13.4200X001","13.4300X001","13.5900X001","13.6400X001","13.6500X002","13.6600","13.7100X001","13.7200X001"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss) and record.ssList and intersect(record.ssList,adrg_ss) and intersect(record.ssList,adrg_ss1):
    message('符合CB11入组条件，匹配规则：主手术匹配、某一手术匹配、双手术匹配')
    return True