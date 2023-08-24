close all
clear all

%% Initialize video writer
outputVideo = VideoWriter('C:\Users\youga\Desktop\BTP\output\New_output_video_30.mp4'); % Change the output file name if needed
outputVideo.FrameRate = 30; % Set the desired frame rate
open(outputVideo);

%% Load PNG files
imageFiles = dir('C:\Users\youga\Desktop\BTP\output\*.png'); % Assuming your PNG files are inside the 'output' folder
NFrames = length(imageFiles);

for ic = 1:NFrames
    % Read the PNG image
    imageFileName = fullfile('output', imageFiles(ic).name);
    img = imread(imageFileName);

    % Write the image to the video
    writeVideo(outputVideo, img);
end

%% Close the video writer
close(outputVideo);