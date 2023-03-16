from drg_group.yancheng_2022.Base import has_mcc,has_cc,intersect
def OB19_group(record):
  return True
def OC19_group(record):
  return True
def OD19_group(record):
  return True
def OD29_group(record):
  return True
def OE19_group(record):
  return True
def OF19_group(record):
  return True
def OF29_group(record):
  return True
def OJ19_group(record):
  return True
def OR19_group(record):
  return True
def OS29_group(record):
  return True
def OT19_group(record):
  return True
def OZ19_group(record):
  return True
def OS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def OS15_group(record):
  return True

