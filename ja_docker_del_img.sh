#!/bin/bash

# Function to delete Docker image
delete_image() {
    docker image rm "$1"
    if [ $? -eq 0 ]; then
        echo "Image with ID $1 deleted successfully."
    else
        echo "Failed to delete image with ID $1."
    fi
}

# List Docker images
echo "Available Docker images:"
docker image ls

# Prompt user for image ID
read -p "Enter the ID of the image you want to delete: " image_id

# Check if the image ID exists
if docker image inspect "$image_id" &> /dev/null; then
    # Image exists, confirm deletion
    read -p "Are you sure you want to delete the image with ID $image_id? (y/n): " confirm
    if [ "$confirm" = "y" ]; then
        delete_image "$image_id"
    else
        echo "Deletion aborted."
    fi
else
    echo "Image with ID $image_id not found."
fi

