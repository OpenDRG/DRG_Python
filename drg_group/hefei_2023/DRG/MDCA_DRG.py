from drg_group.hefei_2023.Base import has_mcc,has_cc,intersect
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
def AG21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def AH11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def AG23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def AG25_group(record):
  return True
def AH15_group(record):
  return True

