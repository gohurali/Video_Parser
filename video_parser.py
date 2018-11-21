__author__ = 'Gohur Ali'
__version__ = 1.2
import cv2          # Opening video and grabbing frames
import os           # Directory searching
import argparse     # Command line arguement seeting
import time         # Getting current time for naming convention
import numpy as np  # Python float to Numpy float conversion
"""
Python script for frame extraction from video files.

How to run:
python3 video_parser.py <video location> <output directory name> <number of frames to skip>

Note: 
0 for the number of frames to skip with give all the frames within the video
5 will save a frame for every 5 seconds in the video

You must have OpenCV and Numpy to be able to run this program as they are dependencies:
    To install OpenCV:
        pip install opencv-python
    To install numpy
        pip install numpy

Output images are named YYYYMMDDhourMinute_pictureNum.png
"""

parser = argparse.ArgumentParser(description='Process and Cut Video Frames')
parser.add_argument('input_video', help='name of the directory that the images will be stored in')
parser.add_argument('output_dir', help='the video path in filesystem')
parser.add_argument('seconds_delay',help='number of seconds delayed before frame is saved')
args = parser.parse_args()

def get_current_time():
    '''
    Using time module to get current time and using it 
    as a time convention.
    '''
    minute = time.localtime().tm_min
    hour = time.localtime().tm_hour
    day = time.localtime().tm_mday
    month = time.localtime().tm_mon
    year = time.localtime().tm_year
    return minute, hour, day, month, year

def parse_video(args):
    '''
    Grabbing particular frames from the video capture and saving them to disk
    at a given location that is taken from the command line.

    :param: Arguments taken from the command line
    '''
    video_path = args.input_video
    frame_count = 0
    vid_cap = cv2.VideoCapture(video_path)
    minute, hour, day, month, year = get_current_time()

    if(os.path.exists(args.output_dir) == False):
        os.mkdir(args.output_dir)
    else:
        print('Directory: "',args.output_dir,'" already exists!')

    while(vid_cap.isOpened()):
        if(int(args.seconds_delay) == 0):
            vid_cap.set(cv2.CAP_PROP_POS_MSEC, frame_count)
        elif(int(args.seconds_delay) > 0):
            frame_skip_rate = np.float32( int(frame_count) * int(args.seconds_delay) * 1000)
            vid_cap.set(cv2.CAP_PROP_POS_MSEC,(frame_skip_rate))

        ret, frame = vid_cap.read()
        
        if(ret == True):
            im_name = str(year) + str(month) + str(day) + str(hour) + str(minute) + '_' +str(frame_count) + '.png'
            print('Creating image: ', im_name)
            save_loc = args.output_dir + '/' + im_name
            cv2.imwrite(save_loc,frame)
        else:
            break
        frame_count += 1

    vid_cap.release()
    cv2.destroyAllWindows()

def main():
    parse_video(args)

if __name__ == '__main__':
    main()