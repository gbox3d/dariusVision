#%%
import cv2 as cv
import numpy as np

from PIL import Image
from IPython.display import display

import os
os.chdir("../")

from dariusVision import getCameraClass,getVersion

print(getVersion())
# %% realsense camera
lcam = getCameraClass(type='rs2')(vid_src=0)
lcam.startCamera()

#%%
# _,_,frame = lcam.getFrame()
depth_buffer = lcam.getDepthBuffer()

depth_frame = np.asanyarray(depth_buffer.get_data())

print(depth_frame.shape)

depth_colormap = cv.applyColorMap(cv.convertScaleAbs(depth_frame, alpha=0.03), cv.COLORMAP_JET)

display(Image.fromarray( cv.cvtColor(depth_colormap,cv.COLOR_BGR2RGB) ))


#%%
lcam.stopCamera()
# %%
