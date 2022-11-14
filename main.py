import json


def skip(in_str, curr_pos, count, valid):
  if curr_pos + count >= len(in_str):
    valid = False
    curr_pos = len(in_str) - 1
  else:
    curr_pos += count
  return in_str, curr_pos, valid


def delete(in_str, curr_pos, count, valid):
  if curr_pos + count > len(in_str):
    valid = False
    return in_str[0:curr_pos], curr_pos, valid
  else:
    return in_str[0:curr_pos] + in_str[curr_pos + count:], curr_pos, valid


def insert(in_str, curr_pos, to_insert):
  return in_str[0:curr_pos] + to_insert + in_str[curr_pos:], curr_pos + len(
    to_insert)


def seek(in_str, to_seek, valid):
  if to_seek >= len(in_str) or to_seek < 0:
    valid = False
  return in_str, to_seek, valid


def isValid(stale, latest, otjson):
  dec = json.JSONDecoder()
  ops = dec.decode(otjson)
  curr = 0
  valid = True
  for ot in ops:
    if ot['op'] == 'skip':
      stale, curr, valid = skip(stale,
                                curr_pos=curr,
                                count=ot['count'],
                                valid=valid)
    if ot['op'] == 'delete':
      stale, curr, valid = delete(stale,
                                  curr_pos=curr,
                                  count=ot['count'],
                                  valid=valid)
    if ot['op'] == 'insert':
      stale, curr = insert(stale, curr_pos=curr, to_insert=ot['chars'])

    if ot['op'] == 'seek':
      stale, curr, valid = seek(stale, to_seek=ot['pos'], valid=valid)

  return valid and stale == latest
