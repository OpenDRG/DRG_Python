from drg_group.guangxi_2022.Base import has_mcc,has_cc,intersect
def US19_group(record):
  return True
def UR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def UR15_group(record):
  return True

