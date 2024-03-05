#Overview
#This script allows you to download videos from Vimeo by simply providing the video URL. It utilizes the vimeo-downloader Python package to handle the downloading process.

#Prerequisites
#Python: The script requires Python to be installed. You can download and install Python from the official website.

#Installation
#To install the required Python package, run the following command in your terminal or command prompt:

#pip3 install vimeo-downloader

#Usage
#Copy the Vimeo video URL that you want to download.
#Run the script and paste the video URL when prompted.
#The script will download the video to your current directory.


from vimeo_downloader import Vimeo

# Initialize Vimeo object with video URL
url = "https://vimeo.com/702138443"  
v = Vimeo(url)

# Get available video formats
video_formats = v.streams

# Print available video formats
print("Available Formats:")
for stream in video_formats:
    print(stream.quality)

# Choose a format (e.g., '720p')
chosen_format = "540p"

# Find the stream with the chosen format
chosen_stream = None
for stream in video_formats:
    if stream.quality == chosen_format:
        chosen_stream = stream
        break

# Download the video
if chosen_stream:
    chosen_stream.download()
    print("Video downloaded successfully!")
else:
    print("Error in video download or Chosen format not available.")
