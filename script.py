import requests
from bs4 import BeautifulSoup
import configparser

# Read URL from config.ini
config = configparser.ConfigParser()
config.read('config.ini') 


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

def find_html_element_by_id ( html : str, html_tag : str, html_id : str ) -> str:
    """
    Purpose: find an element in the HTML document by tag and id
    """
    soup = BeautifulSoup ( html.content, "html.parser" )
    changes = soup.find_all ( html_tag , class_= html_id )
    return changes
    
# end def



html =  get_html(config ['BancoDeVenezuela'] ['BANK_URL'])
changes = find_html_element_by_id(html,"div", "col-sm-6 col-xs-6 centrado" )
print (changes)