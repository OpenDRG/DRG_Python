from drg_group.foshan_2022.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["17.2100X001","17.2200X001","17.2300X001","17.2400X001","53.1000","53.1101","53.1200X001","53.1201","53.1202","53.1203","53.1301","53.1401","53.1501","53.1601","53.1701","53.3100X001","53.3101","53.3901"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GE11入组条件，匹配规则：主手术匹配、某一手术匹配')
    return True