import webbrowser 
# Documnetation of webbrowser module - https://docs.python.org/3/library/webbrowser.html

tab_specify = 2  #Open a new browser tab

url = "https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

webbrowser.open(url, new=tab_specify)