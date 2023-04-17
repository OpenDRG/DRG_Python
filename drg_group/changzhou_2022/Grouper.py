from drg_group.changzhou_2022.Base import message
from drg_group.changzhou_2022.MDC import MDCA,MDCB,MDCC,MDCD,MDCE,MDCF,MDCG,MDCH,MDCI,MDCJ,MDCK,MDCL,MDCM,MDCN,MDCO,MDCP,MDCQ,MDCR,MDCS,MDCT,MDCU,MDCV,MDCW,MDCX,MDCY,MDCZ

def group(record):

  result=MDCA.group(record)
  if result:
    return result

  result=MDCP.group(record)
  if result:
    return result

  result=MDCY.group(record)
  if result:
    return result

  result=MDCZ.group(record)
  if result:
    return result

  result=MDCM.group(record)
  if result:
    return result

  result=MDCN.group(record)
  if result:
    return result

  result=MDCB.group(record)
  if result:
    return result

  result=MDCC.group(record)
  if result:
    return result

  result=MDCD.group(record)
  if result:
    return result

  result=MDCE.group(record)
  if result:
    return result

  result=MDCF.group(record)
  if result:
    return result

  result=MDCG.group(record)
  if result:
    return result

  result=MDCH.group(record)
  if result:
    return result

  result=MDCI.group(record)
  if result:
    return result

  result=MDCJ.group(record)
  if result:
    return result

  result=MDCK.group(record)
  if result:
    return result

  result=MDCL.group(record)
  if result:
    return result

  result=MDCO.group(record)
  if result:
    return result

  result=MDCQ.group(record)
  if result:
    return result

  result=MDCR.group(record)
  if result:
    return result

  result=MDCS.group(record)
  if result:
    return result

  result=MDCT.group(record)
  if result:
    return result

  result=MDCU.group(record)
  if result:
    return result

  result=MDCV.group(record)
  if result:
    return result

  result=MDCW.group(record)
  if result:
    return result

  result=MDCX.group(record)
  if result:
    return result

  message('不符合所有MDC的入组条件，无法入组')
  return '0000'