from drg_group.wuhan_2022.Base import has_mcc,has_cc,intersect
def PB19_group(record):
  return True
def PC19_group(record):
  return True
def PJ19_group(record):
  return True
def PR19_group(record):
  return True
def PS19_group(record):
  return True
def PT19_group(record):
  return True
def PT29_group(record):
  return True
def PV19_group(record):
  return True
def PK11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PU1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def PK1B_group(record):
  return True
def PU15_group(record):
  return True

