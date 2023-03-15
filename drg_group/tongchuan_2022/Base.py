from enum import Enum
import os
from collections import namedtuple

MedicalRecord=namedtuple('MedicalRecord','Index,gender,age,ageDay,weight,dept,inHospitalTime,leavingType,zdList,ssList')
GroupResult=namedtuple('GroupResult','Index,status,messages,mdc,adrg,drg')

MESSAGES=1
TRACE=0
groupMessages=[]
get_first_field=lambda x:x.replace('\n','').partition(' ')[0]
spliter=lambda x:(x.partition(' ')[0],x.partition(' ')[-1].replace('\n',''))
remove_last_zero=lambda x:x[:-2] if x.endswith('.0') else x

class DrgGroupStatus(Enum):
  SUCCESS='分组成功'
  FAIL='无法入组'
  QY='歧义病案'

class DrgGroupStatus(Enum):
  CHECK_FAILED='信息校验不通过'
  SUCCESS='分组成功'
  FAIL='无法入组'
  ZD_NOT_MAPPING='诊断不能转换为分组器支持的编码'
  SS_NOT_MAPPING='手术操作不能转换为分组器支持的编码'
  ZD_NOT_VALID='诊断不是有效的ICD编码'
  SS_NOT_VALID='手术操作不是有效的ICD编码'
  QY='歧义病案'
  ZD_NOT_MATCH_GENDER='主诊断与病人性别不相符'
  MAIN_ZD_NOT_MDC='主诊断不在所有MDC的主诊表内'
  # SPECS_DEFECT='分组规范存在缺陷'
  SS_ERROR='手术选择错误'
  NEWBORN_ERROR='新生儿诊断或手术错误'

class Reader:
  def __init__(self,folder):
    if not os.path.exists(os.path.join(os.path.dirname(__file__),folder)):
      raise Exception('folder not exists:'+type)
    self.path=os.path.join(os.path.dirname(__file__),folder)

  def _from(self,collection):
    self.iter=iter(collection)
    return self
  
  def read(self,name):
    self.iter=iter(open(os.path.join(self.path,name+'.dat'),encoding='utf8').readlines())
    return self

  def to_list(self,_map=get_first_field,_filter=None):
    return list(map(_map,filter(_filter,self.iter)))

  def to_set(self,_map=get_first_field,_filter=None):
    return set(map(_map,filter(_filter,self.iter)))

  def to_dict(self,_map=spliter,_filter=None):
    return dict(map(_map,filter(_filter,self.iter)))

reader=Reader('DATA')
MCC=reader.read('MCC').to_dict()
CC=reader.read('CC').to_dict()
CCE=reader.read('CCE').to_dict()
SS_VALID=reader.read('SS_VALID').to_dict()
DRG=reader.read('DRG').to_dict()
    
def tuple_to_str(t):
  result=''
  for i in t:
    if isinstance(i,str):
      if ',' in i:
        result=result+',"'+i+'"'
      else:
        result=result+','+i
    elif isinstance(i,list):
      result=result+',"'+'|'.join(i)+'"'
    else:
      result=result+','+str(i)
  return result[1:]

def output(*args):
  if TRACE:
    result=''
    for x in args:
      result+=str(x)+' '
    print(result[:-1])

def message(message):
  if MESSAGES:
    groupMessages.append(message)
  output('-->',message)

def has_mcc(main,others):
  cce=CCE.get(main)
  if cce:
    message('主诊断%s排除表%s'%(main,cce))
  for x in others:
    if x in MCC:
      mcc=MCC.get(x)
      message('诊断%s属于MCC，排除表%s'%(x,mcc))
      if cce and cce==mcc:
        continue
      else:
        return True

def has_cc(main,others):
  cce=CCE.get(main)
  if cce:
    message('主诊断%s排除表%s'%(main,cce))
  for x in others:
    if x in CC:
      cc=CC.get(x)
      message('诊断%s属于CC，排除表%s'%(x,cc))
      if cce and cce==cc:
        continue
      else:
        return True

def intersect(a,b):
  for x in a:
    for y in b:
      if x==y:
        return True
  return False

if __name__ == "__main__":
  print(len(CC))
