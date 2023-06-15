from drg_group.yunnan_2022.Base import message,intersect,SS_VALID
from drg_group.yunnan_2022.DRG import MDCC_DRG

def group(record):
  adrg_zd=["E05.902+H58.8*","E10.300x011+H36.0*","E10.300x012+H36.0*","E10.300x013+H36.0*","E10.300x014+H36.0*","E10.300x015+H36.0*","E10.300x021+H36.0*","E10.300x022+H36.0*","E10.300x023+H36.0*","E10.300x024+H36.0*","E10.300x025+H36.0*","E10.300x031+H36.0*","E10.300x032+H36.0*","E10.300x033+H36.0*","E10.300x034+H36.0*","E10.300x035+H36.0*","E10.300x036+H36.0*","E10.300x041+H36.0*","E10.300x042+H36.0*","E10.300x043+H36.0*","E10.300x044+H36.0*","E10.300x045+H36.0*","E10.300x046+H36.0*","E10.300x047+H36.0*","E10.300x052+H22.1*","E10.300x053+H36.0*","E10.301+H36.0*","E10.303+H22.1*","E11.300x011+H36.0*","E11.300x012+H36.0*","E11.300x013+H36.0*","E11.300x014+H36.0*","E11.300x015+H36.0*","E11.300x021+H36.0*","E11.300x022+H36.0*","E11.300x023+H36.0*","E11.300x024+H36.0*","E11.300x025+H36.0*","E11.300x031+H36.0*","E11.300x032+H36.0*","E11.300x033+H36.0*","E11.300x034+H36.0*","E11.300x035+H36.0*","E11.300x036+H36.0*","E11.300x041+H36.0*","E11.300x042+H36.0*","E11.300x043+H36.0*","E11.300x044+H36.0*","E11.300x045+H36.0*","E11.300x046+H36.0*","E11.300x047+H36.0*","E11.300x052+H22.1*","E11.300x053+H36.0*","E11.301+H36.0*","E11.303+H22.1*","E12.300","E13.300x271+H36.0*","E13.300x571+H36.0*","E14.300x011+H36.0*","E14.300x012+H36.0*","E14.300x013+H36.0*","E14.300x014+H36.0*","E14.300x015+H36.0*","E14.300x021+H36.0*","E14.300x022+H36.0*","E14.300x023+H36.0*","E14.300x024+H36.0*","E14.300x025+H36.0*","E14.300x031+H36.0*","E14.300x032+H36.0*","E14.300x033+H36.0*","E14.300x034+H36.0*","E14.300x035+H36.0*","E14.300x036+H36.0*","E14.300x041+H36.0*","E14.300x042+H36.0*","E14.300x043+H36.0*","E14.300x044+H36.0*","E14.300x045+H36.0*","E14.300x046+H36.0*","E14.300x047+H36.0*","E14.300x051+H42.0*","E14.300x052+H22.1*","E14.300x053+H36.0*","E14.300x054+H22.1*","E14.300x071+H36.0*","E14.400x180+G59.0*","H35.004","N18.504+H32.8*","N18.508+H32.8*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合CX1入组条件，匹配规则：主诊断匹配')
    
    
    if MDCC_DRG.CX13_group(record):
      return 'CX13'

    if MDCC_DRG.CX15_group(record):
      return 'CX15'

    return ''
  else:
    return ''
