import time
from drg_group.yunnan_2022.Base import DrgGroupStatus,MedicalRecord,GroupResult,create_result,groupMessages,output,DRG
from drg_group.yunnan_2022.Grouper import group

class Grouper_yunnan_2022:
  
  def __init__(self, **kwargs):
    self.kwargs=kwargs

  def group(self,record):
    drgCode=group(record)
    
    output('***',drgCode,DRG.get(drgCode,DrgGroupStatus.FAIL.value),'***')
    return create_result(record.Index,self.return_messages(),drgCode)

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
  grouper=Grouper_yunnan_2022()
  record=MedicalRecord(Index=1653890, gender=2, age=10, ageDay=21, weight=3200, dept='0302',inHospitalTime=14,leavingType='1',amount=0,
    zdList='Z51.103,C15.900'.split(','), 
    ssList='99.2503'.split(','))
  s1 = time.time()
  result=grouper.group(record)
  s2 = time.time()
  print(result)
  print((s2-s1)*1000)