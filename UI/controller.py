import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._retailer = None

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def load_dd_anno(self):
        anni = self._model.get_anni()
        for a in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(key=a, text=str(a)))
        self._view.update_page()

    def load_dd_brand(self):
        brand = self._model.get_brand()
        for b in brand:
            self._view.dd_brand.options.append(ft.dropdown.Option(key=b, text=str(b)))
        self._view.update_page()

    def load_dd_retailer(self):
        retailer = self._model.get_retailer()
        for r in retailer:
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=r.code, text=r.name, data=retailer, on_click=self.read_retailer))
        self._view.update_page()

    def read_retailer(self, e):
        self._retailer = e.control.data

    def handle_top_vendite(self, e):
        self._view.txt_result.clean()
        anno = self._view.dd_anno.value
        if anno == "Nessun filtro":
            anno = None
        brand = self._view.dd_brand.value
        if brand == "Nessun filtro":
            brand = None
        retailer = self._view.dd_retailer.value
        if retailer == "Nessun filtro":
            retailer = None
        vendite = self._model.get_top_vendite(anno, brand, retailer)
        if len(vendite) == 0:
            self._view.txt_result.controls.append(ft.Text("Nessuna vendita"))
        for v in vendite:
            self._view.txt_result.controls.append(ft.Text(v))
        self._view.update_page()
