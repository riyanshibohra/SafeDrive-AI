from route_optimization_ny import route_optimisation 

def safe_driving(start_location,end_location):
    route_optimisation(start_location,end_location)

def unsafe_driving(state,message):
    print(f"{message}")


def use_predicate_logic(model_output,start_location='',end_location=''):
    '''
        This function determines what alerts will be shown based on Deep Learning Model.
    '''


    # model_output dictionary
        # 0: Safe driving
        # 1: Minimum distraction
        # 2: Turning
        # 3: Texting on the phone
        # 4: Talking on the phone


    #Getting preloaded states for user error
    output_dict_state= {}
    with open('state_dict.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split(': ')
                output_dict_state[int(key)] = value
    
    
    #Getting preloaded messages for user error
    output_dict_message= {}   

    with open('message_dict.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split(': ')
                output_dict_message[int(key)] = value
    
    
    state=output_dict_state[model_output]
    message=output_dict_message[model_output]
    
    #Predicate Logic- Based on model output for attention status
    if(model_output in (0,1)):
        #Continue showing the route when attentive
        safe_driving(start_location,end_location)
    
    else:
        #Show error message- For real world scenario, this will trigger the alert systems
        unsafe_driving(state,message)

        
        
        # Code block for reference future plan
        # if(model_output=2)
        #      trigger_sound()
        
        # if(model_output=3)
        #      trigger_sound()
        #      trigger_visual()
        

        # if(model_output=4)
        #      trigger_sound()
        #      trigger_visual()
        #      trigger_haptic()
        

#Code start


# def get_user_input():
#     print("Note: Give location in format - Location, New York")
#     start_location=input("Start Location: ")
#     end_location=input("End Location: ")

#     route_optimisation(start_location,end_location)


if __name__ == '__main__':
    
    model_output=3
    
    
    try:
   
        
        #get_user_input()
        use_predicate_logic(model_output)

    except Exception as e:
        print(f"Error found- {e}")
