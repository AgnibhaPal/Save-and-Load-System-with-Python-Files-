f = ''
save = ''
load = ''
f = open('save', 'r')
load = f.read()
while True:
  print(str(load) + ' Was Saved in the File Previously')
  save = input('What you want to Save?: ')
  f = open('save', 'w')
  f.write(str(save))
  f.close()
  print(str(save) + ' Was Saved in the file')
  break