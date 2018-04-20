import mapnik
m = mapnik.Map(800,400)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) 


line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 3)


r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style1',s)
ds = mapnik.Shapefile(file="../INDONESIA_KEC.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style1')
m.layers.append(layer)

s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer) 


line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 3)


r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="../shp/masjid.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m, 'indo.pdf', 'pdf')
print "rendered file to 'indo.pdf' "