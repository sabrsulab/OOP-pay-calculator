class Employee:

    
    def __init__(self):

        self.__hourlyRate = 7.25 #verified
        self.__regHours = 0.0 #verified
        self.__overtimeHrs = 0.0 #verified
        
    def set_scribbles(self, empData):
        self.__empName = empData[0] #verified
        self.__hourlyRate = empData[1]
        self.__totalHours = empData[2]


    def get_empData(self):
        
        self.__totalHours = self.__totalHours.split(', ')
        
        for r in range(len(self.__totalHours)):
            self.__totalHours[r] = int(self.__totalHours[r])#verified
        
        
        for r in range(len(self.__totalHours)):
            if self.__totalHours[r] > 40:
                self.__overtimeHrs += self.__totalHours[r] - 40
                self.__regHours += 40
            else:
                self.__regHours += self.__totalHours[r]#verified
        self.__totalHoras = self.__regHours + self.__overtimeHrs
        
        return self.__empName, self.__hourlyRate, self.__regHours, self.__overtimeHrs

    def get_Monayyy(self):

        self.__regPay = self.__hourlyRate * self.__regHours
        return self.__regPay

    def get_MoMonayyy(self):

        self.__OTPay = (self.__hourlyRate * self.__overtimeHrs) * 1.5
        return self.__OTPay

    def get_grossPay(self):
        
        self.__grossPay = self.__regPay + self.__OTPay
        return self.__grossPay
    
    def set_taxes(self, taxRate):
        
        if self.__grossPay > 10000:
            taxRate = .36
        elif self.__grossPay > 6000:
            taxRate = .31
        elif self.__grossPay > 3500:
            taxRate = .28
        elif self.__grossPay > 2000:
            taxRate = .15
        else:
            taxRate = .10

        self.__taxes = self.__grossPay * taxRate
        
    def get_netPay(self):
        
        self.__netPay = self.__grossPay - self.__taxes
        return self.__netPay
    
    def __str__(self):
        return '\nEmployee Name: ' + self.__empName + '\nRegular Hours: ' + format(float(self.__regHours)) +\
               '\nOvertime Hours: ' + format(float(self.__overtimeHrs)) + '\nTotal Hours: ' +\
               format(float(self.__totalHoras)) + '\nPay Rate: $' + format(float(self.__hourlyRate), '.2f') +\
               '\n\nMonthly Regular Pay: $' + format(float(self.__regPay), '.2f') + '\nMonthly Overtime Pay: $' +\
               format(float(self.__OTPay), '.2f') + '\nMonthly Gross Pay: $' + format(float(self.__grossPay), '.2f') +\
               '\nMonthly Taxes: $' + format(float(self.__taxes), '.2f') + '\nMonthly Net Pay: $' + format(float(self.__netPay), '.2f')
