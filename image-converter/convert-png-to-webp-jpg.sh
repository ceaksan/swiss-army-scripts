#!/bin/bash

# Check the OS
if [[ $(uname -s) == "Linux" ]]; then
  # Check if Imagemagick is installed
  if ! command -v convert &> /dev/null; then
      echo "Imagemagick not found. Do you want to install it? (y/n)"
      read -r install_imagemagick
      if [[ "$install_imagemagick" =~ ^[Yy]$ ]]; then
        sudo apt-get update
        sudo apt-get install -y imagemagick
      else
        echo "Aborting script."
        exit 1
      fi
  fi
elif [[ $(uname -s) == "Darwin" ]]; then
  # Check if Imagemagick and cwebp are installed
  if ! command -v convert &> /dev/null || ! command -v cwebp &> /dev/null; then
      echo "Imagemagick or cwebp not found. Do you want to install them? (y/n)"
      read -r install_imagemagick_cwebp
      if [[ "$install_imagemagick_cwebp" =~ ^[Yy]$ ]]; then
        brew install imagemagick webp
      else
        echo "Aborting script."
        exit 1
      fi
  fi
else
  echo "Unsupported OS. This script only supports Linux and macOS."
  exit 1
fi

# Prompt user for directory path
DIR=$(pwd)

echo "This script will convert all PNG files in the current directory to JPG and WebP format."
echo "The converted files will be saved in the same directory as the original PNG files."
echo "The current directory is $DIR"
read -p "Do you want to continue with this directory or specify a different directory? (y/n)" -r
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  read -p "Enter the directory path where the PNG files are located: " -r DIR
  if [[ ! -d "$DIR" ]]; then
    echo "Directory not found. Aborting script."
    exit 1
  fi
  cd "$DIR"
fi

# Check for PNG files
PNG_FILES=(*.png)
if [ ${#PNG_FILES[@]} -eq 0 ]; then
    echo "No PNG files found in current directory."
    exit 1
else
    echo "Found ${#PNG_FILES[@]} PNG file(s) in current directory:"
    for file in "${PNG_FILES[@]}"; do
        echo "- $file"
    done
fi

# Ask user to proceed
read -p "Do you want to proceed with converting these files? (y/n)" -r
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborting script."
    exit 1
fi

# Convert PNG files to JPG and WEBP
for file in "${PNG_FILES[@]}"; do
    filename=$(basename -- "$file")
    extension="${filename##*.}"
    filename="${filename%.*}"
    if [[ $(uname -s) == "Darwin" ]]; then
      cwebp "$file" -quiet -o "${DIR}/${filename}.webp"
    fi
    convert "$file" "$DIR/$filename.jpg"
    convert "$file"
