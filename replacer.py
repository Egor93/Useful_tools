import os
folder='DB_files/15042020'
os.chdir(folder)
fname='term_status'
old_owner='anusuriya'
current_owner='postgres'
# open file
with open(fname,'r',encoding='utf-8') as f:
    fr=f.read()
fr_replaced=fr.replace(old_owner,current_owner)
del fr
# write down file
with open(fname+'_P','w',encoding='utf-8') as f:
    f.write(fr_replaced)