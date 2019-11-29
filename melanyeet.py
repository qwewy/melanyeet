#!/usr/bin/python3
import subprocess
import tempfile
import sys
import os

DEFAULT_TEXT="brother %s, looking correct!" % os.environ['USER']

def get_text_bubble(inputStr=None):
  fp = tempfile.TemporaryFile()
  cmd = 'cowsay -f {}/blank.cow '.format(os.path.dirname(os.path.realpath(__file__)))
  stdinput=""
  
  if inputStr != None:
    cmd += DEFAULT_TEXT
  else:
    cmd += " ".join(sys.argv[1:])
  p = subprocess.call(cmd, stdin=sys.stdin, stdout=fp, shell=True)
  
  fp.seek(0)
  s = fp.readlines()
  fp.close()
  return [ line.decode('utf-8') for line in s ]

def get_melanyeet():
  with open(os.path.dirname(os.path.realpath(__file__)) + '/melanyeet.cow') as f:
    lines = f.readlines()
    for i in range(len(lines)):
      line = lines[i]
    return lines

def combine(textbubble, melanyeet):
    targetRow = 16
    textRows = len(textBubble)
    topHalf = textRows // 2
    botHalf = textRows - topHalf

    if (targetRow - topHalf >= 0 and targetRow + botHalf < len(melanyeet)):
      for i in range(targetRow - topHalf, targetRow + botHalf):
        j = i - (targetRow - topHalf)
        melanyeet[i] = melanyeet[i][:-1] + textbubble[j].rstrip() + "\n"
    else:
      melanyeet = [" "*41 for _ in range(len(textbubble) - len(melanyeet))] + melanyeet
      for i in range(0, len(textbubble)):
        melanyeet[i] = melanyeet[i][:-1] + textbubble[i].strip() + "\n"
    return "".join(melanyeet)


if __name__ == "__main__":
  textBubble = get_text_bubble(DEFAULT_TEXT) if len(sys.argv) > 1 and sys.argv[1] == "--brother" else get_text_bubble()
  melanyeet = get_melanyeet()
  output = combine(textBubble, melanyeet)
  print(output)
