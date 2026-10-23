import cadquery as cq
from cadquery import exporters
from pathlib import Path
import math
OUT=Path(__file__).resolve().parent; # For exact PCB outline place official DXF-derived STEP in this folder.
# Fallback uses rectangular 100x60 board, 1.6mm thick, with approximate mounting holes.
board_ref=OUT/'ANTSDR_E310_ES2_board_preview.step'
if board_ref.exists():
 base=cq.importers.importStep(str(board_ref)).solids().val()
else:
 pcb=cq.Workplane('XY').box(100,60,1.6,centered=(False,False,False))
 for x in (3.0,97.0):
  for y in (3.0,57.0):
   pcb=pcb.cut(cq.Workplane('XY').center(x,y).circle(1.6).extrude(1.6))
 base=pcb.val()
items=[]
def add(name, shape, color): items.append((name,shape,color))
def block(name,x,y,z,w,d,h,col):add(name,cq.Workplane('XY').box(w,d,h,centered=(False,False,False)).translate((x,y,z)).val(),col)
def cyl(name,x,y,z,r,h,col):add(name,cq.Workplane('XY').circle(r).extrude(h).translate((x,y,z)).val(),col)
def x_cyl(name,x,y,z,r,L,col):add(name,cq.Solid.makeCylinder(r,L,cq.Vector(x,y,z),cq.Vector(1,0,0)),col)
add('PCB_DXF_outline_100x60',base,(0.045,0.16,0.13))
# edge connectors, matched to DXF X0 end and user's photos
block('Ethernet_RJ45_housing',-2.0,27.1,1.6,16.5,16.0,13.3,(0.69,0.71,0.73))
block('RJ45_black_inner',-2.5,30.1,4.5,1.0,10.0,6.0,(0.07,0.07,0.08))
for i,y in enumerate([7.1,20.1],1):
 block('USB_TypeC_'+str(i),-4.0,y-4.0,1.6,8.7,8.0,4.1,(0.74,0.76,0.79))
 block('USB_C_tongue_'+str(i),-4.1,y-2.1,3.25,1.2,4.2,0.8,(0.15,0.15,0.17))
# SMA CAD surface footprint from DXF: y6,22,38,54, not equally spaced erroneous middle y22 to 38 old 35 etc
for i,y in enumerate([6.0,22.0,38.0,54.0],1):
 block(f'SMA_{i}_base',95.6,y-3.1,1.6,4.4,6.2,6.5,(0.76,0.61,0.22))
 x_cyl(f'SMA_{i}_barrel',100.0,y,5.0,3.05,11.3,(0.79,0.64,0.25))
 # separate bore visually apparent at end
 x_cyl(f'SMA_{i}_center',111.35,y,5.0,0.65,0.25,(0.14,0.12,0.08))
# RF shield occupies RF side, top of PCB
block('RF_metal_shield_APPROX',62.5,4.1,1.6,33.1,51.7,7.5,(0.71,0.73,0.74))
# heatsink around center of board as photographed
block('Zynq_SOC_body',31.5,15.0,1.6,30,29,3.0,(0.12,0.13,0.14))
block('Heatsink_base',30.7,14.0,4.6,31.2,31.2,2.1,(0.07,0.08,0.09))
for i in range(9): block('Heatsink_fin_'+str(i+1),31.2+i*3.5,14.4,6.7,1.3,30.2,9.2,(0.075,0.078,0.083))
# 2 memory chips beside radiator approximations
for i,y in enumerate([16,30]):block('DDR_memory_'+str(i+1),15.2,y,1.6,12.0,12.3,1.6,(0.09,0.1,0.115))
# microSD on PCB reverse near Ethernet end; in photo SD on underside, not centered
# x=12-31, y=34-57; tray overhang narrow edge
block('microSD_socket_UNDERSIDE',10.0,34.0,-2.0,19.0,22.0,2.0,(0.69,0.71,0.74))
# gpio is holes, so only lightly mark outer header region; footprint is DXF already
# 2 miniature RF clock connectors at x around 65 and x~? at opposite edges
for i,(x,y) in enumerate([(65.5,55.4),(66.2,4.8)],1):
 cyl('RF_mini_connector_'+str(i),x,y,1.6,1.65,2.4,(0.78,0.64,0.27))
 cyl('RF_mini_socket_center_'+str(i),x,y,4.0,0.55,0.15,(0.1,0.09,0.06))
# some major ICs on board near Ethernet
block('interface_controller_1',14.5,48.0,1.6,13,8,1.6,(0.13,0.14,0.17))
block('interface_controller_2',12.0,5.6,1.6,13,8,1.6,(0.12,0.13,0.15))
# Rear of PCB (bottom-photo): approximate logic chips, QFNs and power blocks
for i,(x,y,w,d,h) in enumerate([(57,26,13,9,1.4),(10,12,9,9,1.3),(13,45,8,8,1.3),(71,10,5,5,1.2),(74,45,5,5,1.2),(36,13,6,6,1.1)],1):
 block(f'underside_chip_{i}_APPROX',x,y,-h,w,d,h,(0.11,0.12,0.14))
# Photos show two small status indicators near ethernet, include only visible top LED
cyl('green_status_LED_APPROX',10.5,56.8,1.6,1.25,2.6,(0.07,0.62,0.22))
# metal microSD socket is on rear (opposite heatsink), close to Ethernet end
# no third USB at all
assembly=cq.Assembly(name='ANTSDR_E310_ES2_photo_approx')
for name,s,col in items: assembly.add(s,name=name,color=cq.Color(*col))
step=OUT/'ANTSDR_E310_photo_corrected_v30.step'; stl=OUT/'ANTSDR_E310_photo_corrected_v30.stl'
assembly.save(str(step),exportType='STEP')
# STL with all independent bodies (no boolean union needed for inspection)
cq.exporters.export(cq.Compound.makeCompound([s for _,s,_ in items]),str(stl),exportType='STL',tolerance=0.12,angularTolerance=0.2)
print('Saved',step,step.stat().st_size,stl,stl.stat().st_size,'parts',len(items))