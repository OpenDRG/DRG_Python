from drg_group.wuhan_2022.Base import messages,has_mcc,has_cc,intersect
def XS29_group(record):
  return True
def XT29_group(record):
  return True
def XR29_group(record):
  return True
def XR19_group(record):
  return True
def XJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def XS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def XT31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def XT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def XT33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def XS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def XJ1B_group(record):
  return True
def XT1B_group(record):
  return True
def XT35_group(record):
  return True
def XS15_group(record):
  return True

