import customtkinter
import os
from PIL import Image
import tkinter
import tkinter as tk
import random
import re
from CTkMessagebox import CTkMessagebox

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

    #  # Create a StringVar to store the input
    #     self.input_var = tk.StringVar()

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("blue")
        self.title("SORT ANALYZER")
        # self.geometry("700x600")
        # import tkinter as tk
        # from tkinter import ttk
        # from matplotlib.figure import Figure
        # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        # from plotter.visualizer import Visualizer
        

        # frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        # frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # visualizer = Visualizer()

        # # Create a FigureCanvasTkAgg widget
        # figure =  visualizer.call_algo([6,3,2,4], "insertion_sort", 0.1)
        # canvas = FigureCanvasTkAgg(figure , master=frame)
        # canvas_widget = canvas.get_tk_widget()
        # canvas_widget.pack(fill=tk.BOTH, expand=True)

        # # Create a function to update the graph (e.g., with new data)
        # def update_graph():
        #     pass
        #     # new_data = [1, 4, 6, 8, 9]  # New data
        #     # canvas.figure = 
        #     # canvas.draw()  # Redraw the canvas

        # # Create a button to update the graph
        # update_button = ttk.Button(self, text="Update Graph", command=update_graph)
        # update_button.pack(pady=10)


                # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="SortAnalyzer", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        # self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        # self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        # self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.combobox_1 = customtkinter.CTkComboBox(self.sidebar_frame, 
        #                                            values=["Insertion Sort", "Bubble Sort", "Counting Sort","Heap Sort","Quick Sort","Merge Sort"])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=10)
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False,
                                                      values=["Insertion Sort", "Bubble Sort", "Counting Sort","Heap Sort","Quick Sort","Merge Sort"])
        self.optionmenu_1.grid(row=1, column=0, padx=20, pady= 10)
        # self.entry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Enter Input",  textvariable = self.input_var)

        self.entry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Enter Input", validate="key", validatecommand=(self.validate_command, '%P'))
        self.entry.grid(row=2, column=0,  padx=20, pady=10, sticky="nsew")
        # Bind the <<Modified>> event to the entry widget
        self.entry.bind("<<Modified>>", self.entry_modified)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.generate_button_event, text="Generate")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.generate_random_array, text="Random Input")
        self.sidebar_button_1.grid(row=4, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
       

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="QUIT", command=self.destroy_panel)
        self.main_button_1.grid(row=3, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
        self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # set default values
        # self.sidebar_button_3.configure(state="disabled", text="Generate")
        self.checkbox_3.configure(state="disabled")
        self.checkbox_1.select()
        self.scrollable_frame_switches[0].select()
        self.scrollable_frame_switches[4].select()
        self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        # self.optionmenu_1.set("CTkOptionmenu")
        self.optionmenu_1.set("Algorithms")
        self.combobox_1.set("CTkCombobox")
        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def validate_command(self,data):
        
        # If the input is empty or matches the pattern of comma-separated integers
        if data == re.match(r'^(\d+(,\s*\d+)*)?$',str(data)):
            return True
        else:
            print('Invalid Input')
            return False
        
    def entry_modified(self, event):
        # Check if the entry content is not empty
        if self.entry.get():
            self.sidebar_button_3.configure(state="normal")
        else:
            self.sidebar_button_3.configure(state="disabled")

    def generate_button_event(self):
      # Retrieve the value of input_var
        self.entered_input = self.entry.get()
        self.entered_input = [int(num.strip()) for num in self.entered_input.split(",")]
        
        from plotter.visualizer import Visualizer
        visualizer = Visualizer(self.entered_input)
        try:
            _ = visualizer.compare_algo()
        except Exception as ex:
            print(f"Exception occured, Given function is not defined {ex}")

        if True:
            msg=CTkMessagebox(message="Sorted Array.",
                  icon="check", option_1="Compare with other algorithms")

            if msg.get()=="Compare with other algorithms":
                visualizer.show_list()

        else:
            CTkMessagebox(title="Error", message="Invalid input! Try again!!", icon="cancel")
        self.entry.delete(0, "end") 

        

    def generate_random_array(self):
        # Generate an array of random numbers (e.g., 10 numbers between 1 and 100)
        random_array = [random.randint(1, 100) for _ in range(10)]
    
        # Convert the array to a string for display
        array_str = ', '.join(map(str, random_array))

        # Update the Entry widget with the generated array
        self.entry.delete(0, "end")  # Clear the previous content
        self.entry.insert(0, array_str)
      
    
    def destroy_panel(self):
        self.destroy()   
             
if __name__ == "__main__":
    app = App()
    app.mainloop()
