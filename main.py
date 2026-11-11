import json,os
import urllib.request as rq
U=os.environ["MAKEFUN_ENV_URL"]
Y=(0,100,320,330,500,900,0)
T=("KKKKMPPAMIFKKKKUMMPWPPUZddddKKKK","27<<7AKM<MPR<KRU","AFFFFMKKFPPPFKPP","KKKMIKKKIKKKIKKK","AFFIFKMKFMMMKKMM","UZPKUUKKFAAAA<<7<772<772<772<772")
P=[[ord(c)-75 for c in t]for t in T]
V=("_a","A?","^boq/1>B","_aA?","Q`O@","Q`O@_aA?","Q_`aOA@?")
B=[0]*128
W=0;E=-1;KW=4;KB=116;Z=[];TT={};ND=0;BG=50000
class X(Exception):pass
M=lambda f,t,p=0,l=0:f|t<<7|p<<14|l<<17
def A(s,b):
 for t in((0 if b else 1),2,6,4,3):
  for o in V[t]:
   o=ord(o)-80;a=s+o
   while not a&136:
    p=B[a]
    if p:
     if(p<9)==(b==0)and(p&7==(t or 1)or(p&7==5 and t>2)):return 1
     break
    if t!=3 and t!=4:break
    a+=o
 return 0
def G(c=0):
 m=[]
 for s in range(128):
  if s&136:continue
  p=B[s]
  if not p or not(p<9)^W:continue
  t=p&7
  if t==1:
   d=16-32*W;y=(s>>4)==6-5*W
   for o in(d,d-1,d+1):
    a=s+o
    if a&136:continue
    q=B[a]
    if o==d:
     if q:continue
     if y:m.append(M(s,a,5))
     elif not c:
      m.append(M(s,a))
      if(s>>4)==1+5*W and not B[s+d*2]:m.append(M(s,s+d*2,0,1))
    elif q and not(q<9)^W:
     if y:m.append(M(s,a,5))
     else:m.append(M(s,a))
    elif a==E:m.append(M(s,a,0,2))
  else:
   for o in V[t]:
    o=ord(o)-80;a=s+o
    while not a&136:
     q=B[a]
     if q:
      if not(q<9)^W:m.append(M(s,a))
      break
     if not c:m.append(M(s,a))
     if t==2 or t==6:break
     a+=o
 return m
def K(m):
 global B,W,E,KW,KB
 Z.append((B,W,E,KW,KB))
 nb=B[:]
 f=m&127;t=(m>>7)&127;r=(m>>14)&7;l=(m>>17)&15;p=nb[f]
 if l&2:nb[t-16+32*W]=0
 nb[t]=r+8*W if r else p
 nb[f]=0
 if p==6:KW=t
 elif p==14:KB=t
 E=(f+t)//2 if l&1 else-1
 W^=1
 B=nb
def J():
 global B,W,E,KW,KB
 B,W,E,KW,KB=Z.pop()
def F():
 s=0
 for q in range(128):
  if q&136:continue
  p=B[q]
  if not p:continue
  t=p&7;u=p<9;j=min(q&7,7-(q&7));r=(q>>4)if u else 7-(q>>4)
  if t!=1 and t!=6:r=min(r,7-r)
  v=Y[t]+P[t-1][r*4+j]
  s+=v if u else-v
 return s if not W else-s
def O(m):
 t=(m>>7)&127;c=B[t]
 return 100+Y[c&7]*10 if c else 0
def S(d,a,b,pl):
 global ND
 ND+=1
 if ND>=BG:raise X
 if d<=0:
  if A(KW if not W else KB,1-W):q=2
  else:
   s=F()
   if s>=b:return s
   if s>a:a=s
   q=1
 else:
  q=0
  k=(bytes(B),W,E)
  e=TT.get(k)
  if e and e[0]>=d and(e[1]>=b if e[2]==1 else e[1]<=a if e[2]==2 else 1):return e[1]
 ms=G(1)if q==1 else G()
 ms.sort(key=O,reverse=True)
 be=-1000000;a0=a
 for m in ms:
  K(m)
  if A(KW if W else KB,W):J();continue
  s2=-S(d-1,-b,-a,pl+1)
  J()
  if s2>be:be=s2
  a=max(a,s2)
  if a>=b:break
 if be==-1000000:
  if q==2:return -100000+pl
  if not q:return -100000+pl if A(KW if not W else KB,1-W)else 0
 if not q:
  TT[k]=(d,be,0 if a0<be<b else 1 if be>=b else 2)
  if len(TT)>65536:TT.clear()
  return be
 return a
def R(d,ms):
 be=-1000000;bm=ms[0];a=-1000000
 for m in ms:
  K(m);s=-S(d-1,-1000000,-a,1);J()
  if s>be:be=s;bm=m
  a=max(a,s)
 return bm
def O2(m):
 f=m&127;t=(m>>7)&127;r=(m>>14)&7
 return chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)+("nbrq"[r-2]if r else"")
def D(f):
 global W,E,KW,KB
 B[:]=[0]*128
 p=f.split();i=112
 for ch in p[0]:
  if ch.isdigit():i+=int(ch)
  elif ch=='/':i-=24
  else:
   q="PNBRQK".index(ch.upper())+1
   if ch.islower():q+=8
   B[i]=q
   if q==6:KW=i
   elif q==14:KB=i
   i+=1
 W=p[1]!="w"
 E=(ord(p[3][0])-97)+(ord(p[3][1])-49)*16 if p[3]!="-"else-1
def H(lm):
 global ND
 lg=[m for m in G()if(K(m),not A(KW if W else KB,W),J())[1]]
 if not lg:return None
 lg.sort(key=O,reverse=True)
 ND=0
 be=lg[0]
 for d in range(1,9):
  try:be=R(d,lg)
  except X:break
 u=O2(be)
 return u if u in lm else lm[0]
def p(a,b):
 try:
  with rq.urlopen(U+a,json.dumps(b).encode())as r:return json.load(r)
 except:return{"error":1}
def main():
 g=p("/game",{})
 while g.get("status")!="done":
  if"error"in g:break
  if g.get("status")=="your_move":
   D(g["fen"]);u=H(g["legal_moves"])
   if not u:break
   q={"game":g["game"],"move":u};r=p("/move",q)
   if"error"in r:q["move"]=g["legal_moves"][0];r=p("/move",q)
   g=r
  else:g=p("/game",{})
main()
