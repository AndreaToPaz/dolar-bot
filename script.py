import requests
from bs4 import BeautifulSoup
import configparser

# Read URL from config.ini
config = configparser.ConfigParser()
config.read('config.ini') 

#Constant
REF_NAMES = ["EUR", "CNY", "TRY", "RUB", "USD"]

def get_html ( url : str ) -> str :
    """
    Purpose: Get the HTML document of an website using its URL
    """
    try:
        page_html = requests.get ( url )
        return ( page_html )
    except Exception as e:
        return ( print(e) ) 
# end def

def find_html_element_by_id ( html : str, html_tag : str, html_id : str ) ->  str :
    """
    Purpose: find an element in the HTML document by tag and id
    """
    try:
        soup = BeautifulSoup ( html.content, "html.parser" )
        changes = soup.find_all ( html_tag , class_= html_id )
        return changes
    except Exception as e:
        return ( print(e) ) 
# end def

def str_list_to_float_list ( changes : list, changes_name : list ) -> list :
    """
    Purpose: arg
    """
    ref_change_list = []
    changes_modify = []
    for i in range ( len ( changes ) ) :
        #First replace "," to "." to be able to cast the string to a float later
        changes_modify.append( changes[i].text.replace ( "," , "." ) )  
        ref_change_list.append( [ changes_name[i] , float( changes_modify[i] ) ] )
    return  ref_change_list
# end def


# #
#                                                                  MAIN
# #

html =  get_html(config ['BancoDeVenezuela'] ['BANK_URL'])
changes = find_html_element_by_id(html,"div", "col-sm-6 col-xs-6 centrado" )
ref_num_lits = str_list_to_float_list(changes,REF_NAMES)
print(ref_num_lits)