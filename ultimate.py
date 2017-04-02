from nltk import word_tokenize
from bs4 import BeautifulSoup
import mechanize
import re
import nltk
import MySQLdb
count=0
count2=0
countp=0
countf=0
coname="hello"
def main():
	global count2
	global count
	global coname
	global countf
	print "\t\tMGU Result Analytics Database Updater"
	print "\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	i=input("Enter the First roll no  				   : ")
	x=input("Enter the last roll no   				   : ")
	n=x-i
	c=input("Enter the college name in(double quotes)  : ")
	course=input("Enter the course in(double quotes)   : ")
	s=input("Enter the semester(1,2,3,4)               : ")
	while s>4 or s<=0:
	  s=input("Enter the correct semester(1,2,3,4)       : ")
	if s==1:
		semester1(c,i,x)
	elif s==2:
		semester2(c,i,x)
	elif s==3:
		semester3(c,i,x)
	elif s==4:
		semester4(c,i,x)   
	t=n-count
	n=t-count2
	countp=n-countf
	print "Number of students appeared for the exam : %d"%n
	print "Number of unregistered PRN's : %d"%count
	print "Number of Invalid PRN's : %d"%count2
	print "Number of students passed : %d"%countp
	print "Number of students failed : %d"%countf
	ppercent=(float(countp)/float(n))*100
	dbupdater2(countp,coname,n,s,ppercent)
	dbupdater3(c,coname)  

def semester4(college,first,last):
	while(first<=last):
		sem4(first)
		first=first+1
		
