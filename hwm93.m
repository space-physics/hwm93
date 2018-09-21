function hwm93()
%% HWM93 model from Matlab.
% https://www.scivision.co/matlab-python-user-module-import/
assert(~verLessThan('matlab', '9.5'), 'Matlab >= R2018b required')

% geographic WGS84 lat,lon,alt
glat = 65.1;
glon = -147.5;
alt_km = 100:10:1000;
t = '2015-12-13T10';
f107 = 100;
f107a = 100;
ap = 4;


winds = py.hwm93.run(t, alt_km, glat, glon, f107a, f107, ap);

merid = xarray2mat(winds{'meridional'});
zonal = xarray2mat(winds{'zonal'});

plotwinds(alt_km, merid, zonal, t, glat, glon)
end

function plotwinds(alt_km, merid, zonal, t,glat,glon)
  figure(1), clf(1)
  ax = axes('nextplot','add');

  plot(ax, merid, alt_km, 'displayname', 'meridional')
  plot(ax, zonal, alt_km, 'displayname', 'zonal')
  
  title({[t,' deg.  (',num2str(glat),',', num2str(glon),')']})
  xlabel('Density [m^-3]')
  ylabel('altitude [km]')

  grid('on')
  legend('show')
  
end

function M = xarray2mat(V)
M = double(py.numpy.asfortranarray(V));
end
