from drg_group.qingdao_2023.Base import has_mcc,has_cc,intersect
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
def OS29_group(record):
  return True
def OT19_group(record):
  return True
def OB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def OD11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def OZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def OJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def OS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def OB15_group(record):
  return True
def OD15_group(record):
  return True
def OJ15_group(record):
  return True
def OS15_group(record):
  return True
def OZ15_group(record):
  return True

