#%%
import cv2 as cv

from PIL import Image
from IPython.display import display

import os

os.chdir("../")

#%%
from dariusVision import getCameraClass,getVersion

print(getVersion())

#%%
lcam = getCameraClass(type='cv')(vid_src=0)
# %%
from dariusVision import rs2_AsyncCam
lcam = rs2_AsyncCam()

# %%
lcam.startCamera()

#%%
_,frame = lcam.getFrame()
display(Image.fromarray( cv.cvtColor(frame,cv.COLOR_BGR2RGB) ))
# %%
lcam.stopCamera()
# %%
