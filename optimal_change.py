def optimal_change(item_cost, amount_paid):

    dollars = {'$100': 100, '$50': 50, '$20': 20, '$10': 10, '$5': 5, '$1': 1} #dollars will hold dollar amount as string (key) and int value (value)
    cents = {'quarter' : .25, 'dime': .10, 'nickle': .05, 'penny': .01} #cents will hold cent amount as string (key) and int value (value)

    optimal_change = amount_paid - item_cost #optimal_change will hold ideal change to give back
    
    if optimal_change < 0: #to check for cases of under payment
        return f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is not enough to pay for item. Customer still owes ${abs(round(optimal_change, 2))}."
    
    optimal_dollar = optimal_change // 1 #using floor to just get dollar amount
    optimal_cents = round(optimal_change - optimal_dollar, 2) #subtracting total change from dollar amount to get change and then using round to the 2nd place to only return .00 from decimal
    
    #storing final amount in lists which will be appended from for loops
    final_dollar_amount = []
    final_cent_amount = []
    
    # loop through dollars dictionary
    for dollar in dollars:
        string_dollar = dollar
        value_dollar = dollars[dollar]
        while optimal_dollar >= value_dollar: #set while optimal dollar amount is greater or equal to dollar value in dictionary
            final_dollar_amount.append(string_dollar) #if greater or equal, append to dollar list
            optimal_dollar = optimal_dollar - value_dollar #subtract dollar value from optimal dollar amount
    
    #doing the same things as above for loop but with cents dictionary
    for cent in cents:
        string_cents = cent
        value_cents = cents[cent]
        while optimal_cents >= value_cents:
            final_cent_amount.append(string_cents)
            optimal_cents = round(optimal_cents - value_cents, 2)
            
    
    #concatenating final dollar amount and final cent amount lists
    full_change = final_dollar_amount + final_cent_amount

    #calling turn_to_sentence function with concatenated list item_cost and amount_paid parametersn which will be the result returned
    result = turn_to_sentence(full_change, item_cost, amount_paid)
    
    return result
#creating function that will take in list and set conditions based on items in list and return full string    
def turn_to_sentence(list, cost, paid):
    full_string = '' #variable which will hold change amount 
    x = 0 #setting x to 0 for while loop
    if len(list) == 0: #to catch exact change and return string no change
        full_string += 'no change'
    if len(list) == 1: #if only one item in string, appending 0 to fit conditions 
        list.append(0)
    while x < len(list): #looping through the list for length of list
        counting = list.count(list[x]) #check if plural needed, how many instances are in list
        if counting > 1: #checking if plural
            if x + counting == len(list) and list[1] != 0:
                full_string += 'and '
            if '$' in list[x]:
                full_string += f'{counting} {list[x]} bills'
            elif list[x] == 'penny':
                full_string += f'{counting} pennies'
            else:
                full_string += f'{counting} {list[x]}s'
        elif counting == 1: #checking if singular
            if '$' in list[x]:
                full_string += f'{counting} {list[x]} bill'
            else:
                full_string += f'{counting} {list[x]}'
        x = x + counting #incrementing x by number of instances 
        if len(list) == 2 and list[1] == 0: #break on condition where only one item in list
            break
        if x != len(list): #adding comma as long as not last item on list
            full_string += ', '
    
    return f'The optimal change for an item that costs ${cost} with an amount paid of ${paid} is {full_string}.'
    

