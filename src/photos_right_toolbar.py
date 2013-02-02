from gi.repository import Gtk

from image_text_button import ImageTextButton

class PhotosRightToolbar(Gtk.Alignment):
    """
    The right toolbar with post to facebook and save buttons.
    """
    def __init__(self, **kw):
        super(PhotosRightToolbar, self).__init__(xalign=0.5, yalign=0.5, xscale=0.0, yscale=0.0, **kw)

        self._save_button = ImageTextButton(normal_path="../images/save_normal.png",
                                            hover_path="../images/save_hover.png",
                                            down_path="../images/save_down.png",
                                            label_text="SALVAR",
                                            name="save-button")
        self._save_button.connect('clicked', lambda w: self._presenter.on_save())

        self._share_button = ImageTextButton(normal_path="../images/share_normal.png",
                                            hover_path="../images/share_hover.png",
                                            down_path="../images/share_down.png",
                                            label_text="FACEBOOK",
                                            name="share-button")
        self._share_button.connect('clicked', lambda w: self._presenter.on_share())

        self._button_box = Gtk.VBox(homogeneous=False, spacing=20)
        self._button_box.pack_start(self._save_button, expand=False, fill=False, padding=0)
        self._button_box.pack_start(self._share_button, expand=False, fill=False, padding=0)
        self.add(self._button_box)

        self.show_all()

    def set_presenter(self, presenter):
        self._presenter = presenter
