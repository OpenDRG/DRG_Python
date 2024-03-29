from drg_group.changzhou_2022.Base import has_mcc,has_cc,intersect
def CS10_group(record):
    return record.age<=17
def CB29_group(record):
  return True
def CB49_group(record):
  return True
def CC19_group(record):
  return True
def CD19_group(record):
  return True
def CD29_group(record):
  return True
def CJ19_group(record):
  return True
def CR19_group(record):
  return True
def CS19_group(record):
  return True
def CU19_group(record):
  return True
def CV19_group(record):
  return True
def CW19_group(record):
  return True
def CX19_group(record):
  return True
def CB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CB31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CB13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CB33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CB15_group(record):
  return True
def CB35_group(record):
  return True
def CT15_group(record):
  return True
def CZ15_group(record):
  return True

