from drg_group.wuhan_2022.Base import messages,has_mcc,has_cc,intersect
def CD29_group(record):
  return True
def CD19_group(record):
  return True
def CB39_group(record):
  return True
def CB29_group(record):
  return True
def CV19_group(record):
  return True
def CU19_group(record):
  return True
def CW19_group(record):
  return True
def CJ19_group(record):
  return True
def CB19_group(record):
  return True
def CR19_group(record):
  return True
def CB49_group(record):
  return True
def CC19_group(record):
  return True
def CX1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CZ1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CS1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CT1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CX15_group(record):
  return True
def CS15_group(record):
  return True
def CZ15_group(record):
  return True
def CT15_group(record):
  return True

