__author__ = 'joaquin'

from PyQt4 import *
import shutil
from Main import *
from infoDialog import *
from searchPhotoDialog import *
from addDialog import *
from albumDialog import *
import sys, shelve, os

class Photos():
    def __init__(self, title=None, data=None, file=None, metaP=None, metaL=None, metaA=None):

        self.title = title
        self.data = data
        self.file = file
        self.metadataP = []
        self.metadataL = []
        self.metadataA = []
        buffer = []
        if metaP:
            print metaP
            for m in metaP:
                buffer.append(m)
            self.metadataP = buffer
        buffer = []
        if metaL:
            for m in metaL:
                buffer.append(m)
            self.metadataL = buffer
        buffer = []
        if metaA:
            for m in metaA:
                buffer.append(m)
            self.metadataA.append(m)
            
    def updateMetadata(self, metaP, metaL, metaA):
        buffer = []
        self.metadataA = []
        self.metadataP = []
        self.metadataL = []
        
        if metaP:
            print metaP
            for m in metaP:
                buffer.append(m)
            self.metadataP = buffer
        buffer = []
        if metaL:
            for m in metaL:
                buffer.append(m)
            self.metadataL = buffer
        buffer = []
        if metaA:
            for m in metaA:
                buffer.append(m)
            self.metadataA.append(m)
    def getMetP(self):
        items = []
        for index in xrange(self.listMetadataP.count()):
            items.append(self.listMetadataP.item(index))
        labels = [i.text() for i in items]
        print labels
        return labels
    
    def getMetL(self):
        items = []
        for index in xrange(self.listMetadataL.count()):
            items.append(self.listMetadataL.item(index))
        labels = [i.text() for i in items]
        print labels
        return labels
    
    def getMetA(self):
        items = []
        for index in xrange(self.listMetadataA.count()):
            items.append(self.listMetadataA.item(index))
        labels = [i.text()  for i in items]
        print labels
        return labels

class Album():
    def __init__(self, title, data,):
        self.title = title
        self.data = data
        self.Photos = []

class searchPhotoDialog(QtGui.QDialog, Ui_searchPhotoDialog):
    def __init__(self, albums, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.x = 0
        self.y = 0
        self.albums = albums
        self.cercaFotoBtn.clicked.connect(self.cercarFotoTitol)
        self.comboAlbums.currentIndexChanged['QString'].connect(self.cercaPerAlbums)
        self.listPhotos.itemClicked.connect(self.readDataPhoto)
        self.editarBtn.clicked.connect(self.updatePhoto)
        self.addMetadataBtn.clicked.connect(self.addMetadata)
        self.delMetadataBtn.clicked.connect(self.delMetadata)
        self.OpenBtn.clicked.connect(self.openFile)
        self.eliminarBtn.clicked.connect(self.delPhoto)
        self.photo=None
    
    def delPhoto(self):
        self.y = 0
        
        for album in self.albums:
            if(str(self.comboAlbums.currentText())==album.title):
                for photo in album.Photos:
                    if(photo.title==str(self.listPhotos.currentItem().text())):
                        del album.Photos[self.y]
                        os.remove(str(photo.file))
                        self.saveAlbum()
                    self.y = self.y+1
        self.cercaPerAlbums()
        
    def saveAlbum(self):
        d = shelve.open("dades")
        d["Albums"] = self.albums
        d.close()
        
    def renameFile(self):
        file_extension = self.photo.file.split(".")
        """self.filename = self.encode(self.filename)"""
        format = str(self.photo.file).split(".")
        format =str(format[1])
        
        desti = str(self.comboAlbums.currentText())+"/"+(str(self.lineTitol2.text())+"."+format)
        print desti
        os.rename(str(self.photo.file),desti)
        """
        subs = os.path.basename(str(self.filename))
        cadena = str(str(self.comboAlbums.currentText()+str(self.lineEdit.text())+file_extension))
        os.rename(str(self.comboAlbums.currentText())+str(os.path.basename(str(self.filename))),str(cadena))
        """
        
    def updatePhoto(self):
        self.photo = self.getPhotoSelect()
        self.photo.updateMetadata(self.getMetP(), self.getMetL(), self.getMetA())
        if(self.photo.title != str(self.lineTitol2.text())):
            self.photo.title = str(self.lineTitol2.text())
            self.renameFile()
            self.cercaPerAlbums()


    def getCategoria(self):
        if(self.radioPersona2.isChecked()):
            return 'P'
        elif(self.radioLlocs2.isChecked()):
            return 'L'
        elif(self.radioAltres2.isChecked()):
            return 'A'
        
    def addMetadata(self):
        tipus = self.getCategoria()
        
        if tipus == 'P':
            self.listMetadataP.addItem(self.lineMetadata2.text())
        elif tipus == 'L':
            self.listMetadataL.addItem(self.lineMetadata2.text())
        elif tipus == 'A':
            self.listMetadataA.addItem(self.lineMetadata2.text())
            
    def delMetadata(self):
        
        tipus = self.getCategoria()
        if tipus == "P":
            item = self.listMetadataP.currentItem() 
            self.delMetadataOfPhoto('P')
            """Aixins abans de eliminar la referencia del entorn grafic, eliminem les dades del objecte"""
            self.listMetadataP.removeItemWidget(item)
            
        elif tipus == "L":
            item = self.listMetadataL.currentItem()
            self.delMetadataOfPhoto('L')
            self.listMetadataL.removeItemWidget(item)
            
        elif tipus== "A":
            item = self.listMetadataA.currentItem()
            self.delMetadataOfPhoto('A')
            self.listMetadataA.removeItemWidget(item)
            
        self.getMetadatas()
        """Fem un refresh de totes les llistes"""
    def delMetadataOfPhoto(self, tipus):
        """Aquesta funcio es necesaria per poder borrar tambe les dades del objcte photo sleccionat"""
        self.y = 0
        if(tipus=='P'):
            for metaP in self.photo.metadataP:
                if(str(self.listMetadataP.currentItem().text())==metaP):
                    print "Element %s eliminat ok" % (metaP)
                    del self.photo.metadataP[self.y]
                self.y = self.y + 1
        if(tipus=='L'):
            for metaL in self.photo.metadataL:
                if(str(self.listMetadataL.currentItem().text())==metaL):
                    print "Element %s eliminat ok" %(metaL)
                    del self.photo.metatadaL[self.y]
                self.y = self.y + 1
        if(tipus=='A'):
            for metaA in self.photo.metadataA:
                if(str(self.listMetadataA.current().text())==metaA):
                    print "Element %s eliminat ok" %(metaA)
                    del self.photo.metadataA[self.y]
                self.y = self.y + 1
    def getMetP(self):
        items = []
        for index in xrange(self.listMetadataP.count()):
            items.append(self.listMetadataP.item(index))
        labels = [i.text() for i in items]
        print labels
        return labels
    
    def getMetL(self):
        items = []
        for index in xrange(self.listMetadataL.count()):
            items.append(self.listMetadataL.item(index))
        labels = [i.text() for i in items]
        print labels
        return labels
    
    def getMetA(self):
        items = []
        for index in xrange(self.listMetadataA.count()):
            items.append(self.listMetadataA.item(index))
        labels = [i.text()  for i in items]
        print labels
        return labels

    def readDataPhoto(self):
        
        self.photo = self.getPhotoSelect()
        print self.photo.title
        print self.photo.data
        print self.photo.file
        self.lineTitol2.setText(self.photo.title)
        self.label.setText(self.photo.file)
        self.getMetadatas()
    
    def getPhotoSelect(self):
        
        for album in self.albums:
            if(str(self.comboAlbums.currentText())==album.title):
                for photo in album.Photos:
                    if(photo.title==str(self.listPhotos.currentItem().text())):
                        return photo
    
    
    def getMetadatas(self):
        """Neteixem tot els listWidgets perque reomplirem les metadades
           amb les noves fotos que es cliquen al listPhotosWindget 
        """
        self.setMetadatasListWidget()
        
        for photoMetP in self.photo.metadataP:
            self.listMetadataP.addItem(photoMetP)
        
        for photoMetL in self.photo.metadataL:
            self.listMetadataL.addItem(photoMetL)
        
        for photoMetA in self.photo.metadataA:
            self.listMetadataA.addItem(photoMetA)
            
            
    def setMetadatasListWidget(self):
        self.listMetadataP.clear()
        self.listMetadataL.clear()
        self.listMetadataA.clear()
        
    def cercaPerAlbums(self):
        self.listPhotos.clear()
        self.x = 0
        self.y = 0
        for album in self.albums:
            self.x = self.x + 1
            if(str(self.comboAlbums.currentText())==album.title):
                for photo in album.Photos:
                    self.y = self.y + 1
                    self.listPhotos.addItem(photo.title)
                    
        
    def updateListAlbums(self):
        self.comboAlbums.clear()
        for album in self.albums:
            self.comboAlbums.addItem(album.title)
            self.saveAlbum()

    def cercarFotoTitol(self):
        self.x = 0
        self.listPhotos.clear()
        for album in self.albums:
            for photo in album.Photos:
                if(str(self.lineTitol.text()) in(photo.title)):
                    self.listPhotos.addItem(photo.title)
                    self.comboAlbums.setCurrentIndex(self.x)
                    print album.title
            self.x = self.x+1

    def openFile(self):
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir,self.photo.file)
        os.startfile(filename)
        
