"""
This Python script converts Meshlab inertia into SDF format

Usage example:
    % python3 compute_inertia.py
    Object Mass is : 0.0105
    Mesh Volume is : 15253.618164
    Inertia Tensor is :
      8171479.500000 -1091.582153 858.932007
      -1091.582153 6636559.000000 29447.435547
      858.932007 29447.435547 2481984.750000    

    <inertia>
      <ixx>5.624930021684789</ixx>
      <ixy>-0.0007514028791903619</ixy>
      <ixz>0.0005912555287889139</ixz>
      <iyy>4.568350194084484</iyy>
      <iyz>0.020270474186461353</iyz>
      <izz>1.7085021792735104</izz>
    </inertia>
"""

mass = float(input("Object Mass is : "))
volume = float(input("Mesh Volume is : "))
print("Inertia Tensor is :")
j = [list(map(float, input("  ").strip().split(" "))) for _ in range(3)]

for i in range(3):
    for k in range(3):
        j[i][k] *= mass/volume

print(f"""\n<inertia>
  <ixx>{j[0][0]}</ixx>
  <ixy>{j[0][1]}</ixy>
  <ixz>{j[0][2]}</ixz>
  <iyy>{j[1][1]}</iyy>
  <iyz>{j[1][2]}</iyz>
  <izz>{j[2][2]}</izz>
</inertia>""")