def sem4(i):
    flag=0
    cflag=0
    global count
    global count2
    global countp
    global countf
    global coname
    browser = mechanize.Browser(factory=mechanize.RobustFactory())  #browser part starts
    browser.set_handle_robots(False)
    browser.open("http://14.139.185.88/cbcsshrCamp/index.php?module=public&page=result") 
    browser.select_form(nr=0)
    control=browser.find_control('exam_id')
    print control
    control.value=['205']#select semester value
    browser.form["prn"]=str(i)
    browser.submit() #browser part ends
    html = browser.response().readlines()
    for j in range(0,len(html)):
      if 'Not Registered' in html[j]: 
        flag=1
        count=count+1
      elif 'Invalid PRN !!' in html[j]:
        flag=1
        count2=count2+1
   #counting for failed candidates
    for j in range(0,len(html)):
      if 'Failed' in html[j]: 
        cflag=1
        break
    if cflag==1:
      countf=countf+1 
    if flag==1:
      print "Not registered %d"%count
    else:
      html = str(browser.response().readlines())
      raw = BeautifulSoup(html).get_text()
      raw=raw.replace("\\r\\n"," ")
      raw=raw.replace("\\t"," ")
      raw=raw.replace("\'"," ")
      raw=raw.replace(","," ")
      p=raw.find("Exam Centre")
      q=raw.rfind("P.O")
      a=raw.find("Permanent")
      b=raw.rfind("P.O")
      raw1=raw[a:b]
      x=raw.find("Course Code")
      y=raw.rfind("intended")
      raw2=raw[x:y]
      raw1=raw1.encode('ascii','ignore')
      raw2=raw2.encode('ascii','ignore')
      raw3=raw[p:q]
      raw3=raw3.encode('ascii','ignore')
      raw3=raw3.replace("m "," ")
      tokens3=word_tokenize(raw3)
      tokens1 = word_tokenize(raw1)
      tokens2=word_tokenize(raw2)
      tokens2=filter(lambda a: a != "-", tokens2)
      text1 = nltk.Text(tokens1)
      text2 = nltk.Text(tokens2)
      regno=tokens1[4]
      name1=' '.join(tokens1[9:11])
      coname='_'.join(tokens3[2:6])
      coname=coname.replace(":","")
      print coname
      code1=tokens2[16]
      code2=tokens2[32]
      code3=tokens2[47]
      code4=tokens2[62]
      code5=tokens2[76]
      code6=tokens2[92]
      subject1=' '.join(tokens2[17:21])
      subject2=' '.join(tokens2[33:36])
      subject3=' '.join(tokens2[48:51])
      subject4=' '.join(tokens2[63:65])
      subject5=' '.join(tokens2[77:81])
      subject6=' '.join(tokens2[93:96])
      credit1=tokens2[21]
      credit2=tokens2[36]
      credit3=tokens2[51]
      credit4=tokens2[65]
      credit5=tokens2[81]
      credit6=tokens2[96]
      credittot=tokens2[109]
      esa1=tokens2[22]
      esa2=tokens2[37]
      esa3=tokens2[52]
      esa4=tokens2[66]
      esa5=tokens2[82]
      esa6=tokens2[97]
      emax=80
      isa1=tokens2[24]
      isa2=tokens2[39]
      isa3=tokens2[54]
      isa4=tokens2[68]
      isa5=tokens2[84]
      isa6=tokens2[99]
      imax=20
      t1=tokens2[26]
      t2=tokens2[41]
      t3=tokens2[56]
      t4=tokens2[70]
      t5=tokens2[86]
      t6=tokens2[101]
      tmax=100
      gtmax=600
      grade1=tokens2[28]
      grade2=tokens2[43]  
      grade3=tokens2[58]
      grade4=tokens2[72]
      grade5=tokens2[88]
      grade6=tokens2[103]
      tgrade=tokens2[115]
      gp1=tokens2[29]
      gp2=tokens2[44]
      gp3=tokens2[59]
      gp4=tokens2[73]
      gp5=tokens2[89]
      gp6=tokens2[104]
      cp1=tokens2[30]
      cp2=tokens2[45]
      cp3=tokens2[60]
      cp4=tokens2[74]
      cp5=tokens2[90]
      cp6=tokens2[105]
      tcp=tokens2[116]
      r1=tokens2[31]
      r2=tokens2[46]
      r3=tokens2[61]
      r4=tokens2[75]
      r5=tokens2[91]
      r6=tokens2[106]
      tr=tokens2[117]
      tot_marks=tokens2[113]
      scpa=tokens2[112]
      semester=4
      dbupdater(coname,semester,regno,name1,code1,subject1,esa1,isa1,t1,grade1,gp1,cp1,r1,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code2,subject2,esa2,isa2,t2,grade2,gp2,cp2,r2,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code3,subject3,esa3,isa3,t3,grade3,gp3,cp3,r3,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code4,subject4,esa4,isa4,t4,grade4,gp4,cp4,r4,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code5,subject5,esa5,isa5,t5,grade5,gp5,cp5,r5,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code6,subject6,esa6,isa6,t6,grade6,gp6,cp6,r6,scpa,tot_marks,tgrade,tcp,tr)
      print name1+':'+regno+'\r\n\r\n'+code1+'   '+subject1+'   '+credit1+'   '+esa1+'   '+str(emax)+'   '+isa1+'   '+str(imax)+'   '+t1+'   '+str(tmax)+'   '+grade1+'   '+gp1+'   '+cp1+'   '+r1
      print '\r\n'+code2+'   '+subject2+'   '+credit2+'   '+esa2+'   '+str(emax)+'   '+isa2+'   '+str(imax)+'   '+t2+'   '+str(tmax)+'   '+grade2+'   '+gp2+'   '+cp2+'   '+r2
      print '\r\n'+code3+'   '+subject3+'   '+credit3+'   '+esa3+'   '+str(emax)+'   '+isa3+'   '+str(imax)+'   '+t3+'   '+str(tmax)+'   '+grade3+'   '+gp3+'   '+cp3+'   '+r3
      print '\r\n'+code4+'   '+subject4+'   '+credit4+'   '+esa4+'   '+str(emax)+'   '+isa4+'   '+str(imax)+'   '+t4+'   '+str(tmax)+'   '+grade4+'   '+gp4+'   '+cp4+'   '+r4
      print '\r\n'+code5+'   '+subject5+'   '+credit5+'   '+esa5+'   '+str(emax)+'   '+isa5+'   '+str(imax)+'   '+t5+'   '+str(tmax)+'   '+grade5+'   '+gp5+'   '+cp5+'   '+r5
      print '\r\n'+code6+'   '+subject6+'   '+credit6+'   '+esa6+'   '+str(emax)+'   '+isa6+'   '+str(imax)+'   '+t6+'   '+str(tmax)+'   '+grade6+'   '+gp6+'   '+cp6+'   '+r6
      print '\r\n'+'Total Credit : '+credittot+'\r\nSCPA : '+scpa+'\r\nTotal Marks : '+tot_marks+'/600'
      print '\r\n'+'Overall Grade : '+tgrade+'\r\nTotal CP : '+tcp+'\r\nOverall Status : '+tr


