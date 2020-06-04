# Batch Image Resizer 
Simple batch image resizer script. 
  
CLI interface:  
```python resize.py -l newLengthOfFile -i imageFormat -c Compression Level -d PathToDirectory*```  
  
-d is a required parameter.  Should be the absolute path to directory  
  

Image formats supported are JPEG, TIFF, WebP for saving.  
 
For reading images, 'image/jpeg',   'image/webp', 'image/tiff', 'image/bmp', 'image/png' are accepted mime types