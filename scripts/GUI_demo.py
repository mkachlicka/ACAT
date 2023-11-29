## Requirements
# customtkinter==5.2.1
# darkdetect==0.8.0
# packaging==23.2
# python-dateutil==2.8.2
# pytz==2023.3.post1
# six==1.16.0
# tzdata==2023.3

import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("blue")  

class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        checkbox = customtkinter.CTkCheckBox(self, text=item)
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10), sticky="w")
        self.checkbox_list.append(checkbox)

    def remove_item(self, item):
        for checkbox in self.checkbox_list:
            if item == checkbox.cget("text"):
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
                return

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Speech Rate Tool Demo")

        #frame for file selection + naming tools
        self.filebrowse1_frame = customtkinter.CTkFrame(self)
        self.filebrowse1_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 5), sticky="nsew")
        self.filebrowse1_frame.grid_columnconfigure((0), weight=1)

        # select input dir
        self.entry1_label = customtkinter.CTkLabel(master=self.filebrowse1_frame, text="Input folder:", fg_color="transparent")
        self.entry1_label.grid(row=0, column=0, columnspan=1, padx=(5, 5), pady=(10, 10), sticky="e")
        self.entry1_text = customtkinter.StringVar()
        self.entry1 = customtkinter.CTkEntry(master=self.filebrowse1_frame, textvariable = self.entry1_text, width=200)
        self.entry1.grid(row=0, column=1, columnspan=1, padx=(5, 5), pady=(10, 10), sticky="nsew")
        self.entry1_button = customtkinter.CTkButton(master=self.filebrowse1_frame, text="Browse", width=8, command=self.entry1_button_clicked)
        self.entry1_button.grid(row=0, column=2, columnspan=1, padx=(5, 10), pady=(10, 10), sticky="nsew")

        # select output dir
        self.entry2_label = customtkinter.CTkLabel(master=self.filebrowse1_frame, text="Output folder:")
        self.entry2_label.grid(row=1, column=0, columnspan=1, padx=(10, 5), pady=(10, 10), sticky="e")
        self.entry2_text = customtkinter.StringVar()
        self.entry2 = customtkinter.CTkEntry(master=self.filebrowse1_frame, textvariable = self.entry2_text, width=200)
        self.entry2.grid(row=1, column=1, columnspan=1, padx=(5, 5), pady=(10, 10), sticky="nsew")
        self.entry2_button = customtkinter.CTkButton(master=self.filebrowse1_frame, text="Browse", width=8, command=self.entry2_button_clicked)
        self.entry2_button.grid(row=1, column=2, columnspan=1, padx=(5, 10), pady=(10, 10), sticky="nsew")

        # enter filename
        self.filename_label = customtkinter.CTkLabel(master=self.filebrowse1_frame, text="Save as:", fg_color="transparent")
        self.filename_label.grid(row=2, column=0, columnspan=1, padx=(5, 5), pady=(10, 10), sticky="e")
        self.filename = customtkinter.CTkEntry(master=self.filebrowse1_frame, width=200)
        self.filename.grid(row=2, column=1, columnspan=1, padx=(5, 5), pady=(10, 10), sticky="nsew")
        self.xlsx_label = customtkinter.CTkLabel(master=self.filebrowse1_frame, text=".csv", fg_color="transparent")
        self.xlsx_label.grid(row=2, column=2, columnspan=1, padx=(5, 5), pady=(10, 10), sticky="w")

        # select values to export
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=150, height=50,
                                                                 item_list=['option ' + str(i+1) for i in range(10)], 
                                                                 label_text="Select Metrics to export")
        self.scrollable_checkbox_frame.grid(row=3, column=0, columnspan=3, rowspan=1, padx=10, pady=(5,5), sticky="nesw")

        # convert to csv + open when done (Y/N)
        self.convert_frame = customtkinter.CTkFrame(self)
        self.convert_frame.grid(row=4, column=0, padx=(10, 10), pady=(5, 10), sticky="nsew", columnspan=3)
        self.convert_frame.grid_columnconfigure((1,2), weight=1)
        switch_var = customtkinter.StringVar(value="on")
        self.openyn_switch = customtkinter.CTkSwitch(master=self.convert_frame, text="Open when done", command=self.switch_yn, variable=switch_var)
        self.openyn_switch.grid(row=0, column=0, columnspan=1, padx=(10, 5), pady=(10, 10), sticky="s")
        self.convert_button = customtkinter.CTkButton(master=self.convert_frame, text="Export ", width=70, command=self.convert_button_clicked)
        self.convert_button.grid(row=0, column=2, columnspan=1, padx=(5, 10), pady=(10, 10), sticky="se")

    def entry1_button_clicked(self):
        readin = tk.filedialog.askdirectory(title='Select the folder containing raw data')
        self.entry1_text.set(readin)

    def entry2_button_clicked(self):
        readin = tk.filedialog.askdirectory(title='Select where to save proccessed data')
        self.entry2_text.set(readin)

    def switch_yn(self):
        pass

    def convert_button_clicked(self):
        #### add desired function here
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()