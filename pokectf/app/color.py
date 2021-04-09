
import math
import random



def floatBetween (a, b):
  if (not a): a = 0
  if (not b): b = 1
  return a + ((b - a) * random.random())


def hsvToRgb(h, s, v):
  if s == 0.0: return (v, v, v)
  i = int(h*6.) # XXX assume int() truncates!
  f = (h*6.)-i; p,q,t = v*(1.-s), v*(1.-s*f), v*(1.-s*(1.-f)); i%=6
  if i == 0: return (v, t, p)
  if i == 1: return (q, v, p)
  if i == 2: return (p, v, t)
  if i == 3: return (p, q, v)
  if i == 4: return (t, p, v)
  if i == 5: return (v, p, q)

# hsv here is 360, 1.0, 1.0
def hsvToRgbdio(h, s, v):
  c = s * v
  temp = h / 60
  x = c * (1.0 - abs((temp % 2) - 1))
  m = v - c

  r , g, b = 0,0,0
  if (0 <= h and h < 60):
    r = c
    g = x
    b = 0
  elif (60 <= h and h < 120):
    r = x
    g = c
    b = 0
  elif (120 <= h and h < 180):
    r = 0
    g = c
    b = x
  elif (180 <= h and h < 240):
    r = 0
    g = x
    b = c
  elif (240 <= h and h < 300):
    r = x
    g = 0
    b = c
  else:
    r = c
    g = 0
    b = x

  r = r + m
  g = g + m
  b = b + m

  return [ r, g, b ]

def rgbToHsv(r, g, b):
  r = r/255
  g = g/255
  b = b/255
  mmin = min(r, g, b)
  mmax = max(r, g, b)
  v = mmax
  delta = mmax - mmin
  h, s = 0, 0

  # darkness is an edge case
  if (mmax <= 0 or delta < 0.0001):
    return [0, 0, v]

  s = delta / mmax
  if (r == mmax):
    h = (g - b) / delta
  elif (g == mmax):
    h = 2 + (b - r) / delta
  else:
    h = 4 + (r - g) / delta

  h *= 60
  if (h < 0): h += 360

  return [h, s, v]

def fromHexNotation(hex):
  if (hex.startswith('#')):
    hex = hex[1:]
  r = int(hex[0:2], 16)
  g = int(hex[2:4], 16)
  b = int(hex[4:6], 16)
  return [r, g, b]


def toHexNotation(r, g, b):
  r = "{0:0{1}x}".format(math.floor(r * 255), 2)
  g = "{0:0{1}x}".format(math.floor(g * 255), 2)
  b = "{0:0{1}x}".format(math.floor(b * 255), 2)
  return '#' + r + g + b

def randomPrimary():
  # h = ((random.random() * 240) + 340) % 360
  h = ((random.random() * 200) + 20) % 360
  s = floatBetween(0.1, 0.5)
  v = floatBetween(0.6, 0.8)
  return [ h, s, v ]

def generateFullScheme(h, s, v):

  prim = toHexNotation(*hsvToRgb(h, s, v))

  hintV = v + 0.6
  if (hintV > 1): hintV = 1
  hintS = s + 0.23
  if (hintS > 1): hintS = 1
  hint = toHexNotation(*hsvToRgb((h + 330) % 360, hintS, hintV))

  grime = toHexNotation(*hsvToRgb(h, 1, v))

  wall = toHexNotation(*hsvToRgb((h + 40) % 360, floatBetween(s, 0.4), floatBetween(0.05, 0.2)))
  # value = floatBetween(0.0, 0.1)
  # print(value)
  # wall = toHexNotation(*hsvToRgb(300, 0, value))
  # print(wall)

  return [prim, hint, grime, wall]

def variation(h, s, v):
  h += math.floor(floatBetween(0,40))
  s += floatBetween(0, 0.05)
  v += floatBetween(0, 0.05)
  h = (h + 360) % 360
  s = min(1, max(v, 0))
  v = min(1, max(v, 0))
  return [h, s, v]

def randomScheme():
  return generateFullScheme(*randomPrimary())

def schemeFromHex(hex):
  return generateFullScheme(*variation(*rgbToHsv(*fromHexNotation(hex))))

def gen_colors():
  c = randomScheme()

  def anglediff(a1, a2):
    return 180 - abs(abs(a1 - a2) - 180); 

  wanted_hue = rgbToHsv(*fromHexNotation(c[2]))[0]
  best, bestvalue = 99999999, 99999999999
  for fname, color in poke_color.items():
    if anglediff(wanted_hue, color) < best:
      best = anglediff(wanted_hue, color)
      selected = fname

  return [*c, selected.split("_")[0]]





import os, math
directory = "app/templates/banners/"
selected = "poke23_0.html"
poke_color = {}
for filename in os.listdir(directory):
  if ".html" not in filename:
    continue
  with open(directory + filename, "r") as f:
    t = f.read()
    rgbs = t.split("color:#")[1:]
    lengths = []
    for line in rgbs:
      i, j = line.find(">"), line.find("<")
      lengths += [j - i - 1]
    t = list(map(lambda x: x.split(";")[0], rgbs))
    tt = [[int(x[:2],16),int(x[2:4],16),int(x[4:],16)] for x in t]
    hh, ss, vv = [], [], []
    sk = []
    for length, t in zip(lengths, tt):
      h, s, v = rgbToHsv(t[0], t[1], t[2])
      if s < 0.10:
        continue
      hh += [h]*length
      ss += [s]*length
      vv += [v]*length
      sk += [(h*s*v, h)]*length


    x = list(map(lambda x: math.cos(x*3.1415/180), hh))
    y = list(map(lambda x: math.sin(x*3.1415/180), hh))

    def median(a):
      # return sorted(a)[len(a)//2]
      return sum(a)/len(a)

    angle = math.atan2(median(y), median(x))*180.0 / 3.1415
    final = angle if angle > 0 else angle + 360.0
    poke_color[filename] = final
    # poke_color[filename] = sorted(sk)[len(sk)//2][1]
