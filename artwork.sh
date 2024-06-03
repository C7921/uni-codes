#!/bin/bash

debug=true # To print or not to print?
new_folder="$HOME/artworks"
num_images=3

if [ -d "$new_folder" ]; then
    $debug && echo "The folder $new_folder already exists."
else
    mkdir "$new_folder"
    $debug && echo "Created folder $new_folder."
fi

download_images() {
    response=$(curl -s "https://api.artic.edu/api/v1/artworks")
    total_count=$(echo "$response" | grep -o '"total":[0-9]*' | grep -o '[0-9]*')
    
    if [ -z "$total_count" ] || [ "$total_count" -le 0 ]; then
        $debug && echo "Failed to retrieve the total number of artworks."
        exit 1
    fi
    
    $debug && echo "Total number of artworks: $total_count"
    
    downloaded_count=0
    attempts=0
    max_attempts=20  # Prevent an infinite loop (not all artworks have ID's)

    while [ $downloaded_count -lt $num_images ] && [ $attempts -lt $max_attempts ]; do
        random_id=$(( ( RANDOM % total_count ) + 1 ))
        response=$(curl -s "https://api.artic.edu/api/v1/artworks/$random_id")
        
        image_id=$(echo "$response" | grep -o '"image_id":"[^"]*' | sed 's/"image_id":"//')
        title=$(echo "$response" | grep -o '"title":"[^"]*' | sed 's/"title":"//' | sed 's/[^a-zA-Z0-9]/_/g')
        
        if [ -n "$image_id" ] && [ "$image_id" != "null" ] && [ -n "$title" ]; then
            image_url="https://www.artic.edu/iiif/2/$image_id/full/843,/0/default.jpg"
            if $debug; then
                wget -O "$new_folder/${title}.jpg" "$image_url"
                echo "Downloaded $image_url as ${title}.jpg"
            else
                wget -O "$new_folder/${title}.jpg" "$image_url" > /dev/null 2>&1
            fi
            downloaded_count=$((downloaded_count + 1))
        else
            $debug && echo "Image ID or title not found for artwork ID $random_id"
        fi
        
        attempts=$((attempts + 1))
    done
    
    if [ $downloaded_count -lt $num_images ]; then
        $debug && echo "Only downloaded $downloaded_count images out of $num_images requested."
    fi
}

download_images
$debug && echo "Images downloaded to $new_folder"