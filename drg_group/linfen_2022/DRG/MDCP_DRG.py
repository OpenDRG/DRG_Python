from drg_group.linfen_2022.Base import has_mcc,has_cc,intersect
def PK19_group(record):
  return True
def PR19_group(record):
  return True
def PS19_group(record):
  return True
def PS39_group(record):
  return True
def PS49_group(record):
  return True
def PV19_group(record):
  return True
def PU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PU15_group(record):
  return True

