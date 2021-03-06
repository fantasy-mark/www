#coding=utf-8
#!/usr/bin/env python

import sys
import os


#####################################################################
#                            Deal with single file
#####################################################################
def deal_file(path, filename):
    mark = ''
    filepath=[]
    print '</br>' * 8
    print '<h1 align="center"><a name="%s"> %s </a></h1>' \
			% (filename.replace('.txt', ''), filename.replace('.txt', ''))

    # the mothod to join 2 strings
    filepath.append(filename)
    fp = open(path.join(filepath), "r")

    for eachline in fp:
        '''
        fixme the Character Entities
        '''
        eachline = eachline.replace('&', '&amp;')
        eachline = eachline.replace('<', '&lt;')
        eachline = eachline.replace('>', '&gt;')
        eachline = eachline.replace('"', '&quot;')
        eachline = eachline.replace('	', '&nbsp;&nbsp;&nbsp;&nbsp;')

        if eachline.find('@author') != -1:
            print '%s' % (mark)
            print '<address>'
            mark = '</address>\n'

        elif eachline.find('@title') != -1:
            print '%s' % (mark)
            print '<h2>'
            mark = '</h2>\n'

        elif eachline.find('@text') != -1:
            print '%s' % (mark)
            print '<pre class="text-style">'
            mark = '</pre>\n'

        elif eachline.find('@code') != -1:
            print '%s' % (mark)
            print '<pre class="code-style">'
            mark = '</pre>\n'

        elif eachline.find('@picture') != -1:
            print '%s' % (mark)
            print '<img src="'
            mark = '@picture'

        elif eachline.find('@link') != -1:
            print '%s' % (mark)
            print '<a href="'
            mark = '@link'

        elif eachline.find('@item') != -1:
            print '%s' % (mark)
            print '<li>'
            mark = '</li>\n'

        elif eachline.find('@emphasize') != -1:
            print '%s' % (mark)
            print '<strong>'
            mark = '</strong>\n'

        else:
            if mark == '':
                print '<pre class="text-style">'
                mark = '</pre>\n'

            if mark == '@link':
                print '%s">' % (eachline)

            # logic -- if no label for this line then print the content
            print eachline,

            if mark == '@picture':
                print '"/>'
                mark = ''
	
            if mark == '@link':
                print '</a>'
                mark = ''

    print '%s' % (mark)

    fp.close()


#####################################################################
#                            Deal with project
#####################################################################
def text2html(path):
    index = 0

    if not os.path.isdir(path):
        return False

    print '</br>' * 4

    for filename in os.listdir(path):
        if filename != 'Makefile':
            print '<div class="title"><a href="#%s"> %d : %s </a></div>' \
					% (filename.replace('.txt', ''), index, filename.replace('.txt', ''))
            index += 1

    print '</br>' * 8

    for filename in os.listdir(path):
        if filename != 'Makefile':
			deal_file(path, filename)


#####################################################################
#                            Begin of main function
#####################################################################
#fp = open(sys.argv[1], 'r')
#
#for eachline in fp:
#    if eachline == '' or eachline == '\n':
#        continue
if __name__ == "__main__":
    text2html(sys.argv[1])

