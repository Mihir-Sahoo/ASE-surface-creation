from ase import *
from math import *
from ase.io import *
from ase.lattice.surface import *
lattice = read ('POSCAR')
s1 = surface(lattice, (1,1,1) ,1)
s1.center(vacuum = 10, axis =2)
write('POSCAR-11.vasp',s1)
