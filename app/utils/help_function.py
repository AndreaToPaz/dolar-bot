
def str_list_to_float_list ( currency : list, currency_name : list ) -> list :
    """
    Purpose: Convert the currency number string into a float 
    """
    ref_currency_list = []
    currency_modify = []
    try:
        for i in range ( len ( currency ) ) :
            #First replace "," to "." to be able to cast the string to a float later
            currency_modify.append( currency[i].text.replace ( ',' , '.' ) )  
            ref_currency_list.append( [ currency_name[i] , float( currency_modify[i] ) ] )
        return  ref_currency_list
    except Exception as e:
        return ( print(e) ) 
# end def

def currency_format ( currency : list ) -> str :
    """
    Purpose: Format he currency exchange list to display it in Telegram Bot
    """
    currency_string = ''
    try:
        for i in range ( len ( currency ) ) :
            #First format currency values to %2
            currency_string = currency_string + currency[i][0] + ' ' + '{:.2f}'.format( currency[i][1] ) + '\n'
        return currency_string
    except Exception as e:
        return ( print(e) ) 

 # end def