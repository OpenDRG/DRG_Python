from drg_group.foshan_2022.Base import has_mcc,has_cc,intersect
def BB20_group(record):
    return record.icuHours>120
def BE20_group(record):
    return record.icuHours>120
def BR10_group(record):
    return record.icuHours>120
def BR20_group(record):
    return record.icuHours>120
def BE26_group(record):
  return 1<=record.icuHours<=120
def BR29_group(record):
  return 1<=record.icuHours<=120
def BR28_group(record):
  return record.inHospitalTime>60
def BX18_group(record):
  return record.inHospitalTime>60
def BZ18_group(record):
  return record.inHospitalTime>60
def BV16_group(record):
  return record.age<17 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BV17_group(record):
  return record.age<17
def BB19_group(record):
  return True
def BC19_group(record):
  return True
def BD19_group(record):
  return True
def BD29_group(record):
  return True
def BE19_group(record):
  return True
def BS19_group(record):
  return True
def BT19_group(record):
  return True
def BW19_group(record):
  return True
def BW29_group(record):
  return True
def BC21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BE23_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BM11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BR24_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BT21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BU21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BU31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BX11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BX21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BY11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BZ16_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def BB23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BL13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BV23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BV33_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BY23_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def BM13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def BR25_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def BT23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def BU13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def BV13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def BX13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def BX23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def BY13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def BC23_group(record):
  return True
def BE25_group(record):
  return True
def BU23_group(record):
  return True
def BU33_group(record):
  return True
def BZ17_group(record):
  return True
def BB25_group(record):
  return True
def BJ15_group(record):
  return True
def BL15_group(record):
  return True
def BM15_group(record):
  return True
def BR15_group(record):
  return True
def BR26_group(record):
  return True
def BT25_group(record):
  return True
def BU15_group(record):
  return True
def BV15_group(record):
  return True
def BV25_group(record):
  return True
def BV35_group(record):
  return True
def BX15_group(record):
  return True
def BX25_group(record):
  return True
def BY15_group(record):
  return True
def BY25_group(record):
  return True

