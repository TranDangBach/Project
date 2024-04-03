import tkinter as tk    # Import the tkinter module for creating the GUI
import tkinter.scrolledtext as tkst     # Import the ScrolledText widget for displaying text with scrollbars
import font_manager as fonts    # Import the font_manager module for configuring fonts
import video_library as lib     # Import video library

def set_text(text_area, content):   # Define a function to set the text of a Text or ScrolledText widget
    text_area.delete("1.0", tk.END)     # Delete the existing text in the widget
    text_area.insert(1.0, content)      # Insert the new text into the widget

class CreateVideoList():    # Define a class for creating a video list GUI
    def __init__(self, window):      # Initialize the class with a window parameter
        window.geometry("750x400")      # Set the window size to 750x400 pixels
        window.title("Create Video List")   # Set the window title to "Create Video List"

        self.video_list = []    # Initialize an empty list for storing video keys

        self.add_video_btn = tk.Button(window, text="Add Video", command=self.add_video_clicked)    # Create a button to add videos to the list
        self.add_video_btn.grid(row=0, column=2, padx=10, pady=10)      # Place the List Add Video button in the GUI at row 0, column 2, with horizontal and vertical padding of 10 pixels

        enter_lbl = tk.Label(window, text="Enter Video Number")     # Create a label to display the text "Enter Video Number"
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)    # Place the label in the GUI at row 0, column 0, with horizontal and vertical padding of 10 pixels

        self.input_txt = tk.Entry(window, width=3)      # Create a text entry field for the user to enter the video number
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)      # Place the Entry widget in the GUI at row 0, column 1, with horizontal and vertical padding of 10 pixels

        self.play_btn = tk.Button(window, text="Play", command=self.play_clicked)   # Create a button to play the video list
        self.play_btn.grid(row=2, column=0, padx=10, pady=10)   # Place the Play button in the GUI at row 2, column 0, with horizontal and vertical padding of 10 pixels

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")     # Create a ScrolledText widget to display the list of videos
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)     # Place the ScrolledText widget in the GUI at row 1, column 0, spanning across columns 0, 1, and 2,with a sticky attribute set to "W" for left alignment, and horizontal and vertical padding of 10 pixels

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")   # Create a Text widget to display messages related to the video list
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)     # Place the Text widget for displaying video details in the GUI at row 1, column 3, with a sticky attribute set to "NW" for top-left alignment, and horizontal and vertical padding of 10 pixels

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))     # Create a new Label widget for displaying status messages with an empty initial text, Helvetica font and a font size of 10
        self.status_lbl.grid(row=2, column=2, columnspan=4, sticky="W", padx=10, pady=10)   # Placed in the GUI at row 2, column 2, spanning across columns 2 to 5, with a sticky attribute set to "W" for left alignment, and horizontal and vertical padding of 10 pixels.

        self.reset_btn = tk.Button(window, text="Reset", command=self.reset_clicked)    # Create a button to reset the video list
        self.reset_btn.grid(row=2, column=1, padx=10, pady=10)      # Place the Reset button in the GUI at row 2, column 1, with horizontal and vertical padding of 10 pixels

    def add_video_clicked(self):    # Define a function to add a video to the list
        key = self.input_txt.get()  # Get the video number from the text entry field
        name = lib.get_name(key)    # Get the name of the video with the given key
        self.input_txt.delete(0, tk.END)  # Clear the text entry field
        self.status_lbl.configure(text="Add Video button was clicked!")     # Update the status label with a message

        if name is not None:    # Check if the video exists
            if key not in self.video_list:  # Check if the video is already in the list
                self.video_list.append(key)     # Add the video key to the list
                self.list_txt.insert(tk.END, f"{name}\n")   # Add the name of the video to the list widget
                set_text(self.video_txt, f"Video {key} added\n")    # Display a message in the video widget
            else:
                set_text(self.video_txt, f"Video {key} already\n")  # Display a message in the video widget
        else:
            set_text(self.video_txt, "Invalid video number\n")      # Display a message in the video widget
    def play_clicked(self):     # Define a function to play the video list
        self.status_lbl.configure(text="Play button was clicked!")      # Update the status label with a message
        if self.video_list:     # Check if the list is not empty
            for video_number in self.video_list:    # Iterate over the video list
                lib.increment_play_count(video_number)    # Increment the play count for the current video
            set_text(self.video_txt, "Playlist played\n")   # Display a message in the video widget
        else:
            set_text(self.video_txt, "Playlist is empty\n")     # Display a message in the video widget

    def reset_clicked(self):    # Define a function to reset the video list
        self.status_lbl.configure(text="Reset button was clicked!")     # Update the status label with a message
        self.video_list.clear()     # Clear the video list
        self.list_txt.delete("1.0", tk.END)     # Clear the list widget
        set_text(self.video_txt, "Playlist reset\n")   # Display a message in the video widget

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CreateVideoList(window) # open the CreateVideoList GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc

