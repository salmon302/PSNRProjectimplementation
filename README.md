I quickly put together this code to get PSNR values from a few videos. You can change the video paths for different videos, I just chose the same spaghetti video with different levels of compression. I think MOS is subjective so I think it's probably not applicable for us. 
I don't recommend making pull requests or anything of the sort as this is just on github for the sake of sharing convenience.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Research Video Quality
I am sorry to say, you guys probably have the most difficult task, because its very open ended without a very specific requirement.
We need a way to measure the performance of our streaming protocols. Specifically for things like latency and vide quality. Security will have to be measured somehow too but later.
Professor Qu threw out some terms at us that might help narrow down the ways to measure streaming performance. These were:
Peak Signal to Noise Ratio (PSNR)
Mean Opinion Score (MOS)
I do not know what they mean. I have been far too busy with other aspects of this project to research these topics, and that is where I will need your team to step in.
It is not enough just to get a basic description. Please try to create implementations that we could use, or describe in detail how an implementation can be created and what you are missing to accomplish that task.
Also, do not limit yourselves to PSNR and MOS. These were things the professor worked on many years ago or he read about them, they might not even be applicable. Research and identify different ways that can be used to quantifiably grade a video stream and try to have an implementation that we could use.
For testing you can try this streaming method that we have working so far. You would need to set up GStreamer using the tutorial:
Make sure to change the values for “path to your movie.mp4” and “receiver_IP”. Both computers should be on the same network for this to work. I think you may also be able to test this within the same computer by simply opening up two different terminals (not certain).
The source (with the video):
gst-launch-1.0 filesrc location= /path/to/your/video.mp4 ! qtdemux ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host= receiver_ip port=5000
The sink (the one receiving the stream)
gst-launch-1.0 udpsrc port=5000 caps="application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264" ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Definitions and Implementation guide ideas:

Peak Signal to Noise Ratio (PSNR): PSNR is a widely used metric to quantify the quality of reconstructed or compressed video. It measures the difference between the original video and the compressed video in terms of signal power versus noise power. Higher PSNR values indicate better video quality.

Mean Opinion Score (MOS): MOS is a subjective metric used to evaluate the overall quality of audio and video streams from the perspective of human perception. It typically involves human observers rating the quality of the stream on a scale.

PSNR Implementation:
Capture Original and Compressed Video: Obtain the original video and the compressed (streamed) video for comparison.

Calculate Mean Squared Error (MSE): Compute the MSE between corresponding pixels of the original and compressed frames.
MSE = (1 / n) * Σ((I_original - I_compressed)^2)

Calculate PSNR: Use the MSE to calculate PSNR using the formula:
PSNR = 10 * log10((MAX^2) / MSE), where MAX is the maximum possible pixel value.

Repeat for Multiple Frames: Perform these steps for multiple frames and calculate an average PSNR value.

MOS Implementation:
Collect Subjective Ratings: Conduct subjective evaluations with human observers who rate the quality of the streamed video using a MOS scale.
Calculate Average MOS: Aggregate the individual ratings to calculate an average MOS score for the video stream.

Video Quality Metrics: Explore other objective quality metrics like Structural Similarity Index (SSI), Video Quality Metric (VQM), or Video Quality Assessment (VQA) algorithms.
Latency Measurement: Measure latency by timestamping frames at the sender and receiver ends, then calculate the time difference.
Security Analysis: For security, consider evaluating encryption methods, packet loss, and network vulnerability assessments.
Regarding testing with GStreamer, ensure you follow the provided tutorial and customize the parameters like the path to the video file and receiver IP address. You can use GStreamer commands to simulate streaming and capture data for evaluation with the implemented metrics.