class albumDialog(QtGui.QDialog, Ui_AlbumDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

class infoDialog(QtGui.QDialog, Ui_InfoDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

class Dialog(QtGui.QDialog, Ui_Dialog):

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.addAlbumBtn.clicked.connect(self.showAlbumDialog)
        self.addMetaDataBtn.clicked.connect(self.addMetadata)
        self.delMetadataBtn.clicked.connect(self.delMetadata)
        self.comboAlbums.currentIndexChanged['QString'].connect(self.getParameters)
        self.textcombo = None
        self.category = ["Persones","Llocs","Altres"]
        self.albums = []
        self.album = None
        self.desti = None
        self.scene = QtGui.QGraphicsScene()
        """self.scene.setSceneRect(QtCore.QRectF(0.0, 0.0, self.__size.width(), self.__size.height()))"""
        self.connect(self.uploadFileBtn,QtCore.SIGNAL('clicked()'), self.open)
        self.albumDialog = albumDialog()
        self.filename = None
        
    def getParameters(self):
        print "Has seleccionat Album:"+self.comboAlbums.currentText()
        self.textcombo = str(self.comboAlbums.currentText())
        
        
    def getMetP(self):
        items = []
        for index in xrange(self.listMetadataP.count()):
            items.append(self.listMetadataP.item(index))
        labels = [i.text() for i in items]
        print labels
        return labels
    
    def getMetL(self):
        items = []
        for index in xrange(self.listMetadataL.count()):
            items.append(self.listMetadataL.item(index))
        labels = [i.text() for i in items]
        print labels
        return labels
    
    def getMetA(self):
        items = []
        for index in xrange(self.listMetadataA.count()):
            items.append(self.listMetadataA.item(index))
        labels = [i.text()  for i in items]
        print labels
        return labels
    
    def addMetadata(self):
        tipus = self.getCategoria()
        
        if tipus == 'P':
            self.listMetadataP.addItem(self.lineEditMetadata.text())
        elif tipus == 'L':
            self.listMetadataL.addItem(self.lineEditMetadata.text())
        elif tipus == 'A':
            self.listMetadataA.addItem(self.lineEditMetadata.text())
            
    def delMetadata(self):
        
        tipus = self.getCategoria()
        if tipus == "P":
            item = self.listMetadataP.currentItem() 
            self.listMetadataP.removeItemWidget(item)
        elif tipus == "L":
            item = self.listMetadataL.currentItem()
            self.listMetadataL.removeItemWidget(item)
        elif tipus== "A":
            item = self.listMetadataA.currentItem()
            self.listMetadataA.removeItemWidget(item)
        
    def copyFile(self):
        file_extension = self.filename.split(".")
        """self.filename = self.encode(self.filename)"""
        format = str(self.filename).split(".")
        format =str(format[1])
        print """copiat a la carpeta :"""+self.textcombo
        self.desti = self.textcombo+"/"+(str(self.lineEdit.text())+"."+format)
        print self.desti
        shutil.copy(str(self.filename),self.desti)
        """
        subs = os.path.basename(str(self.filename))
        cadena = str(str(self.comboAlbums.currentText()+str(self.lineEdit.text())+file_extension))
        os.rename(str(self.comboAlbums.currentText())+str(os.path.basename(str(self.filename))),str(cadena))
        """

    def mkdir_p(self):
        try:
            os.mkdir(self.albumDialog.titol.text())
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(self.albumDialog.titol.text()):
                pass
            else: raise

    def open(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        print 'Path file :', filename
        img =QtGui.QImage(filename)
        self.scene.addPixmap(QtGui.QPixmap(filename))
        self.graphicsView.setScene(self.scene)
        self.graphicsView.update()
        self.graphicsView.show()
        self.label_5.setText(filename)
        self.filename = filename


    def updateListAlbums(self):
        self.comboAlbums.clear()
        for album in self.albums:
            self.comboAlbums.addItem(album.title)

    def showAlbumDialog(self):

        ok = self.albumDialog.exec_()
        if ok:
            self.album = Album(self.albumDialog.titol.text(), self.albumDialog.data.text())
            self.mkdir_p()
            self.albums.append(self.album)
            self.updateListAlbums()
    
    def getCategoria(self):
        if(self.radioPersonaBtn.isChecked()):
            return 'P'
        elif(self.radioLlocsBtn.isChecked()):
            return 'L'
        elif(self.radioAltresBtn.isChecked()):
            return 'A'
    
    
    def savePhoto(self):
        for album in self.albums:
            if(album.title == str(self.comboAlbums.currentText())):
                cat = self.getCategoria()
                photo = Photos(str(self.lineEdit.text()), str(self.Data.text()),str(self.desti),self.getMetP(),self.getMetL(),self.getMetA())
                #Aqui ahora viene toda la tralla!!!!
                album.Photos.append(photo)

    def saveAlbum(self):
        d = shelve.open("dades")
        d["Albums"] = self.albums
        d.close()

    def readAlbum(self):
        d = shelve.open("dades")
        self.albums = d["Albums"]
        self.updateListAlbums()
        d.close()

    def encode(text):

        return text.encode('utf-8')


class Main(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.addDialog = None
        self.searchPhotoDialog = None
        self.albums = []
        self.funcionalitat()
        self.readAlbum()
        self.infoDialog = infoDialog()

    def saveAlbum(self):
        d = shelve.open("dades")
        d["Albums"] = self.albums
        d.close()

    def readAlbum(self):
        try:
            d = shelve.open("dades")
            self.albums = d["Albums"]
            d.close()
        except:
            return 0

    def Nova(self):

        self.addDialog = Dialog()
        self.addDialog.albums = self.albums
        self.addDialog.updateListAlbums()
        ok = self.addDialog.exec_()
        if ok:
            self.addDialog.albums=self.albums
            """self.addDialog.updateListAlbums()"""
            self.addDialog.copyFile()
            self.addDialog.savePhoto()
            self.saveAlbum()

    def CercaPhoto(self):
        self.searchPhotoDialog = searchPhotoDialog(self.albums)
        self.searchPhotoDialog.cercarFotoTitol()
        self.searchPhotoDialog.updateListAlbums()
        ok = self.searchPhotoDialog.exec_()
        if ok:
            self.saveAlbum()
    
    def infoProgram(self):
        ok = self.infoDialog.exec_()
    def funcionalitat(self):

        self.actionNova_Imatge.triggered.connect(self.Nova)
        self.actionCerca_Imatge.triggered.connect(self.CercaPhoto)
        self.actionQui_som.triggered.connect(self.infoProgram)
        img =QtGui.QImage("_img/aulasvc.png");
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(QtGui.QPixmap(img))
        self.graphicsView.setScene(scene)
        self.graphicsView.update()

        
        """self.actionOpen.triggered.connect(self.obrir)"""

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
    


