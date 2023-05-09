from drg_group.nanping_2023.Base import has_mcc,has_cc,intersect
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
def CW19_group(record):
  return True
def CX19_group(record):
  return True
def CZ19_group(record):
  return True
def CB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CD21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CB13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CD23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CB15_group(record):
  return True
def CD25_group(record):
  return True
def CV15_group(record):
  return True

