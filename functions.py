
 # syntax
# Declaring a function
def function_name():
   #  coding
   #  coding 
# Calling a function
function_name()

 # Function without parameters
def generate_full_name():
    first_name = 'Abdulkadir'
    last_name = 'Mohamud'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
    generate_full_name() # calling a function

    def add_two_numbers():
        num_one = 10
        num_two = 20
        total = num_one + num_two
        print(total)
        add_two_numbers()

        # function returning a Value 
        def generate_full_name ():
            first_name = 'Abdulkadir'
            last_name = 'Mohamud'
            space = ' '
            full_name = first_name + space + last_name
            return full_name
        print(generate_full_name())

        def add_two_numbers():
            num_one = 10
            num_two = 20
            total = num_one + num_two
            return total
        print(add_two_numbers())

        # function with parameters
        # syntax 
        # Declaring a function
        def function_name(parameter):
            #coding
            #coding
            # calling a function
            print(function_name(argument))

            def greetings (name):
                message = name+', welcome python for everyone !' 
                return message
            print(greetings('Abdulkadir'))

            def add_ten (num):
                ten = 10
                return num + ten
            print(add_ten(90))

            def sqaure_number (x):
                return x*x
            print(sqaure_number(2))

            def area_of_circle (r):
                PI = 3.14
                area = PI * r ** 2 
                return area
            print(area_of_circle(5))

            def sum_of_numbers(n):
                total = 0
                for i in range(n+1):
                    total += i
                print(total)
                print (sum_of_numbers(10)) # 55
                print (sum_of_numbers(100)) # 5050

                # syntax
                # Declaring a function
                def function_name():
                    #  coding
                    #  coding
                    # calling a function
                    print(function_name(arg1, arg2 ))

                    # example
                    def generate_full_name (first_name, last_name):
                        space = ' '
                        full_name = first_name + space + last_name
                        return full_name
                    print(generate_full_name('Abdulkadir', 'Mohamud'))

                    def sum_two_numbers (num_one, num_two):
                        sum = num_one + num_two
                        return sum
                    print('sum_two_numbers: ', sum_two_numbers(1, 9))

                    # passing Arguments with key and value
                    def print_full_name (first_name, last_name):
                        print(print_full_name(first_name = 'Abdulkadir', last_name = 'Mohamud'))
                        def add_two_numbers (num_one, num_two) # oeder does not matter

                        # Function returning a value- part 2
                        # Returning a string example
                        # def print_name (firstname): 
                        #    return firstname 
                       #  print_name ('Abdulkadir') # Mohamud
                       # def print_full_name (first_name, last_name):
                            space = ' '
                            full_name = first_name + space + last_name
                            return full_name
                       # print(print_full_name(first_name='Abdulkadir', last_name='Mohamud'))

                      # Functions with default parameters
                      # example
                       # def greetings (name = 'Abdulkadir'):
                            message = name+', welcome python for everyone !'
                            return message
                       # print(greetings())
                       # print(greetings('Abdulkadir'))

                        # Arbitrary Number of Arguments
                        # syntax 
                        # Declaring a function
                        def function_name(*args):
                            #coding
                            #coding
                            # calling a function
                            function_name(param1, param2, param3, ...) 

                            # Default and Arbitrary Number of Parameters in Functions
                           #  def generate_groups (team,*args):
                           print (team)
                        for i in args:
                            print(i)
                            print (generate_groups('team-1', 'Abdulkadir', 'yaasiin', 'Abdiaziz)'))
                    
                    
                        

                    
            
                    


    
    


