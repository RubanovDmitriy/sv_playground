from bs4 import BeautifulSoup


def handle_embedded_code(iframe):
    soup = BeautifulSoup(iframe, "html.parser")
    return soup.iframe['src']
