f = CurrentFont()

g = f['matrix612']

XY = []
for component in g.components:
    dx = component.transformation[-2]
    dy = component.transformation[-1]
    
    XY.append((int(dx), int(dy)))
    XY.append((int(dx-1000), int(dy)))
    XY.append((int(dx-500), int(dy)))
    XY.append((int(dx+500), int(dy)))
    XY.append((int(dx+1000), int(dy)))
    XY.append((int(dx+1500), int(dy)))
    XY.append((int(dx+2000), int(dy)))
    XY.append((int(dx+2500), int(dy)))


#XY = [(-42, -300), (58, -300), (158, -300), (258, -300), (358, -300), (458, -300), (-28, -200), (72, -200), (172, -200), (272, -200), (372, -200), (472, -200), (-14, -100), (86, -100), (186, -100), (286, -100), (386, -100), (486, -100), (0, 0), (100, 0), (200, 0), (300, 0), (400, 0), (500, 0), (14, 100), (114, 100), (214, 100), (314, 100), (414, 100), (514, 100), (28, 200), (128, 200), (228, 200), (328, 200), (428, 200), (528, 200), (42, 300), (142, 300), (242, 300), (342, 300), (442, 300), (542, 300), (56, 400), (156, 400), (256, 400), (356, 400), (456, 400), (556, 400), (70, 500), (170, 500), (270, 500), (370, 500), (470, 500), (570, 500), (84, 600), (184, 600), (284, 600), (384, 600), (484, 600), (584, 600), (98, 700), (198, 700), (298, 700), (398, 700), (498, 700), (598, 700), (112, 800), (212, 800), (312, 800), (412, 800), (512, 800), (612, 800), (-642, -300), (-542, -300), (-442, -300), (-342, -300), (-242, -300), (-142, -300), (-628, -200), (-528, -200), (-428, -200), (-328, -200), (-228, -200), (-128, -200), (-614, -100), (-514, -100), (-414, -100), (-314, -100), (-214, -100), (-114, -100), (-600, 0), (-500, 0), (-400, 0), (-300, 0), (-200, 0), (-100, 0), (-586, 100), (-486, 100), (-386, 100), (-286, 100), (-186, 100), (-86, 100), (-572, 200), (-472, 200), (-372, 200), (-272, 200), (-172, 200), (-72, 200), (-558, 300), (-458, 300), (-358, 300), (-258, 300), (-158, 300), (-58, 300), (-544, 400), (-444, 400), (-344, 400), (-244, 400), (-144, 400), (-44, 400), (-530, 500), (-430, 500), (-330, 500), (-230, 500), (-130, 500), (-30, 500), (-516, 600), (-416, 600), (-316, 600), (-216, 600), (-116, 600), (-16, 600), (-502, 700), (-402, 700), (-302, 700), (-202, 700), (-102, 700), (-2, 700), (-488, 800), (-388, 800), (-288, 800), (-188, 800), (-88, 800), (12, 800)]

#print(XY)

for g in f:
    for component in g.components:
        t = list(component.transformation)
        dx = int(t[-2])
        dy = int(t[-1])
        t[-2] = dx
        t[-1] = dy
        if t != component.transformation:
            component.transformation = t
        if not (dx, dy) in XY:
            changed = False
            for x, y in XY:

                t = list(component.transformation)
                dx = int(t[-2])
                dy = int(t[-1])
                if 0 < abs(dx - x) < 50 and 0 <= abs(dy - y) < 50:
                    print(g.name, dx, dy, x, y)                            
                    t[-2] = x
                    #if t != component.transformation:
                    component.transformation = t
                    changed = True

                t = list(component.transformation)
                dx = int(t[-2])
                dy = int(t[-1])
                if 0 < abs(dy - y) < 50 and 0 <= abs(dx - x) < 50:
                    print(g.name, dx, dy, x, y)
                    t[-1] = y
                    #if t != component.transformation:
                    component.transformation = t
                    changed = True
                if changed:
                    g.changed()
                    break



if not 'Dcircle' in f:
    f['Dcircle'] = f['copyright']
    f['Dcircle'].unicode = 0x24B9
    print('Add /Dcircle', f.path)

f['Dcircle'].changed()
print('Done')