import time
from drg_group.yancheng_2023.Base import DrgGroupStatus,MedicalRecord,GroupResult,groupMessages,output,DRG
from drg_group.yancheng_2023.Grouper import group

class Grouper_yancheng_2023:
  
  def __init__(self, **kwargs):
    self.kwargs=kwargs

  def group(self,record):
    result=group(record)
    output('***',result,DRG.get(result,DrgGroupStatus.FAIL.value),'***')
    if result=='0000':
      return GroupResult(record.Index,DrgGroupStatus.FAIL.value,self.return_messages(),'0000','00','0000')
    elif result[1:3]=='00':
      return GroupResult(record.Index,DrgGroupStatus.FAIL.value,self.return_messages(),'MDC'+result[0],'00','0000')
    elif result[1:3]=='QY':
      return GroupResult(record.Index,DrgGroupStatus.QY.value,self.return_messages(),'MDC'+result[0],'QY',result)
    else:
      return GroupResult(record.Index,DrgGroupStatus.SUCCESS.value,self.return_messages(),'MDC'+result[0],result[:3],result)

  def return_messages(self):
    result=groupMessages.copy()
    groupMessages.clear()
    for mdc in ['MDCA','MDCV','MDCX']:
      s='不符合%s的ADRG入组条件'%(mdc)
      if s in result:
        i=result.index(s)
        del result[i]
        del result[i-1]
    return result 

if __name__ == "__main__":
  grouper=Grouper_yancheng_2023()
  record=MedicalRecord(Index=1653890, gender=2, age=10, ageDay=21, weight=3200, dept='0302',inHospitalTime=14,leavingType='1',
    zdList='Z51.103,C15.900'.split(','), 
    ssList='99.2503'.split(','))
  s1 = time.time()
  result=grouper.group(record)
  s2 = time.time()
  print(result)
  print((s2-s1)*1000)