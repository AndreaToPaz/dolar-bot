import requests
from bs4 import BeautifulSoup
from app.__init__ import config
from app.utils.help_function import str_list_to_float_list

#Constant
REF_NAMES = ['EUR', 'CNY', 'TRY', 'RUB', 'USD']

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

def find_html_element_by_id ( html : str , html_tag : str , html_id : str ) ->  str :
    """
    Purpose: find an element in the HTML document by tag and id
    """
    try:
        soup = BeautifulSoup ( html.content , 'html.parser' )
        changes = soup.find_all ( html_tag , class_= html_id )
        return changes
    except Exception as e:
        return ( print(e) ) 
# end def

# #
#                                                                  MAIN
# #

html =  get_html( config ['BancoDeVenezuela'] ['BANK_URL'])
currency = find_html_element_by_id( html , 'div' , 'col-sm-6 col-xs-6 centrado' )
currency_list = str_list_to_float_list ( currency , REF_NAMES )