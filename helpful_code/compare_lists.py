list1 = input('Enter List 1').split()
list2 = input('Enter List 2').split()


def compare_lists(control, test):
    diff1 = set(test) - set(control)
    if len(diff1)==0:
        print('All values in Test are in Control')
    else:
        print('''Values in Test that are not in Control:
        ''',diff1)
    
    diff2 = set(control) - set(test)
    if len(diff2) == 0:
        print('All values in Control are in Test')
    else:
        print('''Values in Control that are not in Test:
        ''',diff2) 
        
compare_lists(list1,list2)
