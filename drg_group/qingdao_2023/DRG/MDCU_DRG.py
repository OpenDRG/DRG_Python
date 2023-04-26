from drg_group.qingdao_2023.Base import has_mcc,has_cc,intersect
def US19_group(record):
  return True
def UR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def UR15_group(record):
  return True

