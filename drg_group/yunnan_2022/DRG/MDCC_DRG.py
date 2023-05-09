from drg_group.yunnan_2022.Base import has_mcc,has_cc,intersect
def CB19_group(record):
  return True
def CB29_group(record):
  return True
def CB39_group(record):
  return True
def CB49_group(record):
  return True
def CC19_group(record):
  return True
def CD19_group(record):
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
def CZ19_group(record):
  return True
def CD23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CW13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CX13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CD25_group(record):
  return True
def CW15_group(record):
  return True
def CX15_group(record):
  return True

