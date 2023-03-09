from drg_group.fuzhou_2022.Base import has_mcc,has_cc,intersect
def JS29_group(record):
  return True
def JT19_group(record):
  return True
def JV19_group(record):
  return True
def JV29_group(record):
  return True
def JZ19_group(record):
  return True
def JU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def JU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def JU15_group(record):
  return True

