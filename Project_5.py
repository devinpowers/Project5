
# project 5:
    
def open_file():
    filename = input("Input a file name: ")
    
    fp = open(filename,'r')
    
    return fp


""" Need to add Try and Except"""
   
def get_us_value(fp):
   
    #skips two lines of txt file
    fp.readline()
    fp.readline()
    
    for line in fp:
        state = str(line[0:20]).strip()
        percent =(line[25:29]).strip()
        
        if state == 'United States':
            return float(percent)
        
    
def get_min_value_and_state(fp):
    
    
    fp.seek(0)
    fp.readline()
    fp.readline()
    
    min_value = 100
    min_state = " "
    word = "NA"

    for line in fp:
     
        if not word in line:
    
            state = str(line[0:20]).strip()
            value = float( (line[25:29]).strip())
            
            
            
            if value < min_value: 
                min_value = value
                min_state = state
                
    return min_value, min_state
        
        
        

def get_max_value_and_state(fp):
    
    fp.seek(0)
    fp.readline()
    fp.readline()
    
    max_value = 0
    max_state = " "
    word = "NA"
    
    for line in fp: 
        if not word in line:
    
            state = str(line[0:20]).strip()
            value = float( (line[25:29]).strip())
                    
            
            if value > max_value: 
                max_value = value
                max_state = state
                
    return max_value, max_state
    
        
def display_herd_immunity(fp):
    
    
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
    
    
      
    '''Open the file and try and except shit.'''
     ## open the file
    
    fp = open_file()
    
    percent = get_us_value(fp)
    
    print("Overall US MMR Coverage:", percent)
    
    # minumum value for MMR Coverage
    
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


