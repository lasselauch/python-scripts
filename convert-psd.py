import sys
import os
from psd_tools import PSDImage

def getsuffix(fn):
    f, ext = os.path.splitext(fn)
    if not ' ' in ext:
        return f, ext

def ExportLayers(psd, folder, f):
    for layer in psd.layers:
        filename = "%s_%s" % (f, layer.name)
        outfile = os.path.join(folder, filename + sys.argv[2])
        if layer.visible:
            layer = layer.as_PIL()
            layer.save(outfile)

        print "\n..........................................\n"
        print 'Exported Layer: "%s" from "%s.psd"' % (os.path.basename(outfile), os.path.basename(f))
        print "\n.........................................."

#infile = sys.argv[1]
#LAYERS = False
try:
    LAYERS = sys.argv[3]
except:
    LAYERS = False

for infile in sys.argv[1:]:
    if os.path.isdir(infile):
        os.chdir(infile)
        files = filter(os.path.isfile, os.listdir(infile))
        files = [os.path.join(infile, f) for f in files] # add path to each file
    else:
        files = [infile]

    for infile in files:
        folder, fn = os.path.split(infile)
        f, ext = getsuffix(infile)

        if ext == '.psd':
            psd = PSDImage.load(infile)

            #Export all visibile Layers from PSD
            if LAYERS:
                ExportLayers(psd, folder, f)
                exit()

            #Convert PSD to PNG
            merged = psd.as_PIL()
            outfile = os.path.join(folder, f + sys.argv[2])
            merged.save(outfile)
            print "\n..........................................\n"
            print 'Converted "%s" to "%s"' % (os.path.basename(infile), os.path.basename(outfile))
            print "\n.........................................."