def semester3(college,first,last):
	while(first<=last):
		sem3(first)
		first=first+1

def sem3(i):
  flag=0
  cflag=0
  global count
  global count2
  global countp
  global countf
  global coname
  browser = mechanize.Browser(factory=mechanize.RobustFactory())
  browser.set_handle_robots(False)
  browser.open("http://14.139.185.88/cbcsshrCamp/index.php?module=public&page=result") 
  browser.select_form(nr=0)
  control=browser.find_control('exam_id')
  print control
  control.value=['203']
  browser.form["prn"]=str(i)
  browser.submit()
  html = browser.response().readlines()
  for j in range(0,len(html)):
   if 'Not Registered' in html[j]: 
    flag=1
    count=count+1
   elif 'Invalid PRN !!' in html[j]:
     flag=1
     count2=count2+1
   #counting for failed candidates
  for j in range(0,len(html)):
   if 'Failed' in html[j]: 
    cflag=1
    break
  if cflag==1:
    countf=countf+1 
  if flag==1:
    print "Not registered %d"%count
  else:
    html=str(browser.response().readlines())
    raw = BeautifulSoup(html,"lxml").get_text()
    raw=raw.replace("\\r\\n"," ")
    raw=raw.replace("\\t"," ")
    raw=raw.replace("\'"," ")
    raw=raw.replace(","," ")
    a=raw.find("Permanent")
    b=raw.rfind("P.O")
    raw1=raw[a:b]
    x=raw.find("Course Code")
    y=raw.rfind("intended")
    raw2=raw[x:y]
    p=raw.find("Exam Centre")
    q=raw.rfind("P.O")
    raw3=raw[p:q]
    raw3=raw3.encode('ascii','ignore')
    raw1=raw1.encode('ascii','ignore')
    raw2=raw2.encode('ascii','ignore')
    raw3=raw3.replace("m "," ")
    tokens1 = word_tokenize(raw1)
    tokens2=word_tokenize(raw2)
    tokens3=word_tokenize(raw3)
    tokens2=filter(lambda a: a != "-", tokens2) 
    text1 = nltk.Text(tokens1)
    text2 = nltk.Text(tokens2)
    regno=tokens1[4]
    name1=' '.join(tokens1[9:11])
    coname='_'.join(tokens3[2:6])
    coname=coname.replace(":","")
    code1=tokens2[16]
    code2=tokens2[33]
    code3=tokens2[49]
    code4=tokens2[63]
    code5=tokens2[80]
    code6=tokens2[94]
    subject1=' '.join(tokens2[17:22])
    subject2=' '.join(tokens2[34:38])
    subject3=' '.join(tokens2[50:52])
    subject4=' '.join(tokens2[64:69])
    subject5=' '.join(tokens2[81:83])
    subject6=' '.join(tokens2[95:99])
    credit1=tokens2[22]
    credit2=tokens2[38]
    credit3=tokens2[52]
    credit4=tokens2[69]
    credit5=tokens2[83]
    credit6=tokens2[100]
    credittot=tokens2[113]
    esa1=tokens2[23]
    esa2=tokens2[39]
    esa3=tokens2[53]
    esa4=tokens2[70]
    esa5=tokens2[84]
    esa6=tokens2[100]
    emax=80
    isa1=tokens2[25]
    isa2=tokens2[41]
    isa3=tokens2[55]
    isa4=tokens2[72]
    isa5=tokens2[86]
    isa6=tokens2[102]
    imax=20
    t1=tokens2[27]
    t2=tokens2[43]
    t3=tokens2[57]
    t4=tokens2[74]
    t5=tokens2[88]
    t6=tokens2[104]
    tmax=100
    gtmax=600
    grade1=tokens2[29]
    grade2=tokens2[45]
    grade3=tokens2[59]
    grade4=tokens2[76]
    grade5=tokens2[90]
    grade6=tokens2[106]
    tgrade=tokens2[118]
    gp1=tokens2[30]
    gp2=tokens2[46]
    gp3=tokens2[60]
    gp4=tokens2[77]
    gp5=tokens2[91]
    gp6=tokens2[107]
    cp1=tokens2[31]
    cp2=tokens2[47]
    cp3=tokens2[61]
    cp4=tokens2[78]
    cp5=tokens2[92]
    cp6=tokens2[108]
    tcp=tokens2[119]
    r1=tokens2[32]
    r2=tokens2[48]
    r3=tokens2[62]
    r4=tokens2[79]
    r5=tokens2[93]
    r6=tokens2[109]
    tr=tokens2[120]
    tot_marks=tokens2[116]
    scpa=tokens2[115]
    semester=3
    dbupdater(coname,semester,regno,name1,code1,subject1,esa1,isa1,t1,grade1,gp1,cp1,r1,scpa,tot_marks,tgrade,tcp,tr)
    dbupdater(coname,semester,regno,name1,code2,subject2,esa2,isa2,t2,grade2,gp2,cp2,r2,scpa,tot_marks,tgrade,tcp,tr)
    dbupdater(coname,semester,regno,name1,code3,subject3,esa3,isa3,t3,grade3,gp3,cp3,r3,scpa,tot_marks,tgrade,tcp,tr)
    dbupdater(coname,semester,regno,name1,code4,subject4,esa4,isa4,t4,grade4,gp4,cp4,r4,scpa,tot_marks,tgrade,tcp,tr)
    dbupdater(coname,semester,regno,name1,code5,subject5,esa5,isa5,t5,grade5,gp5,cp5,r5,scpa,tot_marks,tgrade,tcp,tr)
    dbupdater(coname,semester,regno,name1,code6,subject6,esa6,isa6,t6,grade6,gp6,cp6,r6,scpa,tot_marks,tgrade,tcp,tr)
    print name1+':'+regno+'\r\n\r\n'+code1+'   '+subject1+'   '+credit1+'   '+esa1+'   '+str(emax)+'   '+isa1+'   '+str(imax)+'   '+t1+'   '+str(tmax)+'   '+grade1+'   '+gp1+'   '+cp1+'   '+r1
    print '\r\n'+code2+'   '+subject2+'   '+credit2+'   '+esa2+'   '+str(emax)+'   '+isa2+'   '+str(imax)+'   '+t2+'   '+str(tmax)+'   '+grade2+'   '+gp2+'   '+cp2+'   '+r2
    print '\r\n'+code3+'   '+subject3+'   '+credit3+'   '+esa3+'   '+str(emax)+'   '+isa3+'   '+str(imax)+'   '+t3+'   '+str(tmax)+'   '+grade3+'   '+gp3+'   '+cp3+'   '+r3
    print '\r\n'+code4+'   '+subject4+'   '+credit4+'   '+esa4+'   '+str(emax)+'   '+isa4+'   '+str(imax)+'   '+t4+'   '+str(tmax)+'   '+grade4+'   '+gp4+'   '+cp4+'   '+r4
    print '\r\n'+code5+'   '+subject5+'   '+credit5+'   '+esa5+'   '+str(emax)+'   '+isa5+'   '+str(imax)+'   '+t5+'   '+str(tmax)+'   '+grade5+'   '+gp5+'   '+cp5+'   '+r5
    print '\r\n'+code6+'   '+subject6+'   '+credit6+'   '+esa6+'   '+str(emax)+'   '+isa6+'   '+str(imax)+'   '+t6+'   '+str(tmax)+'   '+grade6+'   '+gp6+'   '+cp6+'   '+r6
    print '\r\n'+'Total Credit : '+credittot+'\r\nSCPA : '+scpa+'\r\nTotal Marks : '+tot_marks+'/600'
    print '\r\n'+'Overall Grade : '+tgrade+'\r\nTotal CP : '+tcp+'\r\nOverall Status : '+tr




