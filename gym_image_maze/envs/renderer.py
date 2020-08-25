import numpy as np
import pyglet
import ctypes

class Renderer(object):
    @classmethod
    def get_window(cls, display, width, height):
        from pyglet.window import Window
        screen = display.get_screens()[0]
        config = screen.get_best_config()
        context = config.create_context(None)
        return Window(width=width, height=height, config=config, context=context)
    
    def __init__(self, width, height):
        self.display = pyglet.canvas.get_display()
        self.width = width
        self.height = height
        self.window = Renderer.get_window(self.display, width, height) 
    
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
        