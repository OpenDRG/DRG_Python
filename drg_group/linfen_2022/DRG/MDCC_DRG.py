from drg_group.linfen_2022.Base import has_mcc,has_cc,intersect
def CB49_group(record):
  return True
def CJ19_group(record):
  return True
def CR19_group(record):
  return True
def CS19_group(record):
  return True
def CT19_group(record):
  return True
def CU19_group(record):
  return True
def CV19_group(record):
  return True
def CW19_group(record):
  return True
def CB13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CB23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CB33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CC13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CD13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CD23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CX13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CB15_group(record):
  return True
def CB25_group(record):
  return True
def CB35_group(record):
  return True
def CC15_group(record):
  return True
def CD15_group(record):
  return True
def CD25_group(record):
  return True
def CX15_group(record):
  return True
def CZ15_group(record):
  return True

