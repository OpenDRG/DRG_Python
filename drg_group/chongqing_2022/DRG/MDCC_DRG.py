from drg_group.chongqing_2022.Base import has_mcc,has_cc,intersect
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
def CD29_group(record):
  return True
def CJ19_group(record):
  return True
def CS19_group(record):
  return True
def CU19_group(record):
  return True
def CW19_group(record):
  return True
def CX19_group(record):
  return True
def CR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CV13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CR15_group(record):
  return True
def CT15_group(record):
  return True
def CV15_group(record):
  return True
def CZ15_group(record):
  return True

