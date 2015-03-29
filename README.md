# python-hwm93
NASA Horizontal Wind Model HWM93 in Python

All credit to original authors, I slightly modified the Fortran 77 
code so it could compile in a modern compiler. 

```
f2py3 -m hwm93 -c hwm93_sub.for 
```
plot by:
```
python demo_hwm93.py
```

Prereqs:
--------
``` pip install -r requirements.txt ```

#### Reference
Original A. E. Hedin Fortran 77 HWM93 code from
ftp://hanna.ccmc.gsfc.nasa.gov/pub/modelweb/atmospheric/hwm93/
