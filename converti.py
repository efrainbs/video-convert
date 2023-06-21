import os
import subprocess


folder_path = os.getcwd()

for filename in os.listdir(folder_path):
    if filename.endswith(".avi"):
            
        new_file = filename[:-4]
        os.mkdir(f'nuevo_{new_file}')

        input_path = os.path.join(folder_path, filename)
        output_path = os.path.join(f'nuevo_{new_file}', f'{new_file}.mp4')

        ffmpeg_convert = f'ffmpeg -i {input_path} {output_path}'
        subprocess.run(ffmpeg_convert, shell=True)

        ffmpeg_crop = f'ffmpeg -i {output_path} -filter:v "crop=1500:1100:520:120" {output_path[:-4]}_crop.mp4'
        subprocess.run(ffmpeg_crop, shell=True)

        ffmpeg_images = f'ffmpeg -i {output_path[:-4]}_crop.mp4 -vf fps=1/10 {output_path[:-4]}_%d.jpg'
        subprocess.run(ffmpeg_images, shell=True)

        ffmpeg_short = f'ffmpeg -i {output_path[:-4]}_crop.mp4 -ss 00:00:30 -t 8 {output_path[:-4]}_short.MP4'
        subprocess.run(ffmpeg_short, shell=True)

        ffmpeg_gif = f'ffmpeg -i {output_path[:-4]}_crop.mp4 -ss 00:00:30 -t 6 {output_path[:-4]}_gif.gif'
        subprocess.run(ffmpeg_gif, shell=True)

