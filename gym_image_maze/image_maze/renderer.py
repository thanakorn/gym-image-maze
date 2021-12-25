import numpy as np
import pyglet
import ctypes

class Renderer(object):
    def __init__(self, window):
        self.window = window
    
    def render(self, img_array):
        from pyglet.image import ImageData
        from pyglet.gl import glClearColor
        glClearColor(1,1,1,1)
        img_array = np.ascontiguousarray(img_array[::-1, :])
        img_c_array = img_array.ctypes.data_as(ctypes.POINTER(ctypes.c_float * img_array.size))
        img_data = ImageData(img_array.shape[0], img_array.shape[1], 'L', img_c_array)
        self.window.clear()
        self.window.switch_to()
        self.window.dispatch_events()
        img_data.blit(0, 0)
        self.window.flip()
        
    def close(self):
        self.window.close()