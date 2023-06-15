# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1868419 
 
# Date: 7/12/2021

# Initializing variables
pass_mark=0
defer_mark=0
fail_mark=0
progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0
star='*'
space=' '
# creating a list
range=[0,20,40,60,80,100,120]
        
# Defining the data        
while True:
            
# Checking user inputs are Valid or not        
    while True:
        try:
            pass_mark=int(input('\nEnter your pass mark: '))           
    
        except ValueError:                                           
            print('Integer Required')
            continue
        else:
            if pass_mark not in range:
                print("Out of range")
            elif pass_mark in range:
                break

    while True:
        try:
            defer_mark=int(input('Enter your defer mark: '))
    
        except ValueError:
            print('Integer Required')
            continue
        else:
            if defer_mark not in range:
                print("Out of range")
            elif defer_mark in range:
                break

    while True:
        try:
            fail_mark=int(input('Enter your fail mark: '))
        
        except ValueError:
            print('Integer Required')
            continue
        else:
            if fail_mark not in range:
                print("Out of range")
            elif fail_mark in range:
                break

    if pass_mark + defer_mark + fail_mark != 120:
            print("Total incorrect")
            continue

# Defining conditions to access students progress    
    if pass_mark==120:
        print("Progress")
        progress_count+=1
    elif pass_mark==100:
        print("Progress(Module trailer)")
        trailer_count+=1
    elif pass_mark<=80 and pass_mark>=40 and defer_mark<=80:
        print("Do not progress-Module retriever")
        retriever_count+=1
    elif pass_mark==20 and defer_mark<=100 and defer_mark>=40:
        print("Do not progress-Module retriever")
        retriever_count+=1
    elif pass_mark==0 and defer_mark<=120 and defer_mark>=60:
        print("Do not progress-Module retriever")
        retriever_count+=1
    elif pass_mark<=40 and fail_mark>=80:
        print("Exclude")
        exclude_count+=1

# continuation of the program until user decides to quit    
    cont=str(input("\nWould you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: "))   
    if cont=='y':
        continue
    elif cont=='q':
# Vertical histogram to display the results        
        print('\n')
        print('--------------------------------------------------------------------------')
        print('Vertical Histogram')
        total_outcome=progress_count+trailer_count+retriever_count+exclude_count
        print('Progress   Trailer   Retriever   Excluded')
        while(progress_count>0 or trailer_count>0 or retriever_count>0 or exclude_count>0):
            if(progress_count>0):
                print(f'{star:>4}',end='')
                progress_count-=1
            else:
                print(f'{space:>4}',end='')
            if(trailer_count>0):
                print(f'{star:>11}',end='')
                trailer_count-=1
            else:
                print(f'{space:>11}',end='')
            if(retriever_count>0):
                print(f'{star:>12}',end='')
                retriever_count-=1
            else:
                print(f'{space:>12}',end='')
            if(exclude_count>0):
                print(f'{star:>11}')
                exclude_count-=1
            else:
                print(f'{space:>11}')
                
                            
        print()
        print(total_outcome,'outcomes in total.')
        break