#!/usr/bin/env python
import argparse
import sys
import subprocess

params = {}

params['ip'] = {
    "regex": "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",
    "parameters": "-o -E",
    'source': "https://stackoverflow.com/questions/5284147/validating-ipv4-addresses-with-regexp/5284410#5284410",
    'desc': "grep ip from text"
}

params['ipwithline'] = {
    "regex": "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",
    "parameters": "-E",
    'source': "https://stackoverflow.com/questions/5284147/validating-ipv4-addresses-with-regexp/5284410#5284410",
    'desc': "grep ipwithline from text"
}

params['url'] = {
    "regex": "\\b(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]*[-A-Za-z0-9+&@#/%=~_|]",
    "parameters": "-E -o",
    'source': 'http://linux-and-mac-hacks.blogspot.com.tr/2013/04/use-grep-and-regular-expressions-to.html',
    'desc': 'grep url from text'
}

params['email'] = {
    "regex" : "\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\\b",
    "parameters": "-E -o",
    "source" : "-",
    "desc" : "grep email from text"
}

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('word', help='grep word', choices=params.keys())
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='filename, default stdin')


def read_args():
    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)
    args=parser.parse_args()
    return args


def createCommand(args):
    grepCommand = ["grep"]
    grepCommand.extend((params[args.word]['parameters'].split()))
    grepCommand.append(params[args.word]['regex'])
    if args.infile.name != '<stdin>':
        grepCommand.append(args.infile.name)
    return filter(None,grepCommand)


def runCommand(command):
    #print command
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode == 0 and err != '':
        print("failed %s" % err)
    print out,


if __name__ == '__main__':
    args = read_args()
    runCommand(createCommand(args))

