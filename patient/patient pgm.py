

# Joe Joseph

# Intro to Programming

import proc1
import patient1

def main():

    # variables
    
    name_1p1 = patient1.Patient('John', '1st road Town FL 65655', 'Charles 111-111-1111')

    #name_1p2 = patient1.patient('Nick', '2nd road, Place, FL, 65644', 'Pete, 111-111-2222')

    #name_1p3 = patient1.patient('Paul', '3rd road, City, FL, 65633', 'Sam, 111-111-3333')

    #proc_1p1 = proc1.proc('Procedure name: Physcial Exam', 'Date: 30 March 2021', 'Practitioner: Dr. Irvie', 'Charge: 250.00')

    #proc_1p2 = proc1.proc('Procedure name: X-ray', 'Date: 30 March 2021', 'Practitioner: Dr. Jamison', 'Charge: 500.00')

    #proc_1p3 = proc1.proc('Procedure name: Blood test', 'Date: 30 March 2021', 'Practitioner: Dr. Smith', 'Charge: 200.00')


    # Call Data

    print('Procedure #1')

    print(name_1p1.get_name_1(), '\n', name_1p1.get_address_1(), '\n', name_1p1.get_phone_1(), '\n', name_1p1.get_emergency_1())
    

    
    
    
main()
