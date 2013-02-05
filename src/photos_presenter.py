import os
import tempfile

class PhotosPresenter(object):
    """
    Presenter class for the photo application. Interacts with view and model
    and handles the main logic of the application.
    """
    def __init__(self, model=None, view=None):
        self._model = model
        self._view = view
        self._view.set_presenter(self)
        filters = self._model.get_filter_names()
        self._view.set_filter_names(filters, self._model.get_default_name())

    def _update_view(self):
        temp_path = tempfile.mktemp(".png")
        self._model.save(temp_path)
        self._view.replace_image_from_file(temp_path)
        os.remove(temp_path)

    #UI callbacks...
    def on_close(self):
        # Prompt for save?
        self._view.close_window()

    def on_minimize(self):
        self._view.minimize_window()

    def on_open(self):
        filename = self._view.show_open_dialog()
        if filename != None:
            self._model.open(filename)
            self._view.select_filter(self._model.get_default_name())
            self._update_view()

    def _check_extension(self, filename, original_ext):
        name_arr = filename.split(".")
        ext = name_arr.pop(-1)
        valid = ["jpg", "png", "gif"]
        dot_join = "."
        print name_arr
        # if array is empty, set array to be list with filename as only element
        #if name_arr.empty(): name_arr = 
        if ext not in valid:
            return dot_join.join(name_arr) + "." + original_ext
        return filename
            
    def on_save(self):
        if not self._model.is_open(): return
        
        # Check to see if a file exists with current name
        # If so, we need to add a version extenstion, e.g. (1), (2)
        file_path_list = self._model.get_curr_filename().split("/")
        base_name_arr = file_path_list.pop(-1).split(".")
        name = base_name_arr[0]
        ext = base_name_arr[1]
        str_slash = "/"
        directory_path = str_slash.join(file_path_list)
        i = 1
        curr_name = name
        while(1):
            if not os.path.exists(directory_path + "/" + curr_name + "." + ext):
                break
            curr_name = name + " (" + str(i) + ")" 
            i += 1
        filename = self._view.show_save_dialog(curr_name + "." + ext, directory_path)
        
        filename = self._check_extension(filename, ext)
        print filename


        if filename != None:
            self._model.save(filename)

    def on_share(self):
        print "Share called"

    def on_fullscreen(self):
        print "Fullscreen called"

    def on_filter_select(self, filter_name):
        self._model.apply_filter(filter_name)
        self._update_view()

    # def image_to_pixbuf(self, img):
    #     if img.mode != 'RGB':
    #         img = img.convert('RGB')
    #     buff = StringIO.StringIO()
    #     img.save(buff, 'ppm')
    #     contents = buff.getvalue()
    #     buff.close()
    #     loader = GdkPixbuf.PixbufLoader.new_with_type('pnm')
    #     loader.write(contents)
    #     pixbuf = loader.get_pixbuf()
    #     loader.close()
    #     return pixbuf
