if 0:
    allNames = {}
    for f in AllFonts():
    
        if 'Bitcount_Grid_Double.ufo' in f.path:
            for g in f:
                aNames = []
                for a in g.anchors:
                    aNames.append(a.name)
                allNames[g.name] = sorted(aNames)
        else:
            for g in f:
                if g.name not in allNames:
                    aNames = []
                    for a in g.anchors:
                        aNames.append(a.name)
                    allNames[g.name] = sorted(aNames)

    for f in AllFonts():
        for g in f:
            aNames = []
            for a in g.anchors:
                aNames.append(a.name)
            if sorted(allNames[g.name]) != sorted(aNames):
                print(g.name, sorted(allNames[g.name]), sorted(aNames), f.path.split('/')[-1])
                g.clearAnchors()
                for aName in allNames[g.name]:
                    g.appendAnchor(aName, (0, 0))
        f.save()
        
from math import *

def findRomanAnchor(g, a):
    if 'Italic' in g.font.path:
        for f in AllFonts():
            if f.path == g.font.path.replace('-Italic', ''):
                gr = f[g.name]
                for ar in gr.anchors:
                    if a.name == ar.name:
                        return ar
    return a
    
for f in AllFonts():
    for g in f:
        if 'comb' not in g.name:
            for a in g.anchors:
                if '_' in a.name:
                    print('######', g.name, a.name)
        #if g.name != 'a':
        #    continue            
        if g.components or g.contours:
            x1, y1, x2, y2 = g.bounds
            #x1 = x1 - y1*tan(radians(-g.font.info.italicAngle or 0))
            #x2 = x2 - y2*tan(radians(-g.font.info.italicAngle or 0))
            for a in list(g.anchors):    
                ar = findRomanAnchor(g, a)
                if ar is not a:
                    y = ar.y
                    x = int(round(ar.x + y*tan(radians(-g.font.info.italicAngle or 0)))) - 14/2/2
                    if (x, y) != (a.x, a.y):
                        a.x = x
                        a.y = y
                        print(g.name, 'From roman-', a.name, x, y, x1, y1, x2, y2)
                        g.changed()
                                    
                elif a.name == 'bottom':
                    if 'Prop' in f.path:
                        y = y1
                        x = int(round(x1 + int((x2 - x1)/100/2) * 100 + y*tan(radians(-g.font.info.italicAngle or 0))))
                        if (x, y) != (a.x, a.y):
                            a.x = x
                            a.y = y
                            print(g.name, 'Prop-bottom', x, y, x1, y1, x2, y2)
                            g.changed()
                    elif 'Mono' in f.path:
                        y = y1
                        x = int(round(x1 + int((x2 - x1)/100/2) * 100 + y*tan(radians(-g.font.info.italicAngle or 0))))
                        if (x, y) != (a.x, a.y):
                            a.x = x
                            a.y = y
                            print(g.name, 'Mono-bottom', x, y, x1, y1, x2, y2)
                            g.changed()
                    elif 'Grid' in f.path:
                        y = y1
                        x = int(round(x1 + int((x2 - x1)/100/2) * 100 + y*tan(radians(-g.font.info.italicAngle or 0))))
                        if (x, y) != (a.x, a.y):
                            a.x = x
                            a.y = y
                            print(g.name, 'Grid-bottom', x, y, x1, y1, x2, y2)
                            g.changed()
                elif a.name == 'top':
                    if 'Prop' in f.path:
                        y = y2+100
                        if y == 600:
                            y = 500
                        elif y == 900:
                            y = 800
                        x = int(round(x1 + int((x2 - x1)/100/2) * 100 + y*tan(radians(-g.font.info.italicAngle or 0))))
                        if (x, y) != (a.x, a.y):
                            a.x = x
                            a.y = y
                            print(g.name, 'Prop-top', x, y, x1, y1, x2, y2)
                            g.changed()
                    elif 'Mono' in f.path:
                        y = y2+100
                        if y == 600:
                            y = 500
                        x = int(round(x1 + int((x2 - x1)/100/2) * 100 + y*tan(radians(-g.font.info.italicAngle or 0))))
                        if (x, y) != (a.x, a.y):
                            a.x = x
                            a.y = y
                            print(g.name, 'Mono-top', x, y, x1, y1, x2, y2)
                            g.changed()
                    elif 'Grid' in f.path:
                        y = y2+100
                        if y == 600:
                            y = 500
                        x = int(round(x1 + int((x2 - x1)/100/2) * 100 + y*tan(radians(-g.font.info.italicAngle or 0))))
                        if (x, y) != (a.x, a.y):
                            a.x = x
                            a.y = y
                            print(g.name, 'Mono-top', x, y, x1, y1, x2, y2)
                            g.changed()
                elif a.name == 'ogonek':
                    if 'Prop' in f.path:
                        y = 0
                        x = int(round(x2-100 + y*tan(radians(-g.font.info.italicAngle or 0))))
                        if (x, y) != (a.x, a.y):
                            a.x = x
                            a.y = y
                            print(g.name, 'Prop-ogonek', x, y, x1, y1, x2, y2)
                            g.changed()
                    elif 'Mono' in f.path:
                        y = 0
                        x = int(round(x2-100 + y*tan(radians(-g.font.info.italicAngle or 0))))
                        if (x, y) != (a.x, a.y):
                            a.x = x
                            a.y = y
                            print(g.name, 'Mono-ogonek', x, y, x1, y1, x2, y2)
                            g.changed()
                    elif 'Grid' in f.path:
                        y = 0
                        x = int(round(x2-100 + y*tan(radians(-g.font.info.italicAngle or 0))))
                        if (x, y) != (a.x, a.y):
                            a.x = x
                            a.y = y
                            print(g.name, 'Mono-ogonek', x, y, x1, y1, x2, y2)
                            g.changed()
                
                        
                """
                if a.x == 0 and a.y == 0:
                    pass
                    print(g.name, a.name, a.x, a.y,  f.path.split('/')[-1])
                if a.name == '_top' and not 'comb' in g.name:
                    print('Remove anchor', g.name, a.name)
                    g.removeAnchor(a)
                elif a.x == 0 and 'comb' not in g.name and not 'Prop' in f.path:
                    print(a.name, a.x, '-->', 200)
                    a.x = 200
                    g.changed() 
                elif a.x == 0 and 'comb' not in g.name and 'Prop' in f.path:
                    if a.name == 'top':
                        a.x = x1 + int((x2 - x1)/100/2) * 100
                        g.changed()
                    elif a.name == 'bottom':
                        a.x = x1 + int((x2 - x1)/100/2) * 100
                        g.changed()
                    elif a.name == 'ogonek':
                        a.x = x2 - 100
                    #if a.x == int(g.width/2):
                    #    a.x = int(g.width/100/2) * 100
                    print(a.name, a.x, '-->', 200, f.path.split('/')[-1])
                """
                
    f.save()
                
print('Done')
        