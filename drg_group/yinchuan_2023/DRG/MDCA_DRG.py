from drg_group.yinchuan_2023.Base import has_mcc,has_cc,intersect
def AH11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])

