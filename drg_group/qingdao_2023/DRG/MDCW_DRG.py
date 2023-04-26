from drg_group.qingdao_2023.Base import has_mcc,has_cc,intersect
def WC19_group(record):
  return True
def WJ19_group(record):
  return True
def WZ19_group(record):
  return True
def WB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def WR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def WR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def WB15_group(record):
  return True
def WR15_group(record):
  return True

