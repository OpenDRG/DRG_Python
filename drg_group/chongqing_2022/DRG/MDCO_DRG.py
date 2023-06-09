from drg_group.chongqing_2022.Base import has_mcc,has_cc,intersect
def OB19_group(record):
  return True
def OC19_group(record):
  return True
def OD29_group(record):
  return True
def OE19_group(record):
  return True
def OF19_group(record):
  return True
def OF29_group(record):
  return True
def OR19_group(record):
  return True
def OS19_group(record):
  return True
def OS29_group(record):
  return True
def OZ19_group(record):
  return True
def OD11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def OJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def OT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def OD13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def OJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def OT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def OD15_group(record):
  return True
def OJ15_group(record):
  return True
def OT15_group(record):
  return True

