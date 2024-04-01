import cv2
import numpy as np


def calculate_mse_psnr(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file:", video_path)
        return None, None

    prev_frame = None
    mse_values = []
    psnr_values = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if prev_frame is not None:
            mse = np.mean((prev_frame - frame) ** 2)
            psnr = 10 * np.log10((255 ** 2) / mse) if mse > 0 else float('inf')

            mse_values.append(mse)
            psnr_values.append(psnr)

        prev_frame = frame.copy()

    cap.release()

    return mse_values, psnr_values


def compare_videos(video_paths):
    results = []
    for video_path in video_paths:
        mse_values, psnr_values = calculate_mse_psnr(video_path)
        if mse_values is not None and psnr_values is not None:
            avg_mse = np.mean(mse_values)
            avg_psnr = np.mean(psnr_values)
            results.append({'Video': video_path, 'Average MSE': avg_mse, 'Average PSNR': avg_psnr})
        else:
            results.append({'Video': video_path, 'Average MSE': None, 'Average PSNR': None})

    return results


# Example usage
video_paths = ['How To Cook The Perfect Pasta _ Gordon Ramsay.mp4', 'How To Cook The Perfect Pasta _ Gordon Ramsay 2.mp4', 'How To Cook The Perfect Pasta _ Gordon Ramsay 3.mp4']
comparison_results = compare_videos(video_paths)

# Print the results in a table format
print("Video Comparison Results:")
print("{:<20} {:<15} {:<15}".format('Video', 'Average MSE', 'Average PSNR'))
for result in comparison_results:
    video_name = result['Video'].split('/')[-1]  # Extracting just the video filename
    avg_mse = result['Average MSE']
    avg_psnr = result['Average PSNR']
    print("{:<20} {:<15.4f} {:<15.4f}".format(video_name, avg_mse, avg_psnr))
