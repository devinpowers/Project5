
# project 5:
    
def open_file():
    ''' Open File with try-except to catch errors, if it fails to open, reprompt '''
    
    filename = input("Input a file name: ")
    while True:
        
        try:
            fp = open(filename,'r')
            break #sucessfull
        # If the users enters in the incorrect file 
        except IOError:
            print("Unable to open file. Please try again.")
            filename = input("Input a file name: ")

    return fp
   
def get_us_value(fp):
   
    #skips the first two header lines of txt file
    fp.readline()
    fp.readline()
    
    #reads the txt file line by line
    for line in fp:
        state = str(line[0:20]).strip()
        percent =(line[25:29]).strip()
        
        if state == 'United States':
            return float(percent)
        
    
def get_min_value_and_state(fp):
    ''' Find and Minimmum value in the file and its associated state '''
    #Rewind file and skip first two headers
    fp.seek(0)
    fp.readline()
    fp.readline()
    
    min_value = 100
    min_state = " "
    word = "NA"

    for line in fp:
     # skipping line with 'NA' 
        if not word in line:
            
            
            state = str(line[0:20]).strip()
            value = float( (line[25:29]).strip())
         
            if value < min_value: 
                min_value = value
                min_state = state
                
    return min_value, min_state
        

def get_max_value_and_state(fp):
    ''' Find and Maximum value in the file and its associated state '''
    
    fp.seek(0)
    fp.readline()
    fp.readline()
    
    max_value = 0
    max_state = " "
    word = "NA"
    
    for line in fp: 
        if not word in line:
    
            state = str(line[0:20]).strip()
            value = float((line[25:29]).strip())
                    
            if value > max_value: 
                max_value = value
                max_state = state
                
    return max_value, max_state
    
        
def display_herd_immunity(fp):
    ''' Displays all the States whose coverage is less than 90% '''
    
    print("\nStates with insufficient Measles herd immunity.")
    print("{:<25s}{:>5s}".format("State","Percent"))
    
    fp.seek(0)
    fp.readline()
    fp.readline()
    
    word = "NA"
    
    for line in fp:
        if not word in line:
        
            state = str(line[0:20]).strip()
            value = float( (line[25:29]).strip())
            
            if value < 90.0:
                state_90 = state
                value_90 = value
            
                print("{:<25s}{:>5f}".format(state_90,value_90))   
             
def write_herd_immunity(fp):
    ''' Writes into a file named herd.txt all the states whose coverage is less than 90% '''
    
    outfile = open("herd.txt", "w")
    
    print("\nStates with insufficient Measles herd immunity.",file = outfile)
    print("{:<25s}{:>5s}".format("State","Percent"),file = outfile)
    
    fp.seek(0)
    fp.readline()
    fp.readline()
    
    word = "NA"
    
    for line in fp:
        if not word in line:
        
            state = str(line[0:20]).strip()
            value = float( (line[25:29]).strip())

            if value < 90.0:
                state_90 = state
                value_90 = value
            
                print("{:<25s}{:>5f}".format(state_90,value_90),file = outfile)
    
    outfile.close()


def main():
    
    '''Open the file and try and except.'''
    # call function to open the file
    fp = open_file()
    
    percent = get_us_value(fp)
    
    print("Overall US MMR Coverage: ", percent)
    
    # Minumum value for MMR Coverage
    
    min_value, min_state = get_min_value_and_state(fp)
    
    print("State with minimal MMR Coverage: ", min_state, min_value)
    
    
    # maximum value for the MMR Coverage
    
    max_value, max_state = get_max_value_and_state(fp)
    
    print("State with the maximum MMR Coverage:", max_state, max_value)
     
    #display herd immunity (call the function here)
    
    display_herd_immunity(fp)
    
    
    #write the herd immunity to another txt file
    write_herd_immunity(fp)
    


if __name__ == "__main__":
    main()    


