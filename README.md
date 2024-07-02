# imza.py

This project generates a signature in GIF format and uploads it to Imgur. The project creates visual effects with customized text and background code on the signature.

## Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Example Image](#example-image)

## Features
- Creates a GIF signature with specified dimensions (800x300).
- Customizable font, color, and background code for the signature.
- Uploads the created GIF to Imgur and provides a BBCode formatted link.

## Installation

1. Install the necessary Python libraries:
    ```bash
    pip install pillow imageio requests
    ```

2. Download or copy the `imza.py` file to your computer.

## Usage

1. Run the script:
    ```bash
    python imza.py
    ```

2. After running the script, the `imza.gif` file will be created and uploaded to Imgur.

3. If the upload is successful, you will see a BBCode formatted link in the terminal. You can use this link in forums.

## Requirements

- Python 3.6 or higher
- The following Python libraries:
  - Pillow
  - imageio
  - requests

- Imgur API Client ID (used in the `upload_to_imgur` function as specified in the project)

## Contributing

If you would like to contribute, please submit a pull request. We welcome all contributions and feedback.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.

## Example Image

![Example GIF](https://i.imgur.com/XZXUBsA.gif)

---

**Made with ❤ by @Fridibuck**
