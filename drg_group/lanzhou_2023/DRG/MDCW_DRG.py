from drg_group.lanzhou_2023.Base import has_mcc,has_cc,intersect
def WB19_group(record):
  return True
def WC19_group(record):
  return True
def WJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def WR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def WZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def WJ1B_group(record):
  return True
def WR1B_group(record):
  return True
def WZ1B_group(record):
  return True

