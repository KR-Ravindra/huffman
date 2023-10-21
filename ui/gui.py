import customtkinter
import random
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk


class App(customtkinter.CTk):
    '''
    This class is responsible for creating the GUI and handling the events
    Workflow: UserInput/GUI >> Visualizer >> Sorters
    '''
    def __init__(self):
        super().__init__()        
        self.display=False

        customtkinter.set_appearance_mode("system")
        self.title("Hufman Code")
        x, y = self.center_window(200, 400)
        self.geometry(f"800x600+{x}+{y}")
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        # self.grid_rowconfigure((0, 1, 2), weight=1)

        # create Leftsidebar frame with widgets
        self.left_sidebar_frame = customtkinter.CTkFrame(self,  corner_radius=0)
        self.left_sidebar_frame.grid(row=1, column=1,  sticky="nsew")
        self.left_sidebar_frame.grid_rowconfigure(1, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="Huffman Code", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))


        self.entry = customtkinter.CTkEntry(self.left_sidebar_frame, placeholder_text="Enter Input")
        self.entry.grid(row=1, column=1,  padx=20, pady=10, sticky="nsew")
        self.huffman_button = customtkinter.CTkButton(self.left_sidebar_frame, command=self.generate_button_event, text="Huffman")
        self.huffman_button.grid(row=3, column=1, padx=20, pady=10)

        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.left_sidebar_frame, dynamic_resizing=False,
                                                    #   values=["Encode"])

        # self.optionmenu_1.grid(row=2, column=1, padx=20, pady= 10)


  
    
    def center_window(self,width, height):  # Return for values needed to center Window
        screen_width = self.winfo_screenwidth()  # Width of the screen
        screen_height = self.winfo_screenheight() # Height of the screen     
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        return int(x), int(y)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        
    def generate_button_event(self):        
        self.display=True
        self.entered_input = self.entry.get()

        from algorithms.sorters import huffman_encoding, huffman_decoding
        # if self.optionmenu_1.get() == 'Encode':  
        try:
            self.encoded_message, self.huffman_tree = huffman_encoding(self.entered_input)
            self.decoded_message = huffman_decoding(self.encoded_message, self.huffman_tree)
        except Exception as ex:
            CTkMessagebox(title="Error", message=f"Invalid input! Try again!!\n Exception: {ex}", icon="cancel")
            self.encoded_message = "hello"
            self.entry.delete(0, "end") 
        finally: 
            CTkMessagebox(title="Encode",message=f"Given Input: {self.entered_input} \n Encoded Message: {self.encoded_message} \n Decoded Message: {self.decoded_message}",
                icon="check", options=["Close"], width = 700, height = 300, fade_in_duration = 4)

    def destroy_panel(self):
        self.destroy()   
             
if __name__ == "__main__":
    app = App()
    app.mainloop()
