import tkinter as tk    # Import tkinter library for GUI creation
import tkinter.scrolledtext as tkst     # Import ScrolledText widget from tkinter library
import video_library as lib     # Import video library
import font_manager as fonts    # Import the font manager
from PIL import Image, ImageTk  # Import Pillow for handling images in the GUI
def set_text(text_area, content):   # Set the text of a Text widget in a tkinter GUI
    text_area.delete("1.0", tk.END)     # Delete existing content
    text_area.insert(1.0, content)      # Insert new content

class CheckVideos():    # Class CheckVideos to create the GUI
    def __init__(self, window):     # Initialize the class with a window parameter
        window.geometry("750x400")      # Set window size
        window.title("Check Videos")    # Set window title

        self.search_entry = tk.Entry(window, width=48)  # Create a new Entry widget with width 15
        self.search_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)   # Place the Entry widget in the GUI at row 1, column 0, spanning across columns 0, 1, and 2 with horizontal and vertical padding of 10 pixels

        search_btn = tk.Button(window, text="Search", command=self.search_videos_clicked)   # Create a new button with text "Search" and set the command to handle button click
        search_btn.grid(row=1, column=3, padx=10, pady=10)  # Place the button in the GUI at row 1, column 3, with horizontal and vertical padding of 10 pixels

        self.video_image = tk.Label(window)   # Create a new Label widget for displaying images
        self.video_image.grid(row=2, column=3, sticky="S", padx=10, pady=10)    # Placed in the GUI at row 2, column 3 with a sticky attribute set to "S" for bot alignment, and horizontal and vertical padding of 10 pixels.

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)   # Create a new button with text "List All Videos" and set the command to handle button click
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)     # Place the List All Videos button in the GUI at row 0, column 0, with horizontal and vertical padding of 10 pixels

        enter_lbl = tk.Label(window, text="Enter Video Number")     # Create a new label with text "Enter Video Number"
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)   # Place the label in the GUI at row 0, column 1, with horizontal and vertical padding of 10 pixels

        self.input_txt = tk.Entry(window, width=3)  # Create a new Entry widget with width 3
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)      # Place the Entry widget in the GUI at row 0, column 2, with horizontal and vertical padding of 10 pixels

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)    # Create a new button with text "Check Video" and set the command to handle button click
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)     # Place the button in the GUI at row 0, column 3, with horizontal and vertical padding of 10 pixels

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")     # Create a new ScrolledText widget for displaying the list of videos with a width of 48 characters, a height of 12 lines, and does not wrap text to the next line
        self.list_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)     # Place the ScrolledText widget in the GUI at row 2, column 0, spanning across columns 0, 1, and 2,with a sticky attribute set to "W" for left alignment, and horizontal and vertical padding of 10 pixels

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")   # Create a new Text widget for displaying video details with a width of 24 characters, a height of 4 lines, and does not wrap text to the next line
        self.video_txt.grid(row=2, column=3, sticky="NW", padx=10, pady=10)     # Place the Text widget for displaying video details in the GUI at row 2, column 3, with a sticky attribute set to "NW" for top-left alignment, and horizontal and vertical padding of 10 pixels

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) # Create a new Label widget for displaying status messages with an empty initial text, Helvetica font and a font size of 10
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # Placed in the GUI at row 3, column 0, spanning across columns 0 to 3, with a sticky attribute set to "W" for left alignment, and horizontal and vertical padding of 10 pixels.

        self.list_videos_clicked()      # Calling the list_videos_clicked function

    def check_video_clicked(self):   # Method to check video details when the Check Video button is clicked
        key = self.input_txt.get()      # Get the video key from the input_txt Entry widget
        name = lib.get_name(key)    # Get video name using the key
        self.input_txt.delete(0, tk.END)  # Clear the text entry field
        if name is not None:    # If video is found in the library
            director = lib.get_director(key)    # Get director of the video
            rating = lib.get_rating(key)    # Get rating of the video
            play_count = lib.get_play_count(key)    # Get play count of the video
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"    # Create a string with video details
            set_text(self.video_txt, video_details)     # Display video details in the video_txt Text widget
            image = Image.open(lib.get_image(key))      # Open the video image file
            resized_image = image.resize((180, 130))    # Resize the image
            photo = ImageTk.PhotoImage(resized_image)   # Convert the image to a format usable by the tkinter Label widget
            self.video_image.configure(image=photo)     # Update the video_image Label widget with the new image
            self.video_image.image = photo  # Keep a reference to the photo object
        else:   # If video is not found
            set_text(self.video_txt, f"Video {key} not found")  # Display a error message in the video_txt Text widget
            self.status_lbl.configure(image=None)  # Update the video_image Label widget
            self.video_image.image = None   # Keep the reference to the photo object
        self.status_lbl.configure(text="Check Video button was clicked!")   # Update the status Label widget to indicate the Check Video button was clicked

    def list_videos_clicked(self):  # Method to list all videos when the List All Videos button is clicked
        video_list = lib.list_all()     # Get a list of all videos in the library
        set_text(self.list_txt, video_list)     # Display the list of videos in the list_txt ScrolledText widget
        self.status_lbl.configure(text="List Videos button was clicked!")   # Update the status Label widget to indicate the List All Videos button was clicked
    def search_videos_clicked(self):    # Method to search for videos
        query = self.search_entry.get().strip()     # Get the user input from the search Entry widget
        search_results = ""     # Initialize an empty string to store the search results
        for key in lib.library:     # Iterate over the video library
            item = lib.library[key]     # Get the video item
            if query == key:    # Check if the search term is the same as the video number
                search_results += f"{key} {item.info()}\n"  # Add the video details to search results
            elif query.lower() == lib.get_name(key).lower():    # Check if the search term is the same as the video name
                search_results += f"{key} {item.info()}\n"  # Add the video details to search results
            elif query.lower() == lib.get_director(key).lower():    # Check if the search term is the same as the video director
                search_results += f"{key} {item.info()}\n"  # Add the video details to search results
        set_text(self.list_txt, search_results) # Display the search results in the list_txt ScrolledText widget
        if search_results == "":    # Check if any videos are found
            set_text(self.video_txt, f"No video related to {query}")    # Display the message in the video_txt Text widget
        self.status_lbl.configure(text="Search button was clicked!")    # Update the status Label widget to indicate the Search button was clicked

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
