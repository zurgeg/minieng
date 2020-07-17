mport os
print('MiniENG 1.0.3')
records = []
namespace = {}
towrite = ''
leave = False

def endrec():
  global towrite
  global records
  print('Quitting Recording')
  a = open('main.cart','w')
  towrite = towrite.join(records)
  a.write(towrite)
def leave():
  print('Leaving')
  print('Quitting Recordings')
  endrec()
  raise Exception('Leave')
def parse2(cmd):
  #print(cmd)
  out = None
  if cmd.lower().startswith('load '):
    print('ERR: LOAD NOT ALLOWED IN CART')
  elif cmd.lower().startswith('rec '):
    print('ERR: REC NOT ALLOWED IN CART')
  elif cmd.lower().startswith('#py:'):
    data = cmd.split(':')
    
    eval(data[1])
  elif cmd.lower().startswith('#def:'):
    data = cmd.split(':')
  if data[1].lower() == 'eval':
    a = parse(cmd)
  else:
    a = data[1]
  namespace[data[2]] = a
  return out 



print('Loading extensions')
if os.path.exists('exts'):
  print('Extensions found')
  exts = open('exts/boot.ext')
  for i in exts.readlines():
    eval(i)
else:
  print('[WARN] exts folder not found. Please create it')
print('Loading recordings')
if os.path.exists('carts'):
  print('Found recordings')
else:
  print('[FATAL] carts folder not found. Please create it')
  leave()
def run():
  while True:
    cmd = input('>')
    if cmd.lower().startswith('load '):
      for i in open('carts/' + cmd[5:]).readlines():
        parse2(i)
      print('Loaded')
    elif cmd.lower().startswith('rec '):
      print('ENTERING REC SHELL')
      print('RECORDING...')
      while True:
        cmd = input('>')
        if cmd.lower().startswith('#py:'):
          data = cmd.split(':')
          eval(data[1])
          records.append(cmd)
        elif cmd.lower().startswith('#def:'):
          data = cmd.split(':')
          if data[1].lower() == 'eval':
            a = parse2(cmd)
          else:
            a = data[1]
          namespace[data[2]] = a

        elif cmd.lower().startswith('end'):
          namespace = {}
          leave()
    elif cmd.lower() == 'exit':
      namespace = {}
      leave()
run()
      
