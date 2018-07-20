from PythonGUI import get_form_root
from config import init_gui

form_root = get_form_root()

init_gui(form_root[0])

form_root[1].mainloop()
