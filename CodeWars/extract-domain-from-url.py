
#!Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
# domain_name("http://github.com/Rex-Arnab") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

def domain_name(url):
    try:
        a,name = url.split("//")
    except:
        name = url
    if "www" in name:
        return name.split(".")[1]
    else:
        return name.split(".")[0]