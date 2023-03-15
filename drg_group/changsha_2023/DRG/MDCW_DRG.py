from drg_group.changsha_2023.Base import has_mcc,has_cc,intersect
def WB19_group(record):
  return True
def WC19_group(record):
  return True
def WJ19_group(record):
  return True
def WZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def WR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def WR15_group(record):
  return True
def WZ15_group(record):
  return True

