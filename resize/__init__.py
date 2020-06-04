import click
from PIL import Image
import magic
import os

class Batch:

   def __init__(self, **kwargs):
      """
         Initialize class with a dict containing 
         key value pairs for
         length, format, compression, and directory       
      """
      self.length = kwargs.get('length', 1200)
      self.image_format = kwargs.get('image_format', 'JPEG')
      self.compression = int(kwargs.get('compression'))
      self.directory = kwargs.get('directory')
      self.resizeDir = os.path.join(kwargs.get('directory'), 'resized')
      print('Batch configurations set')


   def processImage(self, filePath, fileName, mimeType):
      """
         starts image process
      """
      acceptedMimetypes = (
         'image/jpeg',
         'image/webp',
         'image/tiff',
         'image/bmp',
         'image/png'
      )

      if mimeType in acceptedMimetypes:
         """
            If mimeType is within accepted mimeTypes,
            Open image into memory
            Get Img Dimensions
            Check if image is landscape
            Resize based on image orientation
         """
         img = Image.open(filePath)
         imgW, imgH = img.size
         isLandscape = imgW > imgH
         resizedImg = None

         print('Resizing ', fileName)

         if isLandscape:
            resizedImg = self.resizeLandscape(img, imgW, imgH)

         else:
            resizedImg = self.resizePortrait(img, imgW, imgH)

         if resizedImg:
            """
               If resized image is returned and is not falsey,
               generate new filepath, save, then close out files
            """
            
            name, extension = os.path.splitext(fileName)
            
            if self.image_format is 'TIFF':
               newFileName = name + '.tiff'
               resizeFilePath = os.path.join(self.resizeDir, newFileName)

               resizedImg.save(resizeFilePath, format="TIFF", compression="tiff_jpeg",quality=self.compression)

            elif self.image_format is 'WebP':
               newFileName = name + '.webp'
               resizeFilePath = os.path.join(self.resizeDir, newFileName)

               resizedImg.save(resizeFilePath, format="WebP", quality=self.compression)

            else:
               newFileName = name + '.jpg'
               resizeFilePath = os.path.join(self.resizeDir, newFileName)

               resizedImg.save(resizeFilePath, format="JPEG", quality=self.compression)

            resizedImg.close()

         img.close()


   def resizeLandscape(self, img, imgW, imgH):
      """
         will resize image in landscape context
      """
      dimensions = (self.length, int(self.length * imgH/imgW))
      resizeImg = img.resize(dimensions)
      return resizeImg
      

   def resizePortrait(self, img, imgW, imgH):
      """
         will resize image in portrait context
      """
      dimensions = (int(self.length * imgW/imgH), self.length)
      resizeImg = img.resize(dimensions)
      return resizeImg

   def batch(self):
      """
         takes a folder and creates a list of images.
         resize each image
      """
      print('Run Batch now!')
      
      dirList = os.listdir(self.directory)
      if not os.path.exists(self.resizeDir):
         os.makedirs(self.resizeDir)
         print('Creating resize folder')

      for listing in dirList:
         listingPath = os.path.join(self.directory, listing)
         isFile = os.path.isfile(listingPath)
         if isFile:
            mimeType = magic.from_file(listingPath, mime=True)
            self.processImage(listingPath, listing, mimeType)
