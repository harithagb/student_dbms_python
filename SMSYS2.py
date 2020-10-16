import sqlite3

conn = sqlite3.connect('student.db')
def create_table():
	conn.execute("CREATE TABLE IF NOT EXISTS studentdb(SRN TEXT PRIMARY KEY, NAME TEXT, DOB TEXT, MA1 FLOAT, MA2 FLOAT, CSP FLOAT, CSPL FLOAT, CSC FLOAT, CSCL FLOAT, EEE FLOAT, ECE FLOAT, MES FLOAT, CAEG FLOAT, CV FLOAT, PHYS FLOAT, PHYSL FLOAT, CHEM FLOAT, CHEML FLOAT, BIO FLOAT, SGPAP FLOAT, SGPAC FLOAT, CGPA FLOAT)")
def start():
	print("")
	print("Enter 1 to enter a new record")
	print("Enter 2 to retrieve a record")
	print("Enter 3 to update a record")
	print("Enter 4 to delete a record")
	print("")
	s=int(input("Please enter a number (1/2/3/4) : "))
	while (s!=1 and s!=2 and s!=3 and s!=4):
		s=int(input("Please enter a valid number : "))
	if (s==1):
		insert_newdata()
	elif (s==2):
		retrieve_data()
	elif (s==3):
		update_record()
	elif (s==4):
		delete_record()
def phys_cycle():
	global csp
	csp=float(input("Introduction to Computing Using Python (UE18CS101) : "))
	global ee
	ee=float(input("Basic Electrical Engineering (UE18EE101) : "))
	global maone
	maone=float(input("Engineering Mathematics - I (UE18MA101) : "))
	global me
	me=float(input("Mechanical Engineering Sciences (UE18ME101) : "))
	global caeg
	caeg=float(input("Computer Assissted Engineering Graphics (UE18ME102) : "))
	global ph
	ph=float(input("Engineering Physics (UE18PH101) : "))
	global phl
	phl=float(input("Engineering Physics Lab (UE18PH102) : "))
	global cspl
	cspl=float(input("Introduction to Computing using Python Lab (UE18CS102) : "))
	global x
	sgpap=(((round(csp/10))*4)+((round(ee/10))*4)+((round(maone/10))*5)+((round(me/10))*4)+((round(caeg/10))*2)+((round(ph/10))*4)+((round(phl/10))*2)+((round(cspl/10))*2))/27
	x=round(sgpap,2)
def chem_cycle():
	global bio
	bio=float(input("Engineering Biology (UE18BT101) : "))
	global csc
	csc=float(input("Introduction to C (UE18CS101) : "))
	global cv
	cv=float(input("Engineering Mechanics (UE18CV101) : "))
	global chem
	chem=float(input("Engineering Chemistry (UE18CY101) : "))
	global ec
	ec=float(input("Basic Electronics Engineering (UE18EC101) : "))
	global matwo
	matwo=float(input("Engineering Mathematics - II (UE18MA101) : "))
	global cscl
	cscl=float(input("Introduction to C Lab (UE18CS102) : "))
	global cheml
	cheml=float(input("Engineering Chemistry Lab (UE18CY102) : "))
	global y
	sgpac=(((round(bio/10))*2)+((round(csc/10))*4)+((round(cv/10))*4)+((round(chem/10))*4)+((round(ec/10))*4)+((round(matwo/10))*5)+((round(cscl/10))*2)+((round(cheml/10))*2))/27
	y=round(sgpac,2)
def cycle():
	c=input("Enter the cycle the student belonged to in Semester-1 (P/C) : ")
	while c!='P' and c!='p' and c!='C' and c!='c':
		print("Please enter a valid option")
		c=input("Enter the cycle the student belonged to in Semester-1 (P/C) : ")
	if c=='P' or c=='p':
		print("Enter the marks obtained by the student in Semester-1")
		phys_cycle()
		print("")
		print("Enter the marks obtained by the student in Semester-2")
		chem_cycle()
		
	else:
		print("Enter the marks obtained by the student in Semester-1")
		chem_cycle()
		print("")
		print("Enter the marks obtained by the student in Semester-2")
		phys_cycle()
		
