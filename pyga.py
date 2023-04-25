#v1.2
import pygame
import math
from pygame import mixer
buttoncount=1
win=''
sx=0
sy=0
X=0
Y=0
Z=0
fov=0
viewdist=10
try:
      viewdist=viewdist*10
except:
      viewdist=viewdist
viewdistq=0
def getkey():
      for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_RSHIFT:
                        return 'rshift'
                  elif event.key == pygame.K_LSHIFT:
                        return 'lshift'
                  elif event.key == pygame.K_LALT:
                        return 'lalt'
                  elif event.key == pygame.K_RALT:
                        return 'ralt'
                  elif event.key == pygame.K_LCTRL:
                        return 'lctrl'
                  elif event.key == pygame.K_RCTRL:
                        return 'rctrl'
                  elif event.key == pygame.K_KP_ENTER:
                        return 'enter'
                  elif event.key == pygame.K_RETURN:
                        return 'enter'
                  elif event.key == pygame.K_BACKSPACE:
                        return 'backspace'
                  elif event.key == pygame.K_TAB:
                        return 'tab'
                  else:
                        return str(event.unicode)
            else:
                  return None
#import multitasking
#@multitasking.task
def get_type2(val):
      value=get_type(val)
      if('<Thread' not in value):
            return get_type2(val)
      else:
            return ''

def get_type(dur):
      toadd=''
      tyt=''
      h=0
      while(h<dur):
            toadd=str(getkey())
            if(toadd!='None'):
                  tyt+=(str(toadd)+',')
            else:
                  toadd=str(getkey())
                  if(toadd!='None'):
                        tyt+=(str(toadd)+',')
            h+=1
            #pygame.time.delay(1)
            continue
      toadd=''
      return tyt
def d3_init(StartPos,Quality,ViewDistance,Fov):
      global sx
      global sy
      global fov
      global X
      global Y
      global Z
      global viewdistq
      global viewdist
      global quality
      sx=int(sx/2)
      sy=int(sy/2)
      quality=Quality
      viewdistq=ViewDistance
      fov=Fov
      try:
            X=int(StartPos[0])
            Y=int(StartPos[1])
            Z=int(StartPos[2])
      except:
            error="Start Pos Needs 3 Numbers"
            raise error
def display_init(size,name="Pyga Window",resize=False,frame=True):
    global win
    global sx
    global sy
    sx=size[0]
    sy=size[1]
    if(frame==True):
          p=False
    else:
          p=pygame.NOFRAME
    pygame.init()
    if(resize==True):
        #if(__name__=="__main__"):
      win=pygame.display.set_mode((size), pygame.RESIZABLE,p)
    else:
        #if(__name__=="__main__"):
      win=pygame.display.set_mode((size),p)
    if(name!=False and name!=None):
        pygame.display.set_caption(name)
def state(size,flag):
    global win
    pygame.init()
    #if(__name__=="__main__"):
    win=pygame.display.set_mode((size),flags=flag)
def mixer_init():
    pygame.mixer.init()
def init_main(size,name,resize):
      display_init(size,name,resize)
      mixer_init()
def init_all(size,name,resize,StartPos,Quality,ViewDistance,Fov):
      display_init(size,name,resize)
      d3_init(StartPos,Quality,ViewDistance,Fov)
      mixer_init()
def rect(position,size,color,trans=None):
    s = pygame.Surface(size)
    if(trans!=False and trans!=None):
        s.set_alpha(255-trans)#+128)
    s.fill(color)
    win.blit(s, position)
def fill(color):
    win.fill(color)
def hide4():
      pygame.display.iconify()
def quit():
      try:
            try:
                  pygame.quit()
            except:
                  pass
            try:
                  pygame.mixer.quit()
            except:
                  pass
            try:
                  pygame.display.update()
            except:
                  pass
            try:
                  for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
            except:
                  pass
      except:
            pass
def pygam(pyg):
      exec("pygame."+pyg)
def update():
    global buttoncount
    global clicked
    pygame.display.update()
    buttoncount=-1
    clicked=None
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            try:
                  pygame.mixer.quit()
            except:
                  blank=""
            exit()
