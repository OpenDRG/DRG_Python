from drg_group.liaocheng_2022.Base import has_mcc,has_cc,intersect
def CD10_group(record):
    return record.age<=17
def CB29_group(record):
  return True
def CD19_group(record):
  return True
def CD29_group(record):
  return True
def CJ19_group(record):
  return True
def CR19_group(record):
  return True
def CT19_group(record):
  return True
def CU19_group(record):
  return True
def CV19_group(record):
  return True
def CB31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CB41_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CX11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CW13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CX13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CB35_group(record):
  return True
def CB45_group(record):
  return True
def CC15_group(record):
  return True
def CS15_group(record):
  return True
def CW15_group(record):
  return True
def CX15_group(record):
  return True
def CZ15_group(record):
  return True

