function hwm93()
% quick demo calling HWM93 model from Matlab.
% https://www.scivision.co/matlab-python-user-module-import/

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

function V = xarray2mat(V)
  % convert xarray 2-D array to Matlab matrix


V= V.values;
S = V.shape;
V = cell2mat(cell(V.ravel('F').tolist()));
if length(S) == 2
  V = reshape(V,[int64(S{1}), int64(S{2})]);
end

end

function I = xarrayind2vector(V,key)

C = cell(V{1}.indexes{key}.values.tolist);  % might be numeric or cell array of strings

if iscellstr(C) || any(class(C{1})=='py.str')
    I=cellfun(@char,C, 'uniformoutput',false);
else
    I = cell2mat();
end % if

end % function
