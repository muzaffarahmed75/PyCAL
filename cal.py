do,mo,fmo,thir=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],{'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12},['January','February','March','April','May','June','July','August','September','October','November','December'],[4,6,9,11]
#do=list of days, mo=dict of months, fmo=full name of months, thir=motnhs having 30 days
import time
from datetime import datetime as dm
z,time.tzname=time.localtime(),('IST','IST') #timezone
def cal(md,di,yi,*o): #the calendar function, md is month_digit, di is date_input, yi is year_input, *o is an argument which if passed will cause the function to return the day's value
 yil=yi%100 #used for calculation of day
 yc=yil+yil/4 #used for calc
 c,co=yi/100,0 #c is century, co is correction
 cc,typ=7-2*(c%4),'Gregorian' #cc is 400-leap-year correction
 mc=int("622503514624"[md-1]) #mc is month code, used for date calculation
 if yi<1752 or (yi==1752 and md<=9): cc,typ=5-c,'Julian' #before 2 September 1752, the Julian Calendar was followed
 l=int(not((yi%4)or(bool(yi%100^yi%400) and yi>1753))and(md<3)) #l is the leap variable
 ind=(cc+yc+mc+di-l)%7 #ind is integer_day, gives the integer corresponding to the day
 if o: return ind #if variable o is passed, ind is returned, nothing is printed
 if md in thir: co=1 #if month is of 30 days, correction is 1
 elif md==2: co=3-l #if month is february, correction is 3-leap
 if di==0: #if input date is 0:
  a=[i[:3]+' ' for i in do]+[27*'-'+' '+(4*(ind+1)%28)*' '] #stores Sun Mon Tue... and ------ to a with proper spacing
  for i in range(31-co): #31-co is number of dates in that motnh
   if yi==1752 and md==9 and i in range(2,13): continue #drops the days 3-13 from September 1752
   a.append(' '+str(i+1).zfill(2)+' ') #if not that special case, each date is appended to a with proper spacing
  s="".join(a) #a is joined into a string and stored to s
  print '%s%s, %s\n'%((11-len(fmo[md-1])/2)*' ',fmo[md-1].upper(),str(yi).zfill(4)) #the month, year is printed with proper spacing
  for t in range(8): print ' '+s.strip()[28*t:28*t+28] #prints the month calendar starting from Sun Mon Tue...
 else: #if input date is not 0
  if yi==1752 and md==9: #september 1752
   if di>=14: ind,typ=ind+3,'Gregorian' #From 14th, Gregorian was adopted. 11 days dropped so the Day must shift increase by 3.
   if di in range(2,14): typ='The calendars in the US, England and many other contries switched from Julian to Gregorian in the year 1752 on 2 September. The change was suggested because the Julian calendar had too many leap years and hence did not properly reflect the actual time it takes for the Earth to circle once round the Sun. In order to get the calendar back in sync with the vernal equinox, 11 days were dropped from September 1752 (2 to 13), making it unusually short with just 19 days. The given day is what it would be if the Julian was continued.'
  st=int(str(yi).zfill(4)+str(md).zfill(2)+str(di).zfill(2))-int("".join([str(z[i]).zfill(2) for i in range(3)])) #st=Sign_wrt_Today, calculates if given date is the past, present or future
  #st is negative if past, zero if today, and positive if future
  cur=['is','was','will be'][(st<0)+(st>0)*2] #is/was/will be will be chosen according to whether the date is in the past, present or future
  print '%s %s, %s %s a %s. (%s)'%(fmo[md-1],str(di),str(yi).zfill(4),cur,do[ind],typ) #prints the day of the given date
  raw_input('<hit enter for more details>')
  pd,dd,cind,l=fmo[md-1]+' '+str(di),dm(yi,md,di),ind,[] #pd is printable date, dd is date in datetime type, duplicating ind to cind to avoid any conflict and l is an empty list
  dy=abs((dd-dm(yi,1,1)).days) #dy=day of the year-1
  tu=(pd, dy+1, yi, pd, (dy+cal(1,1,yi,1))/7+1, yi, pd, 365-dy-bool(yi%4)or(bool(yi%100^yi%400)), yi)
  #tu is a tuple containing printable date, day of the year, input year, week of the year, input year, printable date, days from the end of the year, year input
  for i in range(yi-15,yi+25): #for years from 15 years ago to 25 years in future
   if cal(md,di,i,1)==cind: l.append(i) #if the dates in that year and input year are same, that year is appended to l
  print '%s is Day %d of the year %d.\n%s is in Week %d of the year %d.\n%s is %d days from the end of the year %d.'%tu #prints details of a date
  print '%s is a %s in years '%(pd,do[cind])+('%d, '*(len(l)-1))%tuple(l[:-1])+'and '+str(l[-1])+' as well.' #prints same-day-different-year years
def _i(): #input function
 global di,md,yi #finally we will need these three variables from this function
 while 1: #inputting year with error handling
  yi=raw_input("Enter year: ")
  if not yi: continue
  else:
   if yi.lower()=='menu': m() #at any input, if menu is entered, user can access the main menu
   try: yi=int(yi)
   except ValueError:
    print "\nEnter a valid year."
    continue
   if yi not in range(4000) or (yi==0 and r-1):
    print "\nEnter a year between 1 and 3999.%s"%(['','(0 for current date)'][r==1])
    continue
  break
 if yi==0:
  if r==1: #r is the response variable, refer the function m() at the bottom
   print '\nThe current date is %s %s, %s and the time is %s:%s%s %s'%tuple([str(i) for i in [fmo[z[1]-1],z[2],z[0],(z[3]-1)%12+1,z[4],('AM','PM')[z[3]/12],time.tzname[0]]])
   #if input year is 0, the current date and time are printed
   return None
 while 1: #inputting the month with error handling
  mi=raw_input("Enter month: ")[:3].lower() #month is input and only first 3 characters are taken into consideration
  if not mi: continue
  if r!=1 and mi=='0': continue #0 as month is accepted only for calendar, not age calculator
  else:
   if mi=='men': m() #menu sliced to men
   if not((mi in mo) or (mi.lstrip('0') in ['']+[str(i) for i in range(13)])): #if mi is not in the months dict nor is an integer 0<x<13
    print "\nEnter a valid month. %s"%['','(0 for full year)'][r==1] #r==1 is the boolean value
    continue
   if r==2 and m=='0': continue
  break
 try: md=int(mi) #check if md is an integer
 except ValueError: md=mo[mi] #if not, it is surely a month name
 if md==0: #if 0 is input for month
  for zi in range(12): 
   print '_'*30+'\n'
   cal(zi+1,0,yi) #cal is a print function, 12 months are printed
 else: #if year input is not 0
  while 1:
   co=int(md in thir+[2])+int(((yi%4)or(bool(yi%100^yi%400) and yi>1753))and(md==2))+int(md==2) #correction variable
   di=raw_input("Enter date: ") #date input with error handling
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
  if r==1: cal(md,di,yi) #if selected tool is calendar, cal() is called, else the variables di,md,yi will be used for age calculation
def age(): #age calculator and difference in two dates function
 print "Enter starting date or date of birth:"
 _i() #input is called to get di,md,yi
 dl1=(yi,md,di) #they are stored in a tuple dl1(datelist1)
 print 'Do you wish to compare the date to\n1. Today (or)\n2. Another date?'
 while 1: #input of response with error handling
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
 if p-1: #p==2
  _i() #input function is called again, to get another date
  dl2=(yi,md,di) #the second date is stored in dl2
 else: dl2=z[:3] #else if p==1, dl2 is today's date
 a=abs((dm(*dl1)-dm(*dl2)).days) #a is the absolute difference between the two dates, dm is the datetime.datetime() function
 if a==0: print "Both dates coincide."
 else:
  t1,g=tuple(str(i) for i in [fmo[dl1[1]-1],dl1[2],dl1[0],fmo[dl2[1]-1],dl2[2],dl2[0]]),4+bool(a/7)+bool(a/30)+bool(a/365) #easier to understand if program is run
  t2=tuple([str(a*86400)+' second',str(a*1440)+' minute',str(a*24)+' hour',str(a)+' day',str(a/7)+' week'+('s and %d day'%(a%7))*bool(a%7),str(a/30)+' month'+('s and %d day'%(a%30))*bool(a%30),str(a/365)+' common years and %d day'%(a%365)])
  if a<1809 or p-1: print "There are %d days between %s %s, %s and %s %s, %s."%((a,)+t1) #1809 is a random number a chose, just to distinguish between 5 years old above or below
  else: print "You are %d days old."%a
  raw_input('<hit enter for more details>')
  if a<1809 or p-1:
   for i in range(g): print "Or %ss."%(t2[i])
  else:
   for i in range(g): print "You are %ss old."%(t2[i])
   print "Your age is %s years."%str(a/365.25)[:5]
def m(*x): #menu function, *x is there to save a couple of lines(check last line)
 global r #response variable
 print "\nSelect tool:\n1. Calendar and other details of a date\n2. Difference between two dates (and age calculator)\n3. Exit\n(Enter menu at any input prompt to return here)\n"
 while 1: #input of response with error handling
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
 if r-1: age() #r==2
 else: _i() #r==1
while 1: m(raw_input('-'*22+"\n<hit enter to proceed>"))
