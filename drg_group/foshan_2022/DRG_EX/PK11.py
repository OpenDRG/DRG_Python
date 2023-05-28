from drg_group.foshan_2022.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["96.7101"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss) and record.ageDay!=None and record.ageDay<=28:
    message('符合PK11入组条件，匹配规则：主手术匹配、某一手术匹配、新生儿')
    return True