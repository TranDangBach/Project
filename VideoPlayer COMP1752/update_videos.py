import tkinter as tk    # Import tkinter library for GUI creation
import font_manager as fonts    # Import the font manager
import video_library as lib     # Import video library

def set_text(text_area, content):   # Set the text of a Text widget in a tkinter GUI
    text_area.delete("1.0", tk.END)     # Delete existing content
    text_area.insert(1.0, content)      # Insert new content
class UpdateVideos():    # Class UpdateVideos to create the GUI
    def __init__(self, window):     # Initialize the UpdateVideos class and creates the GUI
        window.geometry("550x350")      # Set the window size to 550x350 pixels
        window.title("Update Videos")   # Set the window title to "Update Videos"

        enter_lbl = tk.Label(window, text="Enter Video Number")     # Create a new label with text "Enter Video Number"
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)   # Place the label in the GUI at row 0, column 0, with horizontal and vertical padding of 10 pixels

        self.input_video_number = tk.Entry(window, width=3)  # Create a new Entry widget with width 3 for video number
        self.input_video_number.grid(row=0, column=1, padx=10, pady=10)      # Place the Entry widget in the GUI at row 0, column 1, with horizontal and vertical padding of 10 pixels

        enter_new_rating_lbl = tk.Label(window, text="Enter New Rating")     # Create a new label with text "Enter New Rating"
        enter_new_rating_lbl.grid(row=0, column=2, padx=10, pady=10)   # Place the label in the GUI at row 0, column 2, with horizontal and vertical padding of 10 pixels

        self.input_new_rating = tk.Entry(window, width=5)  # Create a new Entry widget with width 5 for new rating
        self.input_new_rating.grid(row=0, column=3, padx=10, pady=10)      # Place the Entry widget in the GUI at row 0, column 3, with horizontal and vertical padding of 10 pixels

        update_video_btn = tk.Button(window, text="Update Video", command=self.update_video_clicked)    # Create a new button with text "Update Video" and set the command to handle button click
        update_video_btn.grid(row=2, column=0, padx=10, pady=10)     # Place the button in the GUI at row 2, column 0, with horizontal and vertical padding of 10 pixels

        self.video_details_txt = tk.Text(window, width=50, height=10, wrap="none")   # Create a new Text widget for displaying video details with a width of 50 characters, a height of 10 lines, and does not wrap text to the next line
        self.video_details_txt.grid(row=1, column=0, columnspan=4, padx=10, pady=10)     # Place the Text widget for displaying video details in the GUI at row 1, column 0, spanning across columns 0 to 3, with horizontal and vertical padding of 10 pixels

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) # Create a new Label widget for displaying status messages with an empty initial text, Helvetica font and a font size of 10
        self.status_lbl.grid(row=2, column=1, columnspan=4, sticky="W", padx=10, pady=10)     # Place the Label widget for displaying status messages in the GUI at row 2, column 1, spanning across columns 1 to 4, with horizontal and vertical padding of 10 pixels

    def update_video_clicked(self):  # Function to handle the "Update Video" button click
        try:
            self.status_lbl.configure(text="Update Video button was clicked!")
            video_number = self.input_video_number.get()  # Get the video number from the Entry widget
            name = lib.get_name(video_number)   # Get the name of the video with the given video number
            self.input_video_number.delete(0, tk.END)    # Clear the video number entry field
            if name is not None:    # Check if the video exists
                new_rating = int(self.input_new_rating.get())  # Get the new rating from the Entry widget
                self.input_new_rating.delete(0, tk.END)  # Clear the new rating entry field
                if new_rating < 0:  # If the new rating is less than 0
                    set_text(self.video_details_txt, "New Rating must be non-negative\n")   # Display an error message
                elif new_rating > 5:    # If the new rating is greater than 5
                    set_text(self.video_details_txt, "Sorry, highest rating allowed is 5!\n")   # Display an error message
                else:   # If the new rating is valid
                    lib.set_rating(video_number, new_rating)    # Update the rating of the video
                    video_details = f"Video Name: {name}\nNew Rating: {new_rating}\nPlay Count: {lib.get_play_count(video_number)}\n"   # Get the updated details of the video
                    set_text(self.video_details_txt, video_details)     # Display the updated video details
            else:   # If the video number is invalid
                set_text(self.video_details_txt, "Invalid video number\n")  # Display an error message
        except ValueError:  # If a ValueError is raised
            set_text(self.video_details_txt, "New Rating must be integer\n")    # Display an error message

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    UpdateVideos(window)    # open the UpdateVideos GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc