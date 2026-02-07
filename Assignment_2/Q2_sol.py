import numpy as np
import skimage.io

class cropper:
    def __init__(self, file_name):
        self.path = file_name
        self.img = skimage.io.imread(self.path)
        
    def __call__(self, tl_corner, br_corner):
        self.x0, self.y0 = tl_corner
        self.x1, self.y1 = br_corner

        self.cropped = self.img[self.x0:self.x1, self.y0:self.y1,:]

        directory = self.path.rsplit('/',1)[0]
        image_name = self.path.split('/')[-1].rsplit('.',1)[0]
        save_path = directory + "/" + image_name + "_cropped" + ".png"

        skimage.io.imsave(save_path,self.cropped)    

class segementator:
    def __init__(self, file_name):
        self.path = file_name
        self.img = skimage.io.imread(self.path)

    def __call__(self, r_threshold, g_threshold):

        self.binary_img = np.zeros((self.img.shape[0],self.img.shape[1]),dtype=bool)
        self.binary_img[self.img[:,:,0]>r_threshold] = 255
        self.binary_img[self.img[:,:,1]>g_threshold] = 0
        

        self.masked_img = np.zeros_like(self.img)
        self.masked_img[:,:,3] = 255

        self.masked_img[self.binary_img] = self.img[self.binary_img]

        directory = self.path.rsplit('/',1)[0]
        image_name = self.path.split('/')[-1].rsplit('.',1)[0]
        binary_save_path = directory + "/" + image_name + "_binary_mask" + ".png"
        mask_save_path = directory + "/" + image_name + "_masked_image" + ".png"

        skimage.io.imsave(binary_save_path,self.binary_img)
        skimage.io.imsave(mask_save_path,self.masked_img)



cropped = cropper('Assignment_2/glasshouse_pepper.png')
cropped((550,300),(650,400))

segemented = segementator('Assignment_2/glasshouse_pepper.png')
segemented(60,50)