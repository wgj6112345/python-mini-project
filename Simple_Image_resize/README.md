# Image Resizing Script

This script is designed to resize images in a specified directory using Python and the Pillow library. It iterates through all files in the directory, checks if they are images, and then resizes them according to a specified compression ratio. The resized images are saved in a different directory. it can be used for creating thumbnails or compressing image

## Requirements

- Python 3.x
- Pillow library (PIL)

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the Pillow library using pip:


## Usage

1. Place your images in the `source` directory.
2. Modify the `compression_ratio` variable in the script to adjust the size of the resized images. A value of 1 will keep the original size, values greater than 1 will enlarge the images, and values less than 1 will reduce the images.
3. Run the script:

4. The resized images will be saved in the `resized` directory.

## Configuration

- `directory`: The directory containing the original images. Default is 'source'.
- `compressed_directory`: The directory where the resized images will be saved. Default is 'resized'.
- `compression_ratio`: The ratio by which to resize the images. Default is 1.5.

## Notes

- The script checks if a file is an image before attempting to resize it.
- The resized images retain their original file names but are saved in the specified `compressed_directory`.
- The script ensures that the `compressed_directory` exists before saving the resized images.

## 🤖 Author
[amar sree](https://github.com/amarsree)


## License

This project is licensed under the MIT License. See the LICENSE file for details.
