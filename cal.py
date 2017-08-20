do,mo,fmo,thir=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],{'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12},['January','February','March','April','May','June','July','August','September','October','November','December'],[4,6,9,11]
import time
from datetime import datetime as dm
z,time.tzname=time.localtime(),('IST','IST')
def cal(md,di,yi,*o):
 yil=yi%100
 yc=yil+yil/4
 c,co=yi/100,0
 cc,typ=7-2*(c%4),'Gregorian'
 mc=int("622503514624"[md-1])
 if yi<1752 or (yi==1752 and md<=9): cc,typ=5-c,'Julian'
 l=int(not((yi%4)or(bool(yi%100^yi%400) and yi>1753))and(md<3))
 ind=(cc+yc+mc+di-l)%7
 if o: return ind
 if md in thir: co=1
 elif md==2: co=3-l
 if di==0:
  a=[i[:3]+' ' for i in do]+[27*'-'+' '+(4*(ind+1)%28)*' ']
  for i in range(31-co):
   if yi==1752 and md==9 and i in range(2,13): continue
   a.append(' '+str(i+1).zfill(2)+' ')
  s="".join(a)
  print '%s%s, %s\n'%((11-len(fmo[md-1])/2)*' ',fmo[md-1].upper(),str(yi).zfill(4))
  for t in range(8): print ' '+s.strip()[28*t:28*t+28]
 else:
  if yi==1752 and md==9:
   if di>=14: ind,typ=ind+3,'Gregorian'
   if di in range(2,13): typ='The calendars in the US, England and many other contries switched from Julian to Gregorian in the year 1752 on 2 September. The change was suggested because the Julian calendar had too many leap years and hence did not properly reflect the actual time it takes for the Earth to circle once round the Sun. In order to get the calendar back in sync with the vernal equinox, 11 days were dropped from September 1752 (2 to 13), making it unusually short with just 19 days. The given day is what it would be if the Julian was continued.'
  st=int(str(yi).zfill(4)+str(md).zfill(2)+str(di).zfill(2))-int("".join([str(z[i]).zfill(2) for i in range(3)]))
  cur=['is','was','will be'][(st<0)+(st>0)*2]
  print '%s %s, %s %s a %s. (%s)'%(fmo[md-1],str(di),str(yi).zfill(4),cur,do[ind],typ)
  raw_input('<hit enter for more details>')
  pd,dd,cind,l=fmo[md-1]+' '+str(di),dm(yi,md,di),ind,[]
  dy=abs((dd-dm(yi,1,1)).days)
  tu=(pd, dy+1, yi, pd, (dy+cal(1,1,yi,1))/7+1, yi, pd, 365-dy-bool(yi%4)or(bool(yi%100^yi%400)), yi)
  for i in range(yi-15,yi+25):
   if cal(md,di,i,1)==cind: l.append(i)
  print '%s is Day %d of the year %d.\n%s is in Week %d of the year %d.\n%s is %d days from the end of the year %d.'%tu
  print '%s is a %s in years '%(pd,do[cind])+('%d, '*(len(l)-1))%tuple(l[:-1])+'and '+str(l[-1])+' as well.'
def _i():
 global di,md,yi
 while 1:
  yi=raw_input("Enter year: ")
  if not yi: continue
  else:
   if yi.lower()=='menu': m()
   try: yi=int(yi)
   except ValueError:
    print "\nEnter a valid year."
    continue
   if yi not in range(4000) or (yi==0 and r-1):
    print "\nEnter a year between 1 and 3999.%s"%(['','(0 for current date)'][r==1])
    continue
  break
 if yi==0:
  if r==1:
   print '\nThe current date is %s %s, %s and the time is %s:%s%s %s'%tuple([str(i) for i in [fmo[z[1]-1],z[2],z[0],(z[3]-1)%12+1,z[4],('AM','PM')[z[3]/12],time.tzname[0]]])
   return None
 while 1:
  mi=raw_input("Enter month: ")[:3].lower()
  if not mi: continue
  if r!=1 and mi=='0': continue
  else:
   if mi=='men': m()
   if not((mi in mo) or (mi.lstrip('0') in ['']+[str(i) for i in range(13)])):
    print "\nEnter a valid month. %s"%['','(0 for full year)'][r==1]
    continue
   if r==2 and m=='0': continue
  break
 try: md=int(mi)
 except ValueError: md=mo[mi]
 if md==0:
  for zi in range(12):
   print '_'*30+'\n'
   cal(zi+1,0,yi)
 else:
  while 1:
   co=int(md in thir+[2])+int(((yi%4)or(bool(yi%100^yi%400) and yi>1753))and(md==2))+int(md==2)
   di=raw_input("Enter date: ")
   if not di: continue
   else:
    if di.lower()=='menu': m()
    try: di=int(di)
    except ValueError:
     print '\nEnter a valid date.'
     continue
    if di not in range(32-co):
     print "\nEnter a date between 1 and %s. %s"%(str(31-co),['','(0 for full month)'][r==1])
     continue
   break
  print
  if r==1: cal(md,di,yi)
def age():
 print "Enter starting date or date of birth:"
 _i()
 dl1=(yi,md,di)
 print 'Do you wish to compare the date to\n1. Today (or)\n2. Another date?'
 while 1:
  p=raw_input("\nEnter input: ")
  print
  if p.lower()=='menu': m()
  if not p: continue
  else:
   try: p=int(p)
   except ValueError:
    print "Enter an integer."
    continue
  if p not in (1,2):
   print "Enter 1 or 2 as your response."
   continue
  break
 if p-1:
  _i()
  dl2=(yi,md,di)
 else: dl2=z[:3]
 a=abs((dm(*dl1)-dm(*dl2)).days)
 if a==0: print "Both dates coincide."
 else:
  t1,g=tuple(str(i) for i in [fmo[dl1[1]-1],dl1[2],dl1[0],fmo[dl2[1]-1],dl2[2],dl2[0]]),4+bool(a/7)+bool(a/30)+bool(a/365)
  t2=tuple([str(a*86400)+' second',str(a*1440)+' minute',str(a*24)+' hour',str(a)+' day',str(a/7)+' week'+('s and %d day'%(a%7))*bool(a%7),str(a/30)+' month'+('s and %d day'%(a%30))*bool(a%30),str(a/365)+' common years and %d day'%(a%365)])
  if a<1809 or p-1: print "There are %d days between %s %s, %s and %s %s, %s."%((a,)+t1)
  else: print "You are %d days old."%a
  raw_input('<hit enter for more details>')
  if a<1809 or p-1:
   for i in range(g): print "Or %ss."%(t2[i])
  else:
   for i in range(g): print "You are %ss old."%(t2[i])
   print "Your age is %s years."%str(a/365.25)[:5]
def m(*x):
 global r
 print "\nSelect tool:\n1. Calendar and other details of a date\n2. Difference between two dates (and age calculator)\n3. Exit\n(Enter menu at any input prompt to return here)\n"
 while 1:
  r=raw_input("Enter input: ")
  if not r: continue
  else:
   print
   try: r=int(r)
   except ValueError:
    print "Enter an integer."
    continue
  if r not in (1,2,3):
   print "Enter 1, 2 or 3 as your response."
   continue
  break
 if r==3: quit()
 if r-1: age()
 else: _i()
while 1: m(raw_input('-'*22+"\n<hit enter to proceed>"))
