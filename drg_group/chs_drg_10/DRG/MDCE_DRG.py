from drg_group.chs_drg_10.Base import has_mcc,has_cc,intersect
def EB19_group(record):
  return True
def EC19_group(record):
  return True
def ED19_group(record):
  return True
def EJ19_group(record):
  return True
def ER29_group(record):
  return True
def ES19_group(record):
  return True
def ES29_group(record):
  return True
def ET19_group(record):
  return True
def ET29_group(record):
  return True
def EU19_group(record):
  return True
def EV19_group(record):
  return True
def EW19_group(record):
  return True
def EX19_group(record):
  return True
def EX29_group(record):
  return True
def EZ19_group(record):
  return True
def ER11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ER31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ER13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def ER33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def ER15_group(record):
  return True
def ER35_group(record):
  return True

