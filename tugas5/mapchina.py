import mapnik
m = mapnik.Map(800,400)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 3)
line_symbolizer.stroke_width =  10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style1',s)
ds = mapnik.Shapefile(file="shpadm/CHN_adm0.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style1')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 3)
line_symbolizer.stroke_width =  10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="shpadm/CHN_adm1.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'), 3)
line_symbolizer.stroke_width =  10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style3',s)
ds = mapnik.Shapefile(file="shprds/CHN_roads.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style3')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('yellow'), 3)
line_symbolizer.stroke_width =  10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style4',s)
ds = mapnik.Shapefile(file="shprrd/CHN_rails.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style4')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) 

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('grey'), 3)
line_symbolizer.stroke_width =  10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style5',s)
ds = mapnik.Shapefile(file="shpwat/CHN_water_areas_dcw.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style5')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m, 'china.pdf', 'pdf')
print "rendered file to 'china.pdf' "

 