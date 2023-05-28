from drg_group.foshan_2022.Base import has_mcc,has_cc,intersect
def EJ10_group(record):
    return record.icuHours>120
def ES30_group(record):
    return record.icuHours>120
def ET20_group(record):
    return record.icuHours>120
def ES32_group(record):
  return 1<=record.icuHours<=120
def ET22_group(record):
  return 1<=record.icuHours<=120
def ES36_group(record):
  return record.age<17 and has_mcc(record.zdList[0],record.zdList[1:])
def EX26_group(record):
  return record.age<17 and has_mcc(record.zdList[0],record.zdList[1:])
def ES37_group(record):
  return record.age<17 and has_cc(record.zdList[0],record.zdList[1:])
def ES38_group(record):
  return record.age<17
def EX27_group(record):
  return record.age<17
def EB29_group(record):
  return True
def EC19_group(record):
  return True
def EC29_group(record):
  return True
def EU19_group(record):
  return True
def EV19_group(record):
  return True
def EB11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ED11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def EJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ER11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ER21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ER31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ES11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ES21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ES31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ET11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def ET21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def EW11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def EX21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def EX13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def EZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def EB13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def ED13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def EJ13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def ER13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def ER23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def ES13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def ES33_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def ET13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def ET23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def EW13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def EX23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def ER33_group(record):
  return True
def ES23_group(record):
  return True
def EB15_group(record):
  return True
def ED15_group(record):
  return True
def EJ15_group(record):
  return True
def ER15_group(record):
  return True
def ER25_group(record):
  return True
def ES15_group(record):
  return True
def ES35_group(record):
  return True
def ET15_group(record):
  return True
def ET25_group(record):
  return True
def EW15_group(record):
  return True
def EX15_group(record):
  return True
def EX25_group(record):
  return True
def EZ15_group(record):
  return True

