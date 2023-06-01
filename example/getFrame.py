#%%

from dariusVision import lastest_Cam2,get_version,rs2_AsyncCam
import cv2 as cv

from PIL import Image
from IPython.display import display

print(get_version())
# %%
lcam = rs2_AsyncCam()
# %%
lcam.startCamera()
#%%
_,frame = lcam.getFrame()
# %%
display(Image.fromarray( cv.cvtColor(frame,cv.COLOR_BGR2RGB) ))
# %%
lcam.stopCamera()