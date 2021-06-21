#***************************************************************
#
#  Developer:         <Brandon>
#
#  Program #:         <Program 11>
#
#  File Name:         <Program11.py>
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Course Synonym:    <90696>
#
#  Due Date:          <July 27, 2019>
#
#  Instructor:        Sajjad Mohsin 
#
#  Chapter:           <Chapter #5, 6, 7, 8, 9>
#
#  Description:
#     <Calculates weekly pay given the users pay rate>
#
#***************************************************************



#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program; runs other functions
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
import Weiners

def main():
    taxRate = 0
    
    developerInfo()
    
    employeeData = Weiners.Employee() #verified @ phub
    
    empData = getInfo() #verified
    employeeData.set_scribbles(empData)#verified
    empData = employeeData.get_empData()#verified
    
    regPay = employeeData.get_Monayyy()    
    OTPay = employeeData.get_MoMonayyy()    
    grossPay = employeeData.get_grossPay()
    
    employeeData.set_taxes(taxRate)
    
    netPay = employeeData.get_netPay()
    
    print(employeeData)
    #end of function
#***************************************************************
#
#  Function:     getInfo
# 
#  Description:  Gets employee data
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************    
def getInfo():
    empName = input('Employee Name: ') #verified
    print()
    hourlyRate = float(input('What is your hourly rate?: '))
    print()
    weeklyHours = input('Enter your hours for the month by week: ')#string
    
    
    return empName, hourlyRate, weeklyHours #verified

#end function
#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     <Brandon>')
    print('Course:   Programming Fundamentals I')
    print('Program:  Eleven')
    print()
    # End of the developerInfo function

# Call the main function.
main()
