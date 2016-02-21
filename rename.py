import glob, os

def rename(dir, pattern, patternSuffix):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        name, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename,
                  os.path.join(dir, name + patternSuffix + ext))

rename(r'c:\workspace\jquery\MyGallery\images\photos', r'*.jpg', r'_fullsize')
