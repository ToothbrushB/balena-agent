import subprocess
import time
import os
# print(os.environ)
# lch = subprocess.run(["libcamera-hello", "--list-cameras"], capture_output=True).stdout
vctl = subprocess.run(["v4l2-ctl", "--list-devices"], capture_output=True).stdout
# print(lch)
print(vctl)
# hasPiCam = b"Available cameras\n-----------------\n0" in lch
# vlc = subprocess.Popen(["cvlc","v4l2:///dev/video0", "--rtsp-tcp", "--sout", "#transcode{vcodec=h264,acodec=mpga}:rtp{mux=ts,sdp=rtsp://:554/stream}"])

# if hasPiCam:
#     print("PI CAMERA DETECTED!")
#     # camera = subprocess.Popen(["libcamera-vid", "-t", "0", "--inline", "--nopreview", "--framerate", os.environ['FPS'], "--width", os.environ['WIDTH'], "--height", os.environ['HEIGHT'], "-o", "-"], stdout=subprocess.PIPE)
#     vlc = subprocess.Popen(["cvlc", "v4l2:///dev/video0", "--sout", "#rtp{sdp=rtsp://:554/stream}", ":demux=h264"])
#     # vlc v4l2:///dev/video0 --sout ‘#rtp{mux=ts,sdp=rtsp://IP:PORT/cam.sdp}’ "-rtsp_transport", "tcp""-vcodec", "libx264"
# ffmpeg = subprocess.Popen(["ffmpeg", "-loglevel", "debug", "-i", "/dev/video0", "-r", os.environ['FPS'], "-c:v", "libx264", "-c:a", "aac", "-rtsp_transport", "tcp","-f", "rtsp", "rtsp://192.168.1.31:554/stream"])

# ffmpegtest = subprocess.Popen(["ffmpeg", "-f", "lavfi", "-i", "sine", "-f", "rtsp", "rtsp://192.168.1.31:554/stream"])
ffmpeg2 = subprocess.Popen(["ffmpeg", "-loglevel", "info","-f", "v4l2", "-i", "/dev/video0", "-preset", "ultrafast", "-b:v", "600k", "-c:v","libx264","-f", "rtsp", "rtsp://localhost:8554/mystream"])
# else:
#     #do sum stuff with the webcam or sm
#     print("NO PI CAMERA DETECTED!")
#     pass

"""
libcamera-vid --inline --nopreview -t 0 --width 1920 --height 1080 --framerate 30 --codec h264 -o - | \
  ffmpeg -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -thread_queue_size 1024 \
    -use_wallclock_as_timestamps 1 -i pipe:0 -c:v copy -c:a aac -preset fast -strict experimental \
    -f flv rtmp://a.rtmp.youtube.com/live2/1z39-k1je-281q-k73y-b42w
"""
#libcamera-vid -t 0 --inline --nopreview --framerate 30 --width 640 --height 480 -o - | cvlc stream:///dev/stdin --sout '#std{access=http, mux=ts, dst=:80/stream}' :demux=h264