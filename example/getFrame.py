#%%
import cv2 as cv

from PIL import Image
from IPython.display import display

import os
os.chdir("../")

#%%
from dariusVision import getCameraClass,getVersion

print(getVersion())

#%% generic cv camera
lcam = getCameraClass(type='cv')(vid_src=0)
lcam.startCamera()
lcam.doLastFrame()
# %% realsense camera
lcam = getCameraClass(type='rs2')(vid_src=0)
lcam.startCamera()
# %%


#%%
_,_,frame = lcam.getFrame()
display(Image.fromarray( cv.cvtColor(frame,cv.COLOR_BGR2RGB) ))
# %%
lcam.stopCamera()
# %%
