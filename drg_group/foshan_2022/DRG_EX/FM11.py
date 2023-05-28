from drg_group.foshan_2022.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.0200X001","00.6600X004","00.6601","17.5500X002","17.5500X003","17.5500X004","17.5501","36.0400","36.3400","36.9900X011","36.9900X012","37.2800","37.3400X001","37.3400X002","37.3500X004","37.4900X008","37.4900X017","37.4900X018","37.6101","37.7800","37.9000X001","37.9200X001","37.9900X002","37.9900X003","39.4900X012"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FM11入组条件，匹配规则：其他手术匹配、某一手术匹配')
    return True