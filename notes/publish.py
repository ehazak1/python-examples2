#! /usr/bin/env python2.7

from highlight import analyze_python, build_html_page
import os, glob, cgi

index_html = '''\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
          "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-type" content="text/html;charset=UTF-8">
<meta http-equiv="refresh" content="15">
<link rel="shortcut icon" href="http://www.python.org/favicon.ico">
<title> {title} </title>
<style type="text/css">
{css}
</style>
</head>
<body>
{body}
</body>
</html>
'''

html = '''\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
          "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-type" content="text/html;charset=UTF-8">
<title> {title} </title>
<link rel="shortcut icon" href="http://www.python.org/favicon.ico">
<style type="text/css">
{css}
</style>
</head>
<body>
{body}
</body>
</html>
'''

def publish_one(sourcefile, destfile):
    with open(sourcefile) as sf:
        source = sf.read()
    try:
        classified_text = analyze_python(source)
        encoded = build_html_page(classified_text, html=html, title=sourcefile)
    except Exception:
        return
    with open(destfile, 'w') as df:
        df.write(encoded)

def make_index_page(index):
    lines = [
        '<h2> Python Class Files </h2>\n',
        '<h5> Copyright (c) 2013 Raymond Hettinger </h5>\n',
        '<ul>\n',
    ]
    for htmlfile, sourcefile in sorted(index):
        line = '<li><a href="%s">%s</a></li>\n' % (htmlfile, sourcefile)
        lines.append(line)
    lines += ['</ul>\n']
    body = ''.join(lines)
    css = 'body {background-color:#F8FFFF;}'
    return index_html.format(title='FileIndex', css=css, html=html, body=body)

def publish(pubdir):
    try:
        os.mkdir(pubdir)
    except OSError:
        pass
    updates = 0
    index = []
    for sourcefile in glob.glob('*.py'):
        htmlfile = os.path.splitext(os.path.basename(sourcefile))[0] + '.html'
        destfile = os.path.join(pubdir, htmlfile)
        if not os.path.exists(destfile) or \
           os.stat(sourcefile).st_ctime > os.stat(destfile).st_ctime:
                print time.ctime(), 'Updating', sourcefile, '-->', destfile
                publish_one(sourcefile, destfile)
                updates += 1
        index.append((htmlfile, sourcefile))
    index_filename = os.path.join(pubdir, 'index.html')
    if updates or not os.path.exists(index_filename):
        print 'New index:', index_filename
        index_page = make_index_page(index)
        with open(index_filename, 'w') as f:
            f.write(index_page)
    return index_filename

if __name__ == '__main__':
    import sys, time

    print 'Starting in:', os.getcwd()
    pubdir = sys.argv[1] if len(sys.argv) == 2 else 'pub'
    print 'Writing to:', pubdir
    while True:
        publish(pubdir)
        time.sleep(3)
