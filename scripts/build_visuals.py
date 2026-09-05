"""Build the profile's original, self-contained SVG identity. Python standard library only."""
from pathlib import Path
from math import sin,cos,pi
from html import escape

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets'
OUT.mkdir(exist_ok=True)

def text(x,y,s,size=24,fill='#f0efe6',weight=400,extra=''):
 return f'<text x="{x}" y="{y}" fill="{fill}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" {extra}>{escape(s)}</text>'

def circle(x,y,r,fill,extra=''):
 return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{fill}" {extra}/>'

def line(x1,y1,x2,y2,col='#58615a',w=1,extra=''):
 return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{col}" stroke-width="{w}" {extra}/>'

def svg(w,h,title,body):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><style>@media(prefers-reduced-motion:reduce){{.motion{{display:none}}}}</style>{body}</svg>'''

def art(kind,col,muted):
 p=[]
 if kind=='cosmos':
  for rx,ry,rotation in [(133,47,-23),(124,70,25),(84,105,55)]:
   p.append(f'<ellipse cx="679" cy="127" rx="{rx}" ry="{ry}" transform="rotate({rotation} 679 127)" fill="none" stroke="{muted}" stroke-width="1.2"/>')
  for i in range(21):
   a=i*2.39996;r=23+(i*19)%103;x=679+cos(a)*r;y=127+sin(a)*r*.75
   p.append(line(679,127,x,y,muted,.7));p.append(circle(x,y,2+(i%3),col))
  p.append(circle(679,127,12,col));p.append(circle(679,127,22,'none',f'stroke="{col}" opacity=".3"'))
  p.append(f'<circle class="motion" r="4" fill="{col}"><animateMotion dur="14s" repeatCount="indefinite" path="M546,127 A133,47 0 1 0 812,127 A133,47 0 1 0 546,127"/></circle>')
 elif kind=='terraform':
  for i in range(3):
   y=50+i*46
   p.append(f'<path d="M556 {y+42} L679 {y} L809 {y+42} L679 {y+87} Z" fill="none" stroke="{col if i==0 else muted}" stroke-width="2"/>')
  for x in [556,679,809]:p.append(line(x,92 if x!=679 else 137,x,184 if x!=679 else 229,muted,1,'stroke-dasharray="4 6"'))
  p.append(circle(679,50,5,col));p.append(line(679,24,679,50,col,2))
 elif kind=='nua':
  p.append(f'<rect x="550" y="39" width="255" height="154" rx="8" fill="none" stroke="{muted}" stroke-width="1.5"/>')
  p.append(f'<path d="M650 79 L650 141 L698 110 Z" fill="{col}"/>')
  for i in range(37):
   x=554+i*7;h=7+abs(sin(i*.65)*sin(i*.2))*39
   p.append(line(x,216-h/2,x,216+h/2,col,3))
 else:
  pts=[(573,123),(616,57),(693,57),(735,123),(694,190),(616,190),(801,82)]
  for a,b in [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(3,6),(1,4),(0,3)]:p.append(line(*pts[a],*pts[b],muted,2))
  for i,(x,y) in enumerate(pts):p.append(circle(x,y,12 if i%2 else 7,col));p.append(circle(x,y,20,'none',f'stroke="{muted}" stroke-width="1"'))
  p.append(f'<circle class="motion" r="4" fill="{col}"><animateMotion dur="10s" repeatCount="indefinite" path="M573 123 L616 57 L693 57 L735 123 L694 190 L616 190 Z"/></circle>')
 return ''.join(p)

cards=[
 ('cosmos','01','AI / INTERACTIVE EXPLAINER','The Token Cosmos',['Make token probabilities visible.','Explore how sampling changes the output.'],'REACT  /  TYPESCRIPT  /  FASTAPI',False),
 ('terraform','02','CLOUD / LEARNING SYSTEM','Terraform Mastery',['Understand infrastructure from first principles.','Predict. Run the lab. Verify the result.'],'TERRAFORM  /  LINUX  /  LOCAL LABS',True),
 ('nua','03','SOFTWARE / MULTILINGUAL LEARNING','Nua',['Make technical lectures more accessible.','Translation, dubbing, synchronized playback.'],'ANDROID  /  TYPESCRIPT  /  AUDIO',True),
 ('discovery','04','SCIENCE / RESEARCH PROTOTYPE','Discovery Intelligence',['Explore molecular screening workflows.','Validate data. Rank candidates. Review evidence.'],'PYTHON  /  RDKIT  /  FASTAPI',False),
]
for key,num,label,title,desc,stack,light in cards:
 bg='#eeede5' if light else '#141917';fg='#18211b' if light else '#f0efe6';muted='#69766a' if light else '#8d9a90';accent='#385d28' if light else '#d2f76b';rule='#c4cbc0' if light else '#364139'
 b=f'<rect x="1" y="1" width="878" height="498" rx="18" fill="{bg}" stroke="{rule}"/>'
 b+=text(38,49,label,18,muted,600,'letter-spacing="2"')
 b+=text(36,161,num,105,accent,400,'letter-spacing="-7"')
 b+=art(key,accent,rule)
 b+=text(38,290,title,44,fg,600,'letter-spacing="-1.5"')
 for i,s in enumerate(desc):b+=text(40,339+i*34,s,25,muted)
 b+=line(40,413,838,413,rule)
 b+=text(40,455,stack,18,fg,500,'letter-spacing="1.1"')
 b+=f'<path d="M796 452 h30 m-12 -12 12 12 -12 12" fill="none" stroke="{accent}" stroke-width="2"/>'
 (OUT/f'{key}.svg').write_text(svg(880,500,title+' — '+'. '.join(desc),b))

b='<rect width="1800" height="190" rx="16" fill="#141917"/>'
b+=text(46,51,'THE WORKING METHOD',20,'#98a498',600,'letter-spacing="3"')
for i,(title,sub) in enumerate([('BUILD','Make the idea concrete.'),('TEST','Measure what actually happens.'),('UNDERSTAND','Explain the mechanism.')]):
 x=46+i*586
 b+=text(x,107,title,40,'#d2f76b',600,'letter-spacing="-1"')+text(x,148,sub,23,'#d6dbd0')
 if i<2:b+=f'<path d="M{x+440} 102 h70 m-12 -12 12 12 -12 12" fill="none" stroke="#73816e" stroke-width="2"/>'
(OUT/'method.svg').write_text(svg(1800,190,'Build. Test. Understand. Make the idea concrete, measure what happens, and explain the mechanism.',b))

b='<rect width="1800" height="86" rx="12" fill="#d2f76b"/>'
b+=text(36,55,'THOKCHOM LOLET SINGH',25,'#18211b',600,'letter-spacing="2"')
b+=text(1040,55,'SYSTEMS FIRST. SCIENCE AHEAD.',24,'#18211b',400,'letter-spacing="2"')
(OUT/'signature.svg').write_text(svg(1800,86,'Thokchom Lolet Singh — Systems first. Science ahead.',b))
print('Generated 4 illustrated project cards, method strip, and signature.')

# Compact compositions selected by README picture sources at narrow viewports.
mobile_titles={'cosmos':['The Token','Cosmos'],'terraform':['Terraform','Mastery'],'nua':['Nua',''],'discovery':['Discovery','Intelligence']}
mobile_desc={'cosmos':['LLM sampling','visualizer'],'terraform':['Infrastructure','from first principles'],'nua':['Lecture translation','& dubbing'],'discovery':['Molecular screening','research prototype']}
for key,num,label,title,desc,stack,light in cards:
 bg='#eeede5' if light else '#141917';fg='#18211b' if light else '#f0efe6';muted='#69766a' if light else '#a8b3aa';accent='#385d28' if light else '#d2f76b';rule='#c4cbc0' if light else '#364139'
 b=f'<rect x="1" y="1" width="438" height="498" rx="20" fill="{bg}" stroke="{rule}"/>'
 b+=text(26,88,num,70,accent,400)
 b+=f'<g transform="translate(-193,25) scale(.7)">{art(key,accent,rule)}</g>'
 for i,s in enumerate(mobile_titles[key]):b+=text(26,261+i*49,s,42,fg,600,'letter-spacing="-1"')
 for i,s in enumerate(mobile_desc[key]):b+=text(27,372+i*32,s,26,muted)
 b+=line(26,433,412,433,rule)+text(27,474,'VIEW SOURCE',23,accent,600)
 b+='<path d="M366 466 h34 m-12 -12 12 12 -12 12" fill="none" stroke="'+accent+'" stroke-width="2"/>'
 (OUT/f'{key}-mobile.svg').write_text(svg(440,500,title+' — '+'. '.join(mobile_desc[key]),b))
b='<rect width="600" height="320" rx="18" fill="#141917"/>'
b+=text(25,45,'THE WORKING METHOD',20,'#98a498',600,'letter-spacing="2"')
for i,(title,sub) in enumerate([('BUILD','Make it concrete.'),('TEST','Measure the result.'),('UNDERSTAND','Explain the mechanism.')]):
 y=107+i*84;b+=text(25,y,title,31,'#d2f76b',600)+text(25,y+29,sub,24,'#d6dbd0')
(OUT/'method-mobile.svg').write_text(svg(600,320,'Build. Test. Understand.',b))
