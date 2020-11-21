''' Keyword searchable document database

API:

    create_db(force=False)
    add_document(uri, document)
    get_document(uri) --> document
    document_search(keyword0, keyword1, ...) --> [uri0, ur1, ...]  # sorted by relevance

    Exceptions:  UnknownURI, DuplicateURI

Database schema:

    characters                 documents
    -------------              --------------
    index by word              index by uri
    -------------              --------------
    uri      text              uri       text
    word     text              document  blob
    relfreq  real

'''

from __future__ import division
from contextlib import closing
import os, re, collections, sqlite3, bz2

__all__ = ['create_db', 'add_document', 'get_document', 'document_search',
           'UnknownURI', 'DuplicateURI']

database = 'pepsearch.db'

class UnknownURI(KeyError):
    'This URI is not in the database'
    pass

class DuplicateURI(ValueError):
    'A URI needs to be unique and we already have one'
    pass

stoplist = {'and', 'of', 'or', 'the'}

def normalize(words):
    '''Improve comparability by stripping plurals and lowercasing

        normalize(['Hettinger', 'Enumerates'])  -->  ['hettinger', 'enumerate']

    '''
    wordlist = [word.lower().rstrip('s') for word in words]
    return [word for word in wordlist if word not in stoplist]

def characterize(uri, text, n=200):
    'Scan text and return relative frequencies of the n most common words'
    # return list of tuples in the form: (uri, word, relative_frequency)
    words = re.findall(r"[A-Za-z']+", text)
    words = normalize(words)
    counts = collections.Counter(words).most_common(n)
    total = sum([count for word, count in counts])
    return [(uri, word, count/total) for word, count in counts]

def create_db(force=False):
    'Set-up a new characterized document database, eliminating an old one if it exists'
    if force:
        try:
            os.remove(database)
        except OSError:
            pass
    with closing(sqlite3.connect(database)) as conn:
        c = conn.cursor()
        c.execute('CREATE TABLE documents (uri text, document blob)')
        c.execute('CREATE TABLE characters (uri text, word text, relfreq real)')
        c.execute('CREATE UNIQUE INDEX UriIndex ON documents (uri)')
        c.execute('CREATE INDEX WordIndex ON characters (word)')

def add_document(uri, text):
    'Add a document with a given identifier to the search database'
    characters = characterize(uri, text)
    with closing(sqlite3.connect(database)) as conn:
        c = conn.cursor()
        btext = sqlite3.Binary(bz2.compress(text))
        try:
            c.execute('INSERT INTO documents VALUES (?, ?)', (uri, btext))
        except sqlite3.IntegrityError:
            raise DuplicateURI(uri)
        c.executemany('INSERT INTO characters VALUES (?, ?, ?)', characters)
        conn.commit()
    
def get_document(uri):
    'Retrieve a document with a given URI.'
    with closing(sqlite3.connect(database)) as conn:
        c = conn.cursor()
        t = (uri,)
        c.execute('SELECT document FROM documents WHERE uri=?', t)
        row = c.fetchone()
        if row is None:
            raise UnknownURI(uri)
        return bz2.decompress(row[0])

search_query_template = '''
SELECT uri
FROM characters
WHERE word IN (%s)
GROUP BY uri
ORDER BY SUM(relfreq) DESC
'''
    
def document_search(*keywords):
    'Find ranked list of best matched URIs for a given keyword'
    keywords = normalize(keywords)
    questions = ', '.join(['?'] * len(keywords))
    search_query = search_query_template % questions
    with closing(sqlite3.connect(database)) as conn:
        c = conn.cursor()
        c.execute(search_query, keywords)
        rows = c.fetchall()
    return [uri for uri, in rows]


############################################################
###  Test harness code follows  ############################

if __name__ == '__main__':
    import pprint

    docdir = 'peps'

    if 0:
        print normalize(['Hettinger', 'enumerates'])

    if 0:
        filename = 'pep-0238.txt'
        fullname = os.path.join(docdir, filename)
        with open(fullname) as f:
            text = f.read()
        uri = os.path.splitext(filename)[0]
        c = characterize(uri, text)
        pprint.pprint(c)

    if 0:
        create_db(force=True)

    if 0:
        #for filename in ['pep-0237.txt', 'pep-0236.txt', 'pep-0235.txt']:
        for filename in os.listdir(docdir):
            fullname = os.path.join(docdir, filename)
            with open(fullname, 'rb') as f:
                text = f.read()
            uri = os.path.splitext(filename)[0]
            print uri, len(text)
            add_document(uri, text)

    if 0:
        print get_document('pep-0237')[:100]

    if 0:
        pprint.pprint(document_search('zip', 'barry')[:100])