def nocloseupdate():
    global buttoncount
    global clicked
    pygame.display.update()
    buttoncount=-1
    clicked=None
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            return "close"
            blank=""
def text(tex,pos,color,size):
      try:
            font=pygame.font.Font('w95f.otf', size)
      except:
            try:
                  font=pygame.font.Font(r'C:\Windows\CustomFonts\w95f.ttf', size)
            except:
                  try:
                        font=pygame.font.Font('w95f.ttf', size)
                  except:
                        try:
                              font=pygame.font.Font('/home/pi/Desktopw95f.ttf', size)
                        except:
                              font = pygame.font.SysFont(None, size)
      img = font.render(str(tex), True, color)
      win.blit(img,pos)
clicked=0
pa=False
def mouse():
      try:
            mousee = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
      except:
            mousee=(0,0)
            click=False
      return mousee,click
def button(tex,pos,size,color):
    global clicked
    global pa
    global buttoncount
    #buttoncount=0#New?
    buttoncount+=1
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if(pos[0]+size[0] > mouse[0] > pos[0] and pos[1]+size[1] > mouse[1] > pos[1]):
        rect((pos[0]-2,pos[1]-2),(size[0]+4,size[1]+4),(100,100,255),0)
        rect((pos[0],pos[1]),(size[0],size[1]),color,0)
        if(click[0]==1):
            #clicked=buttoncount
            #buttoncount+=1
            clicked=buttoncount
        else:
            pa=False
    else:
        #rect(pos,size,color,0)
        rect((pos[0]-2,pos[1]-2),(size[0]+4,size[1]+4),(150,150,150),0)
        rect((pos[0],pos[1]),(size[0],size[1]),color,0)
    text(tex,(pos[0]+2,pos[1]+2),(0,0,0),20)
def line(start,end,color,width):
    pygame.draw.line(win,color,start,end,width)
def circle(pos,radius,color):
    pygame.draw.circle(win,color,pos,radius)
def orect(x,y,sx,sy,color,trans):
    rect((x,y),(sx,sy),color,trans)
def outline(x,y,sx,sy,thick,color):
    orect(x,y,thick,sy,color,0)
    orect((x+sx)-thick,y,thick,sy,color,0)
    orect(x,(y+sy)-thick,sx,thick,color,0)
    orect(x,y,sx,thick,color,0)
sd=''
def mouse():
      try:
            return (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],pygame.mouse.get_pressed()[0])
      except:
            return (0,0,False)
def getimg(place):
    try:
        return pygame.image.load(sd+'\\'+place+'.png')
    except:
        try:
           return pygame.image.load(place+'.png')
        except:
            try:
                try:
                    return pygame.image.load(sd+'\\'+place+'.jpg')
                except:
                    try:
                        return pygame.image.load(place+'.jpg')
                    except:
                        try:
                            return pygame.image.load(sd+'\\'+place+'.webp')
                        except:
                            try:
                                return pygame.image.load(place+'.webp')
                            except:
                                try:
                                   return pygame.image.load(sd+'\\'+place)
                                except:
                                    try:                                    
                                        return pygame.image.load(place)
                                    except:
                                        return None
            except:
                return None
def getani(dirrr):
    a=''
    b=''
    c=''
    d=''
    e=''
    f=''
    g=''
    h=''
    i=''
    j=''
    k=''
    dirr=dirrr
    try:
        a=getimg(dirr+'a')
    except:
        dirr=dirr+'\\'
        a=getimg(dirr+'a')
    try:
        b=getimg(dirr+'b')
        c=getimg(dirr+'c')
        d=getimg(dirr+'d')
        e=getimg(dirr+'e')
        f=getimg(dirr+'f')
        g=getimg(dirr+'g')
        h=getimg(dirr+'h')
        i=getimg(dirr+'i')
        j=getimg(dirr+'j')
        k=getimg(dirr+'k')
    except:
        blank=''
    return a,b,c,d,e,f,g,h,i,j,k
