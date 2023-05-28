from drg_group.foshan_2022.Base import has_mcc,has_cc,intersect
def ZB19_group(record):
  return True
def ZD19_group(record):
  return True
def ZZ19_group(record):
  return True
def ZC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ZC13_group(record):
  return True
def ZJ13_group(record):
  return True

