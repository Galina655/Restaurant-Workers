'''
CSC-226 Chapter 12/weeks 12-13 Topics OOP - Inheritance
Sample Program:  RestaurantPayroll
Sample Language: Python
Programmer: A. Wright
Date:       11/25/2018
Description: RestaurantWorker.py
Inheritance/Polymorphism Programming Project
 * 
 * super class RestaurantWorker has a self.__name, phone, netPay and a shift  these
 * are common properties of all workers at the Blue Moon Cafe
 * set and get methods are provided and there is a 
 * polymorphic generatePayCheck() method that is meant to be overridden in
 * sub classes
 * NOTE the enum type is not supported by Python 3 recoded Shift as a Set
'''

class RestaurantWorker:
   '''
   * CONVERSION constructor to build a RestaurantWorker object
   * accepts inputs for: self.__name, phone, shift  
   *
   '''
   def __init__ (self, name, phone, shift):
      self.__allShifts =  {'B', 'L', 'D', 'S'} 
      self.__name = name 
      self.__phone = phone 
      self.__shift = shift
      self.__netPay =200

   '''
   * DEFAULT CONSTRUCTOR (does not require inputs to build object)
   '''
   def __init__(self):
      self.__allShifts =  {'B', 'L', 'D', 'S'} 
      self.__name = input(" Please enter the employee's name > ") 
      self.__phone = input(" Please enter employee's phone number  > ")
      validate = True  #use flag to repeat prompt until valid input for shift
      while validate:
         shift = input('Select shift:\n "B" - Breakfast\n "L" - Lunch\n "D" - Dinner\n "S" - Swing ==> ')
         print('shift echo: ', shift[0].upper() )

         if shift[0].upper() in self.__allShifts:
            self.__shift = shift[0].upper()
            validate = False
         else:
            print ('Input error...try again, please\n')
      self.__netPay = 300       # initially all employees pay is 300
      
   '''
    * Mutator: setName() 
    * Sets the self.__name for this employee.
   '''
   
   def setName (self, name):
      self.__name = name 
    

   '''
    * Mutator: setPhone()
    * Sets self.__phone to the provided input phone number
    *  
    '''
   def  setPhone (self, phone):
      self.__phone = phone 
    
   '''
    * Mutator: setShift()
    *          verify valid input (member of set allShifts
    '''
   def  setShift (self, shift):
      if shift in self.__allShifts:
         self.__shift = shift 
    

   '''
    * Accessor: getName()
    *     returns a copy of the object's name
    '''
   def  getName(self):
      return self.__name 
    

   '''
    * Accessor: getPhone()
    *     returns a copy of the object's phone number
    '''
   def  getPhone(self):
      return self.__phone 
    
   '''
    * Accessor: getShift()
    *     returns a copy of the object's shift Breakfast, Lunch, Dinner, or Swing
   '''
   def  getShift(self):
      if self.__shift == 'B':
         shift = 'Breakfast'
      elif self.__shift == 'L':
         shift = 'Lunch'
      elif self.__shift == 'D':
         shift = 'Dinner'
      else:
         shift = 'Swing'
      return shift
   
   '''
   * Accessor: getPay()
   *     returns a copy of the object's pay
   '''
   def  getPay(self):
      return self.__netPay

   '''
   * Mutator: generatePayCheck()
   * specific to each RestaurantWorker
   * 
   '''
   def generatePayCheck(self):
      print(" INVALID--DO NOT CASH")
     
   '''
   * Accessor: __str__() -- Python's toString()
   * 
   * produces a String version of the object
   '''
   def __str__(self):
      out = "\tBlue Moon Cafe Employee Information\n"
      out = out +" "+ self.__name + "\t" + self.__phone + "\tShift: " + self.__shift +"\n"
      return out
   

class Cook(RestaurantWorker):
   def __init__(self, name, phone, shift, hourly_wage):
      super().__init__(name, phone, shift)
      self.hourly_wage = hourly_wage
   
