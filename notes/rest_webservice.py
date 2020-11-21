''' Demonstrate how to make a REST API using itty.
    Show the effective use of decorators to register functions to routes.

    * Welcome page
    * Time server
    * Dynamic directory display is JSON format
    * Simple text title casing and upper cases services
    * Document finder services:  search, retrieve, and upload

'''

from itty import run_itty, get, Response, NotFound, post
import time
import subprocess
import json
import os
import docfinder

@get('/')
def welcome(request):
    return '"Howdy!"'

@get('/now')
def get_time(request):
    return time.ctime()

@get('/files')
def show_notes(request):
    files = os.listdir('notes')
    result = json.dumps(files, indent=4)
    return Response(result, content_type='application/json')

@get('/stat')
def show_network_status(request):
    result = subprocess.check_output('netstat -a', shell=True)
    return Response(result, content_type='text/plain')

@get('/free')
def show_network_status(request):
    result = subprocess.check_output('df', shell=True)
    return Response(result, content_type='text/plain')

@get('/upper')         # /upper?q=raymond
def upper_case(request):
    word = request.GET.get('q', '--')
    return word.upper()

@get('/security/hole') # /security/hole?q=cal+2+2012
def bryn(request):
    command = request.GET.get('q', "echo 'Enter a query'")
    result = subprocess.check_output(command, shell=True)
    return Response(result, content_type='text/plain')

@get('/search')        # /search?q=Hettinger+Enumerates
def search(request):
    query = request.GET.get('q', 'nothing')
    terms = query.split()
    uris = docfinder.document_search(*terms)
    result = json.dumps(uris, indent=4)
    return Response(result, content_type='application/json')

@get('/doc')           # /doc?uri=pep-0289
def document(request):
    uri = request.GET.get('uri', '')
    try:
        doc = docfinder.get_document(uri)
    except docfinder.UnknownURI:
        raise NotFound(uri)
    return Response(doc, content_type='text/plain')    

if __name__ == '__main__':
    run_itty(host='', port=8080)



















