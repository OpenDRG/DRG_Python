from drg_group.beijing_2022.Base import has_mcc,has_cc,intersect
def CB39_group(record):
  return True
def CB49_group(record):
  return True
def CJ19_group(record):
  return True
def CR19_group(record):
  return True
def CV19_group(record):
  return True
def CW19_group(record):
  return True
def CX19_group(record):
  return True
def CB13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CB23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CC13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CD23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CB15_group(record):
  return True
def CB25_group(record):
  return True
def CC15_group(record):
  return True
def CD25_group(record):
  return True
def CS15_group(record):
  return True
def CT15_group(record):
  return True
def CU15_group(record):
  return True
def CZ15_group(record):
  return True
def CD1D_group(record):
  return record.age<=6
def CD19_group(record):
  return True

