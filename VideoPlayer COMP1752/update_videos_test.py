import tkinter as tk    # Import tkinter library for GUI creation
from update_videos import UpdateVideos  # Import UpdateVideos Class

def test_update_video():

    window = tk.Tk()    # create a TK object
    app = UpdateVideos(window)  # open the UpdateVideos GUI to test

    # Test the update_video button when entering a valid video number and a valid new rating

    # Set input values
    app.input_video_number.delete(0, tk.END)
    app.input_video_number.insert(0, "01")
    app.input_new_rating.delete(0, tk.END)
    app.input_new_rating.insert(0, "3")

    # Perform action
    app.update_video_clicked()

    # Check output
    assert app.video_details_txt.get("1.0", tk.END).strip() == "Video Name: Tom and Jerry\nNew Rating: 3\nPlay Count: 0"
    assert app.status_lbl.cget("text") == "Update Video button was clicked!"

    # Test the update_video button when entering a valid video number and a new rating greater than 5

    # Set input values
    app.input_video_number.delete(0, tk.END)
    app.input_video_number.insert(0, "02")
    app.input_new_rating.delete(0, tk.END)
    app.input_new_rating.insert(0, "6")

    # Perform action
    app.update_video_clicked()

    # Check output
    assert app.video_details_txt.get("1.0", tk.END).strip() == "Sorry, highest rating allowed is 5!"
    assert app.status_lbl.cget("text") == "Update Video button was clicked!"

    # Test the update_video button when entering a valid video number and a new rating less than 5

    # Set input values
    app.input_video_number.delete(0, tk.END)
    app.input_video_number.insert(0, "03")
    app.input_new_rating.delete(0, tk.END)
    app.input_new_rating.insert(0, "-1")

    # Perform action
    app.update_video_clicked()

    # Check output
    assert app.video_details_txt.get("1.0", tk.END).strip() == "New Rating must be non-negative"
    assert app.status_lbl.cget("text") == "Update Video button was clicked!"

    # Test the update_video button when entering a valid video number and a new rating, but new rating is not an integer

    # Set input values
    app.input_video_number.delete(0, tk.END)
    app.input_video_number.insert(0, "02")
    app.input_new_rating.delete(0, tk.END)
    app.input_new_rating.insert(0, "four")

    # Perform action
    app.update_video_clicked()

    # Check output
    assert app.video_details_txt.get("1.0", tk.END).strip() == "New Rating must be integer"
    assert app.status_lbl.cget("text") == "Update Video button was clicked!"

    # Test the update_video button when entering an invalid video number

    # Set input values
    app.input_video_number.delete(0, tk.END)
    app.input_video_number.insert(0, "four")
    app.input_new_rating.delete(0, tk.END)
    app.input_new_rating.insert(0, "3")

    # Perform action
    app.update_video_clicked()

    # Check output
    assert app.video_details_txt.get("1.0", tk.END).strip() == "Invalid video number"
    assert app.status_lbl.cget("text") == "Update Video button was clicked!"
