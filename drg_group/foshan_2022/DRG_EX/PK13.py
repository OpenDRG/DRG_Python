from drg_group.foshan_2022.Base import message,intersect,has_mcc,has_cc,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["93.9000x003","93.9001"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ageDay!=None and record.ageDay<=28 and has_mcc(record.zdList[0],record.zdList[1:]):
    message('符合PK13入组条件，匹配规则：主手术匹配、新生儿、伴严重并发症或合并症')
    return True