def image(img,pos,size,rotate,trans,flip):
    imge=pygame.transform.flip(img, flip[0], flip[1])
    imgo=pygame.transform.scale(imge,size)
    imgf=pygame.transform.rotate(imgo,rotate-90)
    s=imgf
    s.set_alpha(255-trans)
    win.blit(s, pos)
def getdisp_img(imgdir,pos,size,rotate,trans,flip):
    i=getimg(imgdir)
    image(i,pos,size,rotate,trans,flip)
def mixer_load_sound(s):
      return pygame.mixer.Sound(s)
def mixer_sound(obj):
      pygame.mixer.Sound.play(obj)
def mixer_load(directory):
    mixer.music.load(directory)
def mixer_unload():
    pygame.mixer.music.unload()
def mixer_play():
    pygame.mixer.music.play()
def mixer_play_obj(sound):
      pygame.mixer.music.play(sound)
def mixer_replay():
    pygame.mixer.music.rewind()
def mixer_pause():
    pygame.mixer.music.pause()
def mixer_unpause():
    pygame.mixer.music.unpause()
def mixer_volume(vol):
    pygame.mixer.music.set_volume(vol)
def mixer_stop():
    pygame.mixer.music.stop()
def mixer_busy():
    if(pygame.mixer.music.get_busy()==1):
        return True
    else:
        return False
def mixer_start(seconds):
    pygame.mixer.music.set_pos(seconds)
def mixer_get_time():
    return pygame.mixer.music.get_pos()


dx=-999
dy=-999
camx=0
camy=0
camz=0
color=(0,0,0)
def goto(x,y,z):
      global dx
      global dy
      try:
            if(dx==999 or dy==999):
                  dx=int(fov*((x+camx)/(z+camz)))
                  dy=int(fov*((y+camy)/(z+camz)))
            if(dx==-999 or dy==-999):
            #if(math.sqrt(((dx+sx)-int(fov*((x+camx)/(z+camz)))+sx)^2+((dy+sy)-int(fov*((y+camy)/(z+camz)))+sy)^2)>400):
                  dx=int(fov*((x+camx)/(z+camz)))
                  dy=int(fov*((y+camy)/(z+camz)))
            else:
                  if(dx!=-999 and dy!=-999):
                        if(dx<900 and dy<900):
                              if(15-int(((camz)/50)*10)>1):
                                    if(math.sqrt(((dx+sx)-int(fov*((x+camx)/(z+camz)))+sx)^2+((dy+sy)-int(fov*((y+camy)/(z+camz)))+sy)^2)<30):
                                          line((dx+sx,dy+sy),(int(fov*((x+camx)/(z+camz)))+sx,int(fov*((y+camy)/(z+camz)))+sy),color,15-int(((camz)/50)*10))
                                    else:
                                          dx=-999
                                          dy=-999
                              else:
                                    if(viewdistq!=False and viewdistq!=True):
                                          if(viewdist-int(((camz)/50)*10)>1):
                                                if(math.sqrt(((dx+sx)-int(fov*((x+camx)/(z+camz)))+sx)^2+((dy+sy)-int(fov*((y+camy)/(z+camz)))+sy)^2)<30):
                                                      line((dx+sx,dy+sy),(int(fov*((x+camx)/(z+camz)))+sx,int(fov*((y+camy)/(z+camz)))+sy),color,1)
                                    elif(viewdistq==True):
                                          if(150-int(((camz)/50)*10)>1):
                                                if(math.sqrt(((dx+sx)-int(fov*((x+camx)/(z+camz)))+sx)^2+((dy+sy)-int(fov*((y+camy)/(z+camz)))+sy)^2)<30):
                                                      line((dx+sx,dy+sy),(int(fov*((x+camx)/(z+camz)))+sx,int(fov*((y+camy)/(z+camz)))+sy),color,1)
                                    else:
                                          if(math.sqrt(((dx+sx)-int(fov*((x+camx)/(z+camz)))+sx)^2+((dy+sy)-int(fov*((y+camy)/(z+camz)))+sy)^2)<30):
                                                line((dx+sx,dy+sy),(int(fov*((x+camx)/(z+camz)))+sx,int(fov*((y+camy)/(z+camz)))+sy),color,1)
                              dx=-999
                              dy=-999
                        else:
                              dx=-999
                              dy=-999
                  else:
                        dx=int(fov*((x+camx)/(z+camz)))
                        dy=int(fov*((y+camy)/(z+camz)))
      except:
            dx=-999
            dy=-999