def new_record():
	n=input("Would you like to enter a new record? (Y/N)")
	if n=='y' or n=='Y':
		insert_newdata()
	if n=='n' or n=='N':
		start()
def insert_newdata():
	print("")
	srn=input("Enter the student's SRN (PES12018xxxxx): ")
	while (len(srn)!=13) or not srn.startswith("PES12018"):
		srn=input("Please enter the student's valid SRN : ")
	name=input("Enter the student's name : ")
	dob=input("Enter the student's date of birth (DD-MM-YYYY) : ")
	print("")
	cycle()
	cgpa=round(((x+y)/2),2)
	conn.execute("INSERT INTO studentdb(SRN, NAME, DOB, MA1, MA2, CSP, CSPL, CSC, CSCL, EEE, ECE, MES, CAEG, CV, PHYS, PHYSL, CHEM, CHEML, BIO, SGPAP, SGPAC, CGPA) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(srn, name, dob, maone, matwo, csp, cspl, csc, cscl, ee, ec, me, caeg, cv, ph, phl, chem, cheml, bio, x, y, cgpa))
	conn.commit()
	print("New record has been inserted successfully")
	new_record()
def retrieve_data():
	print("")
	id=input("Enter the student's SRN (PES12018xxxxx) : ")
	while (len(id)!=13) or not id.startswith("PES12018"):
		id=input("Please enter the student's valid SRN : ")
	row=list(conn.execute(("SELECT * FROM studentdb WHERE SRN=?"),(id,)))
	conn.commit()
	print("")
	try:
		print("SRN  : ", row[0][0])
		print("NAME : ", row[0][1])
		print("DOB  : ", row[0][2])
		print("")
		print("Engineering Mathematics - I                  (UE18MA101) :   ", row[0][3])
		print("")
		print("Engineering Mathematics - II                 (UE18MA101) :   ", row[0][4])
		print("")
		print("Introduction to Computing Using Python       (UE18CS101) :   ", row[0][5])
		print("")
		print("Introduction to Computing Using Python Lab   (UE18CS102) :   ", row[0][6])
		print("")
		print("Introduction to C                            (UE18CS101) :   ", row[0][7])
		print("")
		print("Introduction to C Lab                        (UE18CS102) :   ", row[0][8])
		print("")
		print("Basic Electrical Engineering                 (UE18EE101) :   ", row[0][9])
		print("")
		print("Basic Electronics Engineering                (UE18EC101) :   ", row[0][10])
		print("")
		print("Mechanical Engineering Sciences              (UE18ME101) :   ", row[0][11])
		print("")
		print("Computer Assissted Engineering Graphics      (UE18ME102) :   ", row[0][12])
		print("")
		print("Engineering Mechanics                        (UE18CV101) :   ", row[0][13])
		print("")
		print("Engineering Physics                          (UE18PH101) :   " , row[0][14])
		print("")
		print("Engineering Physics Lab                      (UE18PH102) :   ", row[0][15])
		print("")
		print("Engineering Chemistry                        (UE18CY101) :   ", row[0][16])
		print("")
		print("Engineering Chemistry Lab                    (UE18CY102) :   ", row[0][17])
		print("")
		print("Engineering Biology                          (UE18BT101) :   ", row[0][18])
		print("")
		print("SGPA - P                                                 :   ", row[0][19])
		print("")
		print("SGPA - C                                                 :   ", row[0][20])
		print("")
		print("CGPA                                                     :   ", row[0][21])
		print("")
	except IndexError:
		print("No such record exists")
	start()
def delete_record():
	print("")
	d=input("Enter the SRN of the student whose record is to be deleted (PES12018xxxxx) : ")
	while (len(d)!=13) or not d.startswith("PES12018"):
		d=input("Please enter the student's valid SRN : ")
	conn.execute(("DELETE FROM studentdb WHERE SRN=?"),(d,))
	conn.commit()
	print("Record has been deleted successfully")
	start()
def newsgpap(srn):
        row=list(conn.execute(("SELECT * FROM studentdb WHERE SRN=?"),(srn,)))
        conn.commit()
        newsgpap=(((round(row[0][5]/10))*4)+((round(row[0][9]/10))*4)+((round(row[0][3]/10))*5)+((round(row[0][11]/10))*4)+((round(row[0][12]/10))*2)+((round(row[0][14]/10))*4)+((round(row[0][15]/10))*2)+((round(row[0][6]/10))*2))/27
        conn.execute(("UPDATE studentdb SET SGPAP = ? WHERE SRN = ?"),(round(newsgpap,2),srn))
        conn.commit()
        newcgpa(srn,newsgpap,p)
def newsgpac(srn):
        row=list(conn.execute(("SELECT * FROM studentdb WHERE SRN=?"),(srn,)))
        newsgpac=(((round(row[0][18]/10))*2)+((round(row[0][7]/10))*4)+((round(row[0][13]/10))*4)+((round([0][16]/10))*4)+((round(row[0][10]/10))*4)+((round(row[0][4]/10))*5)+((round(row[0][8]/10))*2)+((round(row[0][17]/10))*2))/27
        conn.execute(("UPDATE studentdb SET SGPAC = ? WHERE SRN = ?"),(round(newsgpac,2),srn))
        conn.commit()
        newcgpa(srn,newsgpac,c)
def newcgpa(srn,newsgpa,x):
        if x=="p":
                newcgpa=(newsgpa+row[0][20])/2
                conn.execute(("UPDATE studentdb SET CGPA = ? WHERE SRN = ?"),(round(newcgpa,2),srn))
                conn.commit()
        elif x=="c":
                newcgpa=(newsgpa+row[0][19])/2
                conn.execute(("UPDATE studentdb SET CGPA = ? WHERE SRN = ?"),(round(newcgpa,2),srn))
                conn.commit()
def update_record():
	print("")
	srn=input("Enter the SRN of the student whose record is to be updated (PES12018xxxxx) : ")
	while (len(srn)!=13) or not srn.startswith("PES12018"):
		srn=input("Please enter the student's valid SRN : ")
	c=input("Please enter which record is to be updated (NAME, DOB, MA1, MA2, etc) : ")
	while (c!='NAME' and c!='DOB' and c!='MA1' and c!='MA2' and c!='CSP' and c!='CSPL' and c!='CSC' and c!='CSCL' and c!='EEE' and c!='ECE' and c!='MES' and c!='CAEG' and c!='CV' and c!='PHYS' and c!='PHYSL' and c!='CHEM' and c!='CHEML'):
		c=input("Please enter a valid record : ")
	col=['NAME','DOB','MA1','CSP','CSPL','EEE','MES','CAEG','PHYS','PHYSL','MA2','CSC','CSCL','ECE','CV','CHEM','CHEML','BIO']
	pcol=['MA1','CSP','CSPL','EEE','MES','CAEG','PHYS','PHYSL']
	ccol=['MA2','CSC','CSCL','ECE','CV','CHEM','CHEML','BIO']
	for i in col:
                if c==i:
                        nr=input("Enter the new record : ")
                        x="UPDATE studentdb SET "+i+" = ? WHERE SRN = ?"
                        conn.execute((x),(nr,srn))
                        conn.commit()
                        print("")
                        print("Record updated successfully")
                        if c in pcol:
                                newsgpap(srn)
                        elif c in ccol:
                                newsgpac(srn)
                        else:
                                pass
                else:
                        pass
                
	start()
	
create_table()
start()
