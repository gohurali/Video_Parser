__author__ = 'Gohur Ali'
__version__ = 1.2
import cv2
import os
import argparse
import time
import numpy as np
"""
Python script for frame extraction from video files.

How to run:
python3 video_parser.py <video location> <output directory name> <number of frames to skip>

You must have OpenCV and Numpy to be able to run this program as they are dependencies
Files are named YYYYMMDDhourMinute_pictureNum.png
"""

parser = argparse.ArgumentParser(description='Process and Cut Video Frames')
parser.add_argument('input_video', help='name of the directory that the images will be stored in')
parser.add_argument('output_dir', help='the video path in filesystem')
parser.add_argument('seconds_delay',help='number of seconds delayed before frame is saved')
args = parser.parse_args()

video_path = args.input_video

frame_count = 0
vid_cap = cv2.VideoCapture(video_path)

if(os.path.exists(args.output_dir) == False):
    os.mkdir(args.output_dir)
else:
    print('Directory: "',args.output_dir,'" already exists!')

minute = time.localtime().tm_min
hour = time.localtime().tm_hour
day = time.localtime().tm_mday
month = time.localtime().tm_mon
year = time.localtime().tm_year

while(vid_cap.isOpened()):
    if(int(args.seconds_delay) == 0):
        vid_cap.set(cv2.CAP_PROP_POS_MSEC, frame_count)
    elif(int(args.seconds_delay) > 0):
        frame_skip_rate = np.float32( int(frame_count) * int(args.seconds_delay) * 1000)
        vid_cap.set(cv2.CAP_PROP_POS_MSEC,(frame_skip_rate))
    
    ret, frame = vid_cap.read()
    
    if(ret == True):
        im_name = str(year) + str(month) + str(day) + str(hour) + str(minute) + '_'+str(frame_count) + '.png'
        print('Creating image: ', im_name)

        save_loc = args.output_dir + '/' + im_name
        cv2.imwrite(save_loc,frame)
    else:
        break
    frame_count += 1

vid_cap.release()
cv2.destroyAllWindows()

def main():
    pass

if __name__ == "__main__":
    main()