def objover_3d_wire():
      global dx
      global dy
      dx=-999
      dy=-999
      goto(0,0,0)
      goto(-20,20,0)
      goto(20,20,0)
      goto(20,-20,0)
      goto(-20,-20,0)
      goto(-20,20,0)
      goto(-20,20,-10)
      goto(-20,-20,-10)
      goto(-20,-20,0)
      goto(-20,-20,-10)
      goto(20,-20,-10)
      goto(20,20,-10)
      goto(-20,20,-10)
      goto(-20,20,-10)
      goto(-20,20,0)
      goto(20,20,0)
      goto(20,-20,0)
      goto(20,-20,-10)
      goto(20,20,-10)
      goto(-20,20,-10)
      goto(-20,-20,-10)
      goto(-20,-20,0)
      goto(-20,20,0)
      goto(20,20,0)
      goto(20,20,-10)
      goto(-20,20,-10)
      goto(-20,20,0)
      goto(0,0,0)
      dx=-999
      dy=-999
def objover_3d_fill():
      global dx
      global dy
      dx=-999
      dy=-999
      goto(0,0,0)
      goto(0,0,0)
      filly=15
      c=0
      while(c<35):
            goto(-20,filly,0)
            goto(20,filly,0)
            goto(0,0,0)
            dx=-999
            dy=-999
            filly-=1
            c+=1
      goto(0,0,0)
      filly=15
      c=0
      while(c<35):
            goto(-20,filly,-10)
            goto(20,filly,-10)
            goto(0,0,0)
            goto(0,0,0)
            dx=-999
            dy=-999
            filly-=1
            c+=1
      goto(0,0,0)
      filly=15
      c=0
      while(c<35):
            goto(20,filly,-10)
            goto(20,filly,0)
            goto(0,0,0)
            dx=-999
            dy=-999
            filly-=1
            c+=1
      goto(0,0,0)
      filly=15
      c=0
      while(c<35):
            goto(-20,filly,-10)
            goto(-20,filly,0)
            goto(0,0,0)
            dx=-999
            dy=-999
            filly-=1
            c+=1
      goto(0,0,0)
      filly=20
      c=0
      while(c<40):
            goto(filly,20,-10)
            goto(filly,20,0)
            goto(0,0,0)
            dx=-999
            dy=-999
            filly-=1
            c+=1
      goto(0,0,0)
      filly=20
      c=0
      while(c<40):
            goto(filly,-20,-10)
            goto(filly,-20,0)
            goto(0,0,0)
            dx=-999
            dy=-999
            filly-=1
            c+=1
      goto(-20,20,0)
      goto(0,0,0)
      goto(0,0,0)
      dx=-999
      dy=-999
def d3_cube(x,y,z,fillc,outc):
      global camx
      global camy
      global camz
      global color
      view=False
      if(viewdist!=False and viewdist!=True and viewdist!=None and viewdist!='' and viewdist!=' '):
            viewdista=viewdist
      elif(viewdist==False):
            viewdista=None
      else:
            viewdista=150
      camx=X+x
      camy=Y+(y/1.08)
      camz=Z+z
      if(camx>-300):
            if(camx<300):
                  if(camz>10):
                        if(viewdista!=None):
                              if(camz<viewdista):
                                    view=True
                              else:
                                    view=False
                        else:
                              view=True
                        if(view==True):
                              if(quality==4):
                                    color=fillc
                                    objover_3d_fill()
                                    color=outc
                                    objover_3d_wire()
                              if(quality==3):
                                    color=outc
                                    objover_3d_wire()
                                    color=fillc
                                    objover_3d_fill()
                              if(quality==2):
                                    color=fillc
                                    objover_3d_fill()
                              if(quality==1):
                                    color=outc
                                    objover_3d_wire()
