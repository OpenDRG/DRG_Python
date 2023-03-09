from drg_group.fuzhou_2022.Base import has_mcc,has_cc,intersect
def AH11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def AH15_group(record):
  return True

