import tkinter as tk    # Import tkinter library for GUI creation
import font_manager as fonts    # Import the font manager
from check_videos import CheckVideos    # Import CheckVideos Class
from create_video_list import CreateVideoList   # Import CreateVideoList Class
from update_videos import UpdateVideos  # Import UpdateVideos Class

def check_videos_clicked():     # Function for Check Videos button
    status_lbl.configure(text="Check Videos button was clicked!")   # Update the status label with a message
    CheckVideos(tk.Toplevel(window))    # Create a CheckVideos window that is a child of the main window

def create_video_list_clicked():    # Function for Create Video List button
    status_lbl.configure(text="Create Video List button was clicked!")  # Update the status label with a message
    CreateVideoList(tk.Toplevel(window))    # Create a CreateVideoList window that is a child of the main window

def update_videos_clicked():    # Function for Update Videos button
    status_lbl.configure(text="Update Videos button was clicked!")  # Update the status label with a message
    UpdateVideos(tk.Toplevel(window))   # Create a UpdateVideos window that is a child of the main window


window = tk.Tk()    # create a TK object
window.geometry("520x150")  # Set the window size to "520x150" pixels
window.title("Video Player")    # Set the window title to "Video Player"

fonts.configure()   # Configure the font

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")     # Create a header label with text "Select an option by clicking one of the buttons below"
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)    # Place the label in the GUI at row 0, column 0, spanning across columns 0 to 2 with horizontal and vertical padding of 10 pixels

check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)     # Create a new button with text "Check Videos" and set the command to handle button click
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)    # Place the button in the GUI at row 1, column 0, with horizontal and vertical padding of 10 pixels

create_video_list_btn = tk.Button(window, text="Create Video List", command=create_video_list_clicked)  # Create a new button with text "Create Video List" and set the command to handle button click
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)   # Place the button in the GUI at row 1, column 1, with horizontal and vertical padding of 10 pixels

update_videos_btn = tk.Button(window, text="Update Videos", command=update_videos_clicked)  # Create a new button with text "Update Videos" and set the command to handle button click
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)   # Place the button in the GUI at row 1, column 2, with horizontal and vertical padding of 10 pixels

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))  # Create a new Label widget for displaying status messages with an empty initial text, Helvetica font and a font size of 10
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)    # Place the Label widget for displaying status messages in the GUI at row 2, column 0, spanning across columns 0 to 2, with horizontal and vertical padding of 10 pixels

window.mainloop()   # run the window main loop, reacting to button presses, etc
