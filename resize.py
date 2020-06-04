import click
from lib.resize import Batch
import os

@click.command()
@click.option('-l','--length', default=1200, help='Maximum length of edge of image')
@click.option('-i','--image_format', default='JPEG', help='Image format - JPEG, TIFF, WebP')
@click.option('-c','--compression', default=75, help='Compression Level')
@click.option('-d','--directory', required=True, help='Directory to batch resize')
def run_main(length, image_format, compression, directory):
   """
      Sets config and runs batch script
   """
   
   if os.path.isdir(directory):
      batch = Batch(length=length, image_format=image_format, compression=compression, directory=directory)
      batch.batch()
      print('Batch Resize Complete')

   else:
      print('Not a valid directory')
   

if __name__ == '__main__':
   run_main()