from drg_group.taizhou_2022.Base import messages,has_mcc,has_cc,intersect
def XS29_group(record):
  return True
def XT19_group(record):
  return True
def XS19_group(record):
  return True
def XR29_group(record):
  return True
def XJ19_group(record):
  return True
def XT39_group(record):
  return True
def XR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def XT21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def XR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def XT23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def XR15_group(record):
  return True
def XT25_group(record):
  return True

