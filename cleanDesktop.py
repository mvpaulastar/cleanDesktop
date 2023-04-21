import os, sys, shutil

downloadsFolder = 'C:/Users/slyce/Downloads'

def cleanNewFolders():
    allFiles = [*os.listdir('./'), *os.listdir(downloadsFolder)]
    newFolders = [newFolder for newFolder in allFiles if "New folder" in newFolder and os.path.isdir(newFolder)]
    for folder in newFolders:
        shutil.rmtree(folder)

def sortFiles():
    imgs = ['.png', '.jpg', '.psd', '.webp']
    maps = ['.w3x', '.w3m']
    downloads = os.listdir(downloadsFolder)
    desktop = os.listdir('./')
    downloads = [downloadsFolder +'/'+ file for file in downloads]
    allFiles = [*desktop, *downloads]
    imgFiles = [img for img in allFiles if img[-4:] in imgs]
    mapFiles = [map for map in allFiles if map[-4:] in maps]
    for map in mapFiles:
        if os.path.isdir(map):
            shutil.copytree(map, './Map Stuff', dirs_exist_ok=True)
            shutil.rmtree(map)
        else: 
            shutil.copy(map, './Map Stuff')
            os.remove(map)
    for img in imgFiles:
        shutil.copy(img, './Images')
        os.remove(img)

#Command line args
numArgs = len(sys.argv)

match sys.argv[1]:
    case "newFolder":
        cleanNewFolders()
    case "sortFiles":
        sortFiles()
    case _:
        print('Invalid Arguments')
    
