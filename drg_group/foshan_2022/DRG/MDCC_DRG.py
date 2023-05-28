from drg_group.foshan_2022.Base import has_mcc,has_cc,intersect
def CB13_group(record):
  return True
def CB29_group(record):
  return True
def CB39_group(record):
  return True
def CB49_group(record):
  return True
def CD29_group(record):
  return True
def CJ19_group(record):
  return True
def CR19_group(record):
  return True
def CV19_group(record):
  return True
def CW19_group(record):
  return True
def CZ19_group(record):
  return True
def CX11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def CC13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CD13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def CX13_group(record):
  return True
def CC15_group(record):
  return True
def CD15_group(record):
  return True
def CS15_group(record):
  return True
def CT15_group(record):
  return True
def CU15_group(record):
  return True

