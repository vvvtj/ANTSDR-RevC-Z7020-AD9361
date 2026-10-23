// ANTSDR E310 Rev.C 23-E310B25-20 enclosure-clearance model
// Units: mm. Photo-derived approximations, NOT verified mechanical tolerances.
// Compare with MicroPhase ANT_E310_ES2_Mechanical.dxf before manufacture.
// X=0 Ethernet/USB end; X=100 SMA end. Component side is +Z.
$fn=32;
module cube_at(x,y,z,w,d,h){ translate([x,y,z]) cube([w,d,h]); }
module shaft_x(x,y,z,r,l){translate([x,y,z])rotate([0,90,0])cylinder(h=l,r=r);}
module pcb(){
 difference(){
  color([0.05,0.17,0.13]) cube_at(0,0,0,100,60,1.6);
  // mounting hole positions provisional: refer to original DXF for exact drill file
  for(x=[3,97],y=[3,57])translate([x,y,-0.5])cylinder(h=3,r=1.6);
 }
}
module assembly(){
 pcb();
 // two USB Type C at interface end; no micro-USB
 color("silver")for(y=[7.1,20.1])cube_at(-4,y-4,1.6,8.7,8,4.1);
 // RJ45
 color("silver")cube_at(-2,27.1,1.6,16.5,16,13.3);
 // four edge mounted SMA
 color("gold")for(y=[6,22,38,54]){
   cube_at(95.6,y-3.1,1.6,4.4,6.2,6.5);
   shaft_x(100,y,5,3.05,11.3);
 }
 // RF shield + heatsink
 color("silver")cube_at(62.5,4.1,1.6,33.1,51.7,7.5);
 color("black")cube_at(31.5,15,1.6,30,29,3);
 color("black")cube_at(30.7,14,4.6,31.2,31.2,2.1);
 color("black")for(i=[0:8])cube_at(31.2+i*3.5,14.4,6.7,1.3,30.2,9.2);
 color("black")for(y=[16,30])cube_at(15.2,y,1.6,12,12.3,1.6);
 // underside microSD (towards Ethernet)
 color("silver")cube_at(10,34,-2,19,22,2);
 // small onboard connector models; NOT antenna-port validation
 color("gold")for(p=[[65.5,55.4],[66.2,4.8]])translate([p[0],p[1],1.6])cylinder(h=2.4,r=1.65);
 color("black"){
  cube_at(14.5,48,1.6,13,8,1.6);
  cube_at(12,5.6,1.6,13,8,1.6);
  for(a=[[57,26,13,9,1.4],[10,12,9,9,1.3],[13,45,8,8,1.3],[71,10,5,5,1.2],[74,45,5,5,1.2],[36,13,6,6,1.1]])
   cube_at(a[0],a[1],-a[4],a[2],a[3],a[4]);
 }
}
assembly();
