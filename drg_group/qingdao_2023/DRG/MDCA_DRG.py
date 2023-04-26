from drg_group.qingdao_2023.Base import has_mcc,has_cc,intersect
def AA19_group(record):
  return True
def AC19_group(record):
  return True
def AE19_group(record):
  return True
def AF19_group(record):
  return True
def AG19_group(record):
  return True
def AG29_group(record):
  return True
def AH19_group(record):
  return True
def AB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def AB15_group(record):
  return True

