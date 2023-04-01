# Convert PNG to WEBP and JPG

This is a simple bash script that converts all PNG files in a directory to WEBP and JPG format.

## Usage
You can run this script directly by typing ./convert-png-to-webp-jpg.sh in the terminal, assuming you have the required packages installed. Alternatively, you can use fig to run the script using the command fig run convert-png-to-webp-jpg.

[![asciicast](https://asciinema.org/a/TCDTF7OZHfjM5yyS051ZCaXVr.svg)](https://asciinema.org/a/TCDTF7OZHfjM5yyS051ZCaXVr)

### Using fig
fig is a tool that allows you to run scripts and automate tasks with Docker containers. If you do not have fig installed, you can install it by following the instructions here.

To use fig with this script, add the following to your fig.yml file:

```yaml
scripts:
  convert-png-to-webp-jpg:
    cmd: ["./convert-png-to-webp-jpg.sh"]
```

Then run the command `fig run convert-png-to-webp-jpg` to execute the script.

### Requirements
This script requires the following packages to be installed:

- ImageMagick
- cwebp (only on macOS)

If the required packages are not installed, you will be prompted to install them.
