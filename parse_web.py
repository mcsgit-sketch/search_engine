
def get_links(html): 
    page_length = len(html) 
    links = []
    i = 0

    while i < page_length:
        link = ""

        if html[i:i+2] == "<a":
            i += 3
            while i < page_length: 
                # href = " or href=" or href= "
                if html[i:i+4].lower() == "href":
                    i += 4
                
                if html[i] == "=":
                    i += 1 
                start = 0
                if html[i] == "\"":
                    i += 1 
                    while html[i] != "\"":
                        link += html[i]
                        i+=1
        links.append(link)

        i += 1
    return links
