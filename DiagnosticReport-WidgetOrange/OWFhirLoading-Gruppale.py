
from Orange.widgets import widget, gui
from tkinter import filedialog


class OWFhirLoading(widget.OWWidget):
    name = "Loading"
    description = "Upload a fhir resource and trasform it to an orange table where you can develop any analytics you need"
    category = "FHIR Loading Widgets"
    
    class Outputs:
        final_process_table = widget.Output("Processed Data",list)

    def __init__(self):
        super().__init__()

        box = gui.button(self.controlArea, self,label = "Import one or more Json files", callback = self.UploadAction() )
        self.infoa = gui.widgetLabel(
            box, ".")
        self.infob = gui.widgetLabel(box, '')


    def select_paths(self,file_path):
         self.bundle_path = file_path
         print("bundle file path: ",self.bundle_path)
         self.commit()

    def UploadAction(self,event=None):
            file_paths = filedialog.askopenfilenames(
                 title      = "Select json fhir resources"
            )
            if file_paths:
                 print("file paths list: ", file_paths)
                 self.file_paths = file_paths
                 self.commit()
            else:
                 print("selected 0 files")
                 return 
 
                
    def commit(self):
         self.Outputs.final_process_table.send(self.file_paths)
        