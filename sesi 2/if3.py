if 'foo' in ['foo', 'bar', 'baz']:        
    print('Outer condition is true')      

    if 10 > 20:                           
        print('Inner condition 1')        

    print('Between inner conditions')     

    if 10 < 20:                           
        print('Inner condition 2')        

    print('End of outer condition')       
print('After outer condition')            