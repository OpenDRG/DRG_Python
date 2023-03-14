from drg_group.zhejiang_2022.Base import has_mcc,has_cc,intersect
def AA19_group(record):
  return True
def AB19_group(record):
  return True
def AC19_group(record):
  return True
def AD19_group(record):
  return True
def AE19_group(record):
  return True
def AF19_group(record):
  return True
def AG19_group(record):
  return True
def AG29_group(record):
  return True
def AH13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def AH11_group(record):
  return record.ssList and '39.6500' in record.ssList
def AH19_group(record):
  return record.ssList and intersect(record.ssList,['31.1x00x005','31.2100x001','31.2900x001','96.0400']) and '96.7201' in record.ssList

