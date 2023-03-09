from drg_group.fuzhou_2022.Base import has_mcc,has_cc,intersect
def WJ19_group(record):
  return True
def WR19_group(record):
  return True
def WZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def WZ15_group(record):
  return True

