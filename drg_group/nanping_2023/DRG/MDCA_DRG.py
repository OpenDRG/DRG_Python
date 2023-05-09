from drg_group.nanping_2023.Base import has_mcc,has_cc,intersect
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
def AH11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def AH13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def AH15_group(record):
  return True

