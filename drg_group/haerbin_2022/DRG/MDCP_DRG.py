from drg_group.haerbin_2022.Base import has_mcc,has_cc,intersect
def PB19_group(record):
  return True
def PC19_group(record):
  return True
def PJ19_group(record):
  return True
def PK19_group(record):
  return True
def PS19_group(record):
  return True
def PS29_group(record):
  return True
def PS49_group(record):
  return True
def PV19_group(record):
  return True
def PR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PS31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def PR1B_group(record):
  return True
def PS3B_group(record):
  return True
def PU15_group(record):
  return True

