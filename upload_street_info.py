'''
Created on Jul 5, 2011

@author: varun
'''
import py2psql
import xlrd

def read_street_names(file):  #creates commands list for ML counts

    #---------Variables used-----------------------------------
    commands = []
    name = ""
    #-------------------------- open the .xls file------------------------------
    
    book = xlrd.open_workbook(file)
    
    #---------Find all sheet names in book-------------------------------------- 
   
    sheetnames =  book.sheet_names()
    
    #----------Loop through counts and Create SQL Commandslist with parameters-------------    
     
    totalsheets_ids = range(len(sheetnames))  #create sheet id list
    
    for sheet in totalsheets_ids :
       
        activesheet = book.sheet_by_name(sheetnames[sheet])
        row_ids = range(0,len(activesheet.col(0))) #find rows to process for column
            
        for row in row_ids:
                
            name = activesheet.cell_value(row,0) 
            if name != "" : #if we have a count, validate inputs !
                #-------Create time in time format !!!----------------- 
                commands.append(name)
                
    return commands

def read_int_ids(file):  #creates commands list for ML counts

    #---------Variables used-----------------------------------
    commands = []
    street1 = ""
    street2 = ""
    #ind_id = -1
    #-------------------------- open the .xls file------------------------------
    
    book = xlrd.open_workbook(file)
    
    #---------Find all sheet names in book-------------------------------------- 
   
    sheetnames =  book.sheet_names()
    
    #----------Loop through counts and Create SQL Commandslist with parameters-------------    
     
    totalsheets_ids = range(len(sheetnames))  #create sheet id list
    
    for sheet in totalsheets_ids :
       
        activesheet = book.sheet_by_name(sheetnames[sheet])
        row_ids = range(0,len(activesheet.col(0))) #find rows to process for column
            
        for row in row_ids:
                
            street1 = activesheet.cell_value(row,0)
            street2 = activesheet.cell_value(row,1)
            int_id = activesheet.cell_value(row,2)   
            if (street1 != "" and street2 != "" and int_id != ""): #if we have a count, validate inputs !
                #-------Create time in time format !!!----------------- 
                commands.append([street1,street2,int_id])
                
    return commands



if __name__ == '__main__':
    
    print "Input street names file to upload:"
    #filename = raw_input()
    filenamestreets = "C:\\Documents and Settings\\Varun\\Desktop\\Docs\\nodenumbering\\FINAL\\Streets.xls"
    filenameids = "C:\\Documents and Settings\\Varun\\Desktop\\Docs\\nodenumbering\\FINAL\\IntIds.xls"
    db = "postgres"
    user = "postgres"
    
    
    street_names = read_street_names(filenamestreets)
    py2psql.street_names(street_names,db,user)
    
    int_ids = read_int_ids(filenameids)
    py2psql.int_ids(int_ids,db,user)
    
    
    print "DONE!"
    