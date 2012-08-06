# -*- coding: utf-8 *-*
import sys
sys.path.append('./lib')

import cherrypy
from asciidocapi import AsciiDocAPI
import StringIO

class AsciiPage(object):
    def blog(self, page='index'):
        asciidoc = AsciiDocAPI()
        outfile = StringIO.StringIO()
        asciidoc.execute('pages/%s.txt'%page, outfile, backend='html5')
        return outfile.getvalue()

    blog.exposed = True

if __name__ == '__main__':
    cherrypy.quickstart(AsciiPage())

