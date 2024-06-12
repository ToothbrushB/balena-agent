# python demo.py &
udevadm control --reload

# libcamera-hello --list-cameras -n -v
# libcamera-hello --version
# libcamera-jpeg -o /data/lcc2.jpg # THIS WORKS!!!

# python demo.py

# cd mediamtx_v1.3.0_linux_armv7
# ./mediamtx
# sleep infinity
export FPS=30
export WIDTH=640
export HEIGHT=480
python start.py
sleep infinity
# ffmpeg -f video4linux2 -input_format h264 -video_size 1280x720 -framerate 30 -i /dev/video0 -vcodec copy -an test.h264
# cd /data
# python -m http.server 80
