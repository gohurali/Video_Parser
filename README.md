# Video Parser for Frame Extraction

This is script can help obtain images from a video capture that can be used for collecting image data.

### Usage

Obtaining frames from an input video
```
$ python3 parser.py --input_video location/to/video.MOV --output_dir frames/here/ --seconds_delay 1
```
`--seconds_delay` represents the time interval in which a frame will be saved (e.g. `--seconds_delay 2.5` would parse a frame every 2.5 seconds of the video.

Gathering frames to create gif
```
$ python3 parser.py --make-gif --frames_path frames/here/ --output_loc video/placed/here/
```

### Dependencies
* Numpy
    * `pip install numpy`
* OpenCV
    * `pip install opencv-python`
* tqdm
    * `pip install tqdm`
* imageio
    * `pip install imageio`
