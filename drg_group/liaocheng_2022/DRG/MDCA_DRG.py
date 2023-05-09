from drg_group.liaocheng_2022.Base import has_mcc,has_cc,intersect
def AB19_group(record):
  return True
def AG19_group(record):
  return True
def AG29_group(record):
  return True
def AH11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def AH15_group(record):
  return True

