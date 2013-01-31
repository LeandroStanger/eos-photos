import os
import Image
import StringIO

class PhotosPresenter(object):
    def __init__(self, model=None, view=None):
        self._model = model
        self._view = view
        self._view.set_presenter(self)

    def close(self):
        # Prompt for save?
        self._view.close_window()

    def minimize(self):
        self._view.minimize_window()

    def open(self):
        filename = self._view.present_dialog()
        self._model.set_current_image(filename)
        self.update_view()
        # call update view here
        
    def update_view(self):
        new_image = self._model.get_current_image()
        self._view.replace_image(new_image)

    def image_to_pixbuf(self, img):
        if img.mode != 'RGB':
            img = img.convert('RGB')
        buff = StringIO.StringIO()
        img.save(buff, 'ppm')
        contents = buff.getvalue()
        buff.close()
        loader = GdkPixbuf.PixbufLoader.new_with_type('pnm')
        loader.write(contents)
        pixbuf = loader.get_pixbuf()
        loader.close()
        return pixbuf

    def save(self):
        print "Save called"

    def share(self):
        print "Share called"

