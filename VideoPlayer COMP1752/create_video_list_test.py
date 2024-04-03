import tkinter as tk    # Import tkinter library for GUI creation
from create_video_list import CreateVideoList   # Import CreateVideoList Class
import video_library as lib     # Import video library

window = tk.Tk()    # create a TK object
app = CreateVideoList(window)  # open the CreateVideoList GUI to test

def test_add_video():
    # Add 2 video to the list
    # Set input values
    app.input_txt.delete(0, tk.END)
    app.input_txt.insert(0, "01")

    # Perform action
    app.add_video_clicked()

    # Check output
    assert app.list_txt.get("1.0", tk.END).strip() == "Tom and Jerry"
    assert app.video_txt.get("1.0", tk.END).strip() == "Video 01 added"
    assert app.status_lbl.cget("text") == "Add Video button was clicked!"

    # Set input values
    app.input_txt.delete(0, tk.END)
    app.input_txt.insert(0, "02")

    # Perform action
    app.add_video_clicked()

    # Check output
    assert app.list_txt.get("1.0", tk.END).strip() == "Tom and Jerry\nBreakfast at Tiffany's"
    assert app.video_txt.get("1.0", tk.END).strip() == "Video 02 added"
    assert app.status_lbl.cget("text") == "Add Video button was clicked!"

    # Add a video to the list but the video is available in the list
    # Set input values
    app.input_txt.delete(0, tk.END)
    app.input_txt.insert(0, "01")

    # Perform action
    app.add_video_clicked()

    # Check output
    assert app.list_txt.get("1.0", tk.END).strip() == "Tom and Jerry\nBreakfast at Tiffany's"
    assert app.video_txt.get("1.0", tk.END).strip() == "Video 01 already"
    assert app.status_lbl.cget("text") == "Add Video button was clicked!"

    # Entering an invalid video number
    # Set input values
    app.input_txt.delete(0, tk.END)
    app.input_txt.insert(0, "one")

    # Perform action
    app.add_video_clicked()

    # Check output
    assert app.list_txt.get("1.0", tk.END).strip() == "Tom and Jerry\nBreakfast at Tiffany's"
    assert app.video_txt.get("1.0", tk.END).strip() == "Invalid video number"
    assert app.status_lbl.cget("text") == "Add Video button was clicked!"

def test_reset():
    # Perform action
    app.reset_clicked()

    # Check output
    assert app.list_txt.get("1.0", tk.END).strip() == ""
    assert app.status_lbl.cget("text") == "Reset button was clicked!"

def test_play():
    # When there is no video in the list
    # Perform action
    app.play_clicked()

    # Check output
    assert app.video_txt.get("1.0", tk.END).strip() == "Playlist is empty"
    assert app.status_lbl.cget("text") == "Play button was clicked!"

    # When there are 2 videos in the list
    # Set input values and add videos to the list
    app.input_txt.delete(0, tk.END)
    app.input_txt.insert(0, "01")
    app.add_video_clicked()
    app.input_txt.delete(0, tk.END)
    app.input_txt.insert(0, "02")
    app.add_video_clicked()

    # Perform action
    app.play_clicked()

    # Check output
    assert app.video_txt.get("1.0", tk.END).strip() == "Playlist played"
    assert app.status_lbl.cget("text") == "Play button was clicked!"
    assert lib.get_play_count("01") == 1
    assert lib.get_play_count("02") == 1