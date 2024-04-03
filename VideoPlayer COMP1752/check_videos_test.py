import tkinter as tk    # Import tkinter library for GUI creation
from check_videos import CheckVideos    # Import CheckVideos Class


window = tk.Tk()    # create a TK object
app = CheckVideos(window)  # open the CheckVideos GUI to test

def test_list_videos():

    # Perform action
    app.list_videos_clicked()

    # Check output
    assert app.list_txt.get("1.0",tk.END).strip() == "01 Tom and Jerry - Fred Quimby ****\n02 Breakfast at Tiffany's - Blake Edwards *****\n03 Casablanca - Michael Curtiz **\n04 The Sound of Music - Robert Wise *\n05 Gone with the Wind - Victor Fleming ***"
    assert app.status_lbl.cget("text") == "List Videos button was clicked!"

def test_check_video():
    # Entering a valid video number
    # Set input values
    app.input_txt.delete(0, tk.END)
    app.input_txt.insert(0, "01")

    # Perform action
    app.check_video_clicked()

    # Check output
    assert app.video_txt.get("1.0", tk.END).strip() == "Tom and Jerry\nFred Quimby\nrating: 4\nplays: 0"
    assert app.status_lbl.cget("text") == "Check Video button was clicked!"


    # Entering an invalid video number
    # Set input values
    app.input_txt.delete(0, tk.END)
    app.input_txt.insert(0, "one")

    # Perform action
    app.check_video_clicked()

    # Check output
    assert app.video_txt.get("1.0", tk.END).strip() == "Video one not found"
    assert app.status_lbl.cget("text") == "Check Video button was clicked!"

def test_search_videos():
    # When typing the video number
    # Set input values
    app.search_entry.delete(0, tk.END)
    app.search_entry.insert(0, "01")

    # Perform action
    app.search_videos_clicked()

    # Check output
    assert app.list_txt.get("1.0",tk.END).strip() == "01 Tom and Jerry - Fred Quimby ****"
    assert app.status_lbl.cget("text") == "Search button was clicked!"

    # When typing the video name
    # Set input values
    app.search_entry.delete(0, tk.END)
    app.search_entry.insert(0, "breakfast at tiffany's")

    # Perform action
    app.search_videos_clicked()

    # Check output
    assert app.list_txt.get("1.0",tk.END).strip() == "02 Breakfast at Tiffany's - Blake Edwards *****"
    assert app.status_lbl.cget("text") == "Search button was clicked!"

    # When typing the video director
    # Set input values
    app.search_entry.delete(0, tk.END)
    app.search_entry.insert(0, "Michael Curtiz")

    # Perform action
    app.search_videos_clicked()

    # Check output
    assert app.list_txt.get("1.0",tk.END).strip() == "03 Casablanca - Michael Curtiz **"
    assert app.status_lbl.cget("text") == "Search button was clicked!"

    # When typing an invalid value
    # Set input values
    app.search_entry.delete(0, tk.END)
    app.search_entry.insert(0, "four")

    # Perform action
    app.search_videos_clicked()

    # Check output
    assert app.list_txt.get("1.0", tk.END).strip() == ""
    assert app.video_txt.get("1.0", tk.END).strip() == "No video related to four"
    assert app.status_lbl.cget("text") == "Search button was clicked!"