def semester2(college,first,last):
	while(first<=last):
		sem2(first)
		first=first+1
 
def sem2(i):
    flag=0
    cflag=0
    global coname
    global count
    global count2
    global countp
    global countf
    browser = mechanize.Browser(factory=mechanize.RobustFactory())  #browser part starts
    browser.set_handle_robots(False)
    browser.open("http://14.139.185.88/cbcsshrCamp/index.php?module=public&page=result") 
    browser.select_form(nr=0)
    control=browser.find_control('exam_id')
    print control
    control.value=['202']#select semester value
    browser.form["prn"]=str(i)
    browser.submit() #browser part ends
    html = browser.response().readlines()
    for j in range(0,len(html)):
      if 'Not Registered' in html[j]: 
        flag=1
        count=count+1
      elif 'Invalid PRN !!' in html[j]:
        flag=1
        count2=count2+1
   #counting for failed candidates
    for j in range(0,len(html)):
      if 'Failed' in html[j]: 
        cflag=1
        break
    if cflag==1:
      countf=countf+1 
    if flag==1:
      print "Not registered %d"%count
    else:
      html = str(browser.response().readlines())
      raw = BeautifulSoup(html).get_text()
      raw=raw.replace("\\r\\n"," ")
      raw=raw.replace("\\t"," ")
      raw=raw.replace("\'"," ")
      raw=raw.replace(","," ")
      p=raw.find("Exam Centre")
      q=raw.rfind("P.O")
      a=raw.find("Permanent")
      b=raw.rfind("P.O")
      raw1=raw[a:b]
      x=raw.find("Course Code")
      y=raw.rfind("intended")
      raw2=raw[x:y]
      raw1=raw1.encode('ascii','ignore')
      raw2=raw2.encode('ascii','ignore')
      raw3=raw[p:q]
      raw3=raw3.encode('ascii','ignore')
      raw3=raw3.replace("m "," ")
      tokens3=word_tokenize(raw3)
      tokens1 = word_tokenize(raw1)
      tokens2=word_tokenize(raw2)
      tokens2=filter(lambda a: a != "-", tokens2)
      text1 = nltk.Text(tokens1)
      text2 = nltk.Text(tokens2)
      regno=tokens1[4]
      name1=' '.join(tokens1[9:11])
      coname='_'.join(tokens3[2:6])
      coname=coname.replace(":","")
      print coname
      code1=tokens2[16]
      code2=tokens2[35]
      code3=tokens2[52]
      code4=tokens2[66]
      code5=tokens2[82]
      code6=tokens2[97]
      subject1=' '.join(tokens2[17:24])
      subject2=' '.join(tokens2[36:41])
      subject3=' '.join(tokens2[53:55])
      subject4=' '.join(tokens2[67:71])
      subject5=' '.join(tokens2[83:86])
      subject6=' '.join(tokens2[98:101])
      credit1=tokens2[24]
      credit2=tokens2[41]
      credit3=tokens2[55]
      credit4=tokens2[71]
      credit5=tokens2[86]
      credit6=tokens2[101]
      credittot=tokens2[114]
      esa1=tokens2[25]
      esa2=tokens2[42]
      esa3=tokens2[56]
      esa4=tokens2[72]
      esa5=tokens2[87]
      esa6=tokens2[102]
      emax=80
      isa1=tokens2[27]
      isa2=tokens2[44]
      isa3=tokens2[58]
      isa4=tokens2[74]
      isa5=tokens2[89]
      isa6=tokens2[104]
      imax=20
      t1=tokens2[29]
      t2=tokens2[46]
      t3=tokens2[60]
      t4=tokens2[76]
      t5=tokens2[91]
      t6=tokens2[106]
      tmax=100
      gtmax=600
      grade1=tokens2[31]
      grade2=tokens2[48]
      grade3=tokens2[62]
      grade4=tokens2[78]
      grade5=tokens2[93]
      grade6=tokens2[108]
      tgrade=tokens2[120]
      gp1=tokens2[32]
      gp2=tokens2[49]
      gp3=tokens2[63]
      gp4=tokens2[79]
      gp5=tokens2[94]
      gp6=tokens2[109]
      cp1=tokens2[33]
      cp2=tokens2[50]
      cp3=tokens2[64]
      cp4=tokens2[80]
      cp5=tokens2[95]
      cp6=tokens2[110]
      tcp=tokens2[121]
      r1=tokens2[34]
      r2=tokens2[51]
      r3=tokens2[65]
      r4=tokens2[81]
      r5=tokens2[96]
      r6=tokens2[111]
      tr=tokens2[122]
      tot_marks=tokens2[118]
      scpa=tokens2[117]
      semester=2
      dbupdater(coname,semester,regno,name1,code1,subject1,esa1,isa1,t1,grade1,gp1,cp1,r1,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code2,subject2,esa2,isa2,t2,grade2,gp2,cp2,r2,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code3,subject3,esa3,isa3,t3,grade3,gp3,cp3,r3,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code4,subject4,esa4,isa4,t4,grade4,gp4,cp4,r4,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code5,subject5,esa5,isa5,t5,grade5,gp5,cp5,r5,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code6,subject6,esa6,isa6,t6,grade6,gp6,cp6,r6,scpa,tot_marks,tgrade,tcp,tr)
      print name1+':'+regno+'\r\n\r\n'+code1+'   '+subject1+'   '+credit1+'   '+esa1+'   '+str(emax)+'   '+isa1+'   '+str(imax)+'   '+t1+'   '+str(tmax)+'   '+grade1+'   '+gp1+'   '+cp1+'   '+r1
      print '\r\n'+code2+'   '+subject2+'   '+credit2+'   '+esa2+'   '+str(emax)+'   '+isa2+'   '+str(imax)+'   '+t2+'   '+str(tmax)+'   '+grade2+'   '+gp2+'   '+cp2+'   '+r2
      print '\r\n'+code3+'   '+subject3+'   '+credit3+'   '+esa3+'   '+str(emax)+'   '+isa3+'   '+str(imax)+'   '+t3+'   '+str(tmax)+'   '+grade3+'   '+gp3+'   '+cp3+'   '+r3
      print '\r\n'+code4+'   '+subject4+'   '+credit4+'   '+esa4+'   '+str(emax)+'   '+isa4+'   '+str(imax)+'   '+t4+'   '+str(tmax)+'   '+grade4+'   '+gp4+'   '+cp4+'   '+r4
      print '\r\n'+code5+'   '+subject5+'   '+credit5+'   '+esa5+'   '+str(emax)+'   '+isa5+'   '+str(imax)+'   '+t5+'   '+str(tmax)+'   '+grade5+'   '+gp5+'   '+cp5+'   '+r5
      print '\r\n'+code6+'   '+subject6+'   '+credit6+'   '+esa6+'   '+str(emax)+'   '+isa6+'   '+str(imax)+'   '+t6+'   '+str(tmax)+'   '+grade6+'   '+gp6+'   '+cp6+'   '+r6
      print '\r\n'+'Total Credit : '+credittot+'\r\nSCPA : '+scpa+'\r\nTotal Marks : '+tot_marks+'/600'
      print '\r\n'+'Overall Grade : '+tgrade+'\r\nTotal CP : '+tcp+'\r\nOverall Status : '+tr
	
      
def semester1(college,first,last):
	while(first<=last):
		sem1(first)
		first=first+1

def sem1(i):
    flag=0
    cflag=0
    global count
    global count2
    global countp
    global countf
    global coname
    browser = mechanize.Browser(factory=mechanize.RobustFactory())  #browser part starts
    browser.set_handle_robots(False)
    browser.open("http://14.139.185.88/cbcsshrCamp/index.php?module=public&page=result") 
    browser.select_form(nr=0)
    control=browser.find_control('exam_id')
    print control
    control.value=['201']#select semester value
    browser.form["prn"]=str(i)
    browser.submit() #browser part ends
    html = browser.response().readlines()
    for j in range(0,len(html)):
      if 'Not Registered' in html[j]: 
        flag=1
        count=count+1
      elif 'Invalid PRN !!' in html[j]:
        flag=1
        count2=count2+1
   #counting for failed candidates
    for j in range(0,len(html)):
      if 'Failed' in html[j]: 
        cflag=1
        break
    if cflag==1:
      countf=countf+1 
    if flag==1:
      print "Not registered %d"%count
    else:
      html = str(browser.response().readlines())
      raw = BeautifulSoup(html).get_text()
      raw=raw.replace("\\r\\n"," ")
      raw=raw.replace("\\t"," ")
      raw=raw.replace("\'"," ")
      raw=raw.replace(","," ")
      p=raw.find("Exam Centre")
      q=raw.rfind("P.O")
      a=raw.find("Permanent")
      b=raw.rfind("P.O")
      raw1=raw[a:b]
      x=raw.find("Course Code")
      y=raw.rfind("intended")
      raw2=raw[x:y]
      raw1=raw1.encode('ascii','ignore')
      raw2=raw2.encode('ascii','ignore')
      raw3=raw[p:q]
      raw3=raw3.encode('ascii','ignore')
      raw3=raw3.replace("m "," ")
      tokens3=word_tokenize(raw3)
      tokens1 = word_tokenize(raw1)
      tokens2=word_tokenize(raw2)
      tokens2=filter(lambda a: a != "-", tokens2)
      text1 = nltk.Text(tokens1)
      text2 = nltk.Text(tokens2)
      regno=tokens1[4]
      name1=' '.join(tokens1[9:11])
      coname='_'.join(tokens3[2:6])
      coname=coname.replace(":","")
      print coname
      code1=tokens2[16]
      code2=tokens2[33]
      code3=tokens2[48]
      code4=tokens2[63]
      code5=tokens2[82]
      code6=tokens2[100]
      subject1=' '.join(tokens2[17:22])
      subject2=' '.join(tokens2[34:37])
      subject3=' '.join(tokens2[49:52])
      subject4=' '.join(tokens2[64:71])
      subject5=' '.join(tokens2[83:89])
      subject6=' '.join(tokens2[101:104])
      credit1=tokens2[22]
      credit2=tokens2[37]
      credit3=tokens2[52]
      credit4=tokens2[71]
      credit5=tokens2[89]
      credit6=tokens2[104]
      credittot=tokens2[117]
      esa1=tokens2[23]
      esa2=tokens2[38]
      esa3=tokens2[53]
      esa4=tokens2[72]
      esa5=tokens2[90]
      esa6=tokens2[105]
      emax=80
      isa1=tokens2[25]
      isa2=tokens2[40]
      isa3=tokens2[55]
      isa4=tokens2[74]
      isa5=tokens2[92]
      isa6=tokens2[107]
      imax=20
      t1=tokens2[27]
      t2=tokens2[42]
      t3=tokens2[57]
      t4=tokens2[76]
      t5=tokens2[94]
      t6=tokens2[109]
      tmax=100
      gtmax=600
      grade1=tokens2[29]
      grade2=tokens2[44]
      grade3=tokens2[59]
      grade4=tokens2[78]
      grade5=tokens2[96]
      grade6=tokens2[111]
      tgrade=tokens2[123]
      gp1=tokens2[30]
      gp2=tokens2[45]
      gp3=tokens2[60]
      gp4=tokens2[79]
      gp5=tokens2[97]
      gp6=tokens2[112]
      cp1=tokens2[31]
      cp2=tokens2[46]
      cp3=tokens2[61]
      cp4=tokens2[80]
      cp5=tokens2[98]
      cp6=tokens2[113]
      tcp=tokens2[124]
      r1=tokens2[32]
      r2=tokens2[47]
      r3=tokens2[62]
      r4=tokens2[81]
      r5=tokens2[99]
      r6=tokens2[114]
      tr=tokens2[125]
      tot_marks=tokens2[121]
      scpa=tokens2[120]
      semester=1
      dbupdater(coname,semester,regno,name1,code1,subject1,esa1,isa1,t1,grade1,gp1,cp1,r1,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code2,subject2,esa2,isa2,t2,grade2,gp2,cp2,r2,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code3,subject3,esa3,isa3,t3,grade3,gp3,cp3,r3,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code4,subject4,esa4,isa4,t4,grade4,gp4,cp4,r4,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code5,subject5,esa5,isa5,t5,grade5,gp5,cp5,r5,scpa,tot_marks,tgrade,tcp,tr)
      dbupdater(coname,semester,regno,name1,code6,subject6,esa6,isa6,t6,grade6,gp6,cp6,r6,scpa,tot_marks,tgrade,tcp,tr)
      print name1+':'+regno+'\r\n\r\n'+code1+'   '+subject1+'   '+credit1+'   '+esa1+'   '+str(emax)+'   '+isa1+'   '+str(imax)+'   '+t1+'   '+str(tmax)+'   '+grade1+'   '+gp1+'   '+cp1+'   '+r1
      print '\r\n'+code2+'   '+subject2+'   '+credit2+'   '+esa2+'   '+str(emax)+'   '+isa2+'   '+str(imax)+'   '+t2+'   '+str(tmax)+'   '+grade2+'   '+gp2+'   '+cp2+'   '+r2
      print '\r\n'+code3+'   '+subject3+'   '+credit3+'   '+esa3+'   '+str(emax)+'   '+isa3+'   '+str(imax)+'   '+t3+'   '+str(tmax)+'   '+grade3+'   '+gp3+'   '+cp3+'   '+r3
      print '\r\n'+code4+'   '+subject4+'   '+credit4+'   '+esa4+'   '+str(emax)+'   '+isa4+'   '+str(imax)+'   '+t4+'   '+str(tmax)+'   '+grade4+'   '+gp4+'   '+cp4+'   '+r4
      print '\r\n'+code5+'   '+subject5+'   '+credit5+'   '+esa5+'   '+str(emax)+'   '+isa5+'   '+str(imax)+'   '+t5+'   '+str(tmax)+'   '+grade5+'   '+gp5+'   '+cp5+'   '+r5
      print '\r\n'+code6+'   '+subject6+'   '+credit6+'   '+esa6+'   '+str(emax)+'   '+isa6+'   '+str(imax)+'   '+t6+'   '+str(tmax)+'   '+grade6+'   '+gp6+'   '+cp6+'   '+r6
      print '\r\n'+'Total Credit : '+credittot+'\r\nSCPA : '+scpa+'\r\nTotal Marks : '+tot_marks+'/600'
      print '\r\n'+'Overall Grade : '+tgrade+'\r\nTotal CP : '+tcp+'\r\nOverall Status : '+tr      
      
      
def dbupdater(cname,sem,rno,sname,ccode,ctitle,esa1,isa1,stotal1,grade1,gp1,cp1,result1,scpa1,gtotal1,tgrade1,tcp1,status):
  college=str(cname)
  print college
  name=str(sname)
  semester=int(sem)
  regno=str(rno)
  c_code=str(ccode)
  course=ctitle
  esa=esa1
  isa=isa1
  stotal=stotal1
  grade=grade1
  gp=gp1
  cp=cp1
  result=str(result1)
  scpa=scpa1
  gtotal=gtotal1
  tgrade=tgrade1
  tcp=tcp1
  overallstatus=status
  db=MySQLdb.connect("localhost","root","<password>","dbname")
  cursor=db.cursor()
  cursor.execute("create table if not exists f"+college+"(id varchar(14),sem int,scpa int,gtotal int,tgrade char(1),tcp int,overallstatus varchar(10),primary key(id,sem))")
  try:
    cursor.execute("insert into f"+college+"(id,sem,scpa,gtotal,tgrade,tcp,overallstatus) values(%s,%s,%s,%s,%s,%s,%s)",(regno,semester,scpa,gtotal,tgrade,tcp,overallstatus))
    db.commit
  except:
    db.rollback
  cursor.execute("create table if not exists "+college+"(id varchar(14),name varchar(50),sem int,c_code varchar(10),course varchar(50),esa int,isa int,stotal int,grade char(1),gp int,cp int,result varchar(10),PRIMARY KEY(id,c_code))")
  try:
	cursor.execute("insert into "+college+"(id,name,sem,c_code,course,esa,isa,stotal,grade,gp,cp,result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(regno,name,semester,c_code,course,esa,isa,stotal,grade,gp,cp,result))
	db.commit()
  except:
	  db.rollback
  db.close()


def dbupdater2(countp,cname,appeared,sem,percent):
  college=str(cname)
  passedno=countp
  writtenno=appeared
  semester=sem
  passpercent=percent
  print passpercent
  db=MySQLdb.connect("localhost","root","<password>","<dbname>")
  cursor=db.cursor()
  cursor.execute("create table if not exists rank(college varchar(50),passedno int,writtenno int,semester int,passpercent int,PRIMARY KEY(semester,college))")
  try:
    cursor.execute("insert into rank(college,passedno,writtenno,semester,passpercent) values(%s,%s,%s,%s,%s)",(college,passedno,writtenno,semester,passpercent))
    db.commit()
  except:
      db.rollback
  db.close()
 
def dbupdater3(cname,college):
	tname=cname
	collegename=college
	db=MySQLdb.connect("localhost","root","<password>","<db name>")
	cursor=db.cursor()
	cursor.execute("create table if not exists collegename(college varchar(50),cname varchar(50),PRIMARY KEY(college,cname))")
	try:
		cursor.execute("insert into collegename(college,cname) values(%s,%s)",(collegename,tname))
		db.commit()
	except:
		db.rollback
	db.close()
	
	
main()
