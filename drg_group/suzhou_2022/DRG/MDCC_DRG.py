from drg_group.suzhou_2022.Base import messages,has_mcc,has_cc

def CR19_group(record):
  return True

def CB39_group(record):
  return True

def CD29_group(record):
  return True

def CB49_group(record):
  return True

def CB19_group(record):
  return True

def CW19_group(record):
  return True

def CX19_group(record):
  return True

def CJ19_group(record):
  return True

def CB29_group(record):
  return True

def CD19_group(record):
  return True

def CV19_group(record):
  return True

def CC1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def CZ1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def CT1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def CS1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def CU1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))

def CS15_group(record):
  return True

def CZ15_group(record):
  return True

def CU15_group(record):
  return True

def CC15_group(record):
  return True

def CT15_group(record):
  return True

