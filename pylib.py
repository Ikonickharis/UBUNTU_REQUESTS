import requests
import os
import hashlib
from urllib.parse import urlparse

MAX_FILE_SIZE_MB = 10  # Limit file size to 10MB
SUPPORTED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/gif", "image/webp"}

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    return filename if filename else "downloaded_image.jpg"

def hash_content(content):
    return hashlib.sha256(content).hexdigest()

def is_duplicate_image(image_hash, hash_set):
    return image_hash in hash_set

def fetch_image(url, saved_hashes, save_dir):
    try:
        headers = {
            "User-Agent": "UbuntuImageFetcher/1.0 (respectful-client)"
        }
        with requests.get(url, stream=True, headers=headers, timeout=10) as response:
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "").lower()
            content_length = response.headers.get("Content-Length")

            if content_type not in SUPPORTED_IMAGE_TYPES:
                print(f"✗ Skipped: Unsupported content type ({content_type}) from {url}")
                return

            if content_length and int(content_length) > MAX_FILE_SIZE_MB * 1024 * 1024:
                print(f"✗ Skipped: File too large (> {MAX_FILE_SIZE_MB}MB) from {url}")
                return

            content = response.content
            image_hash = hash_content(content)

            if is_duplicate_image(image_hash, saved_hashes):
                print(f"✗ Skipped: Duplicate image from {url}")
                return

            filename = get_filename_from_url(url)
            filepath = os.path.join(save_dir, filename)

            # Ensure unique filename in case of name collision
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(filepath):
                filepath = os.path.join(save_dir, f"{base}_{counter}{ext}")
                counter += 1

            with open(filepath, 'wb') as f:
                f.write(content)

            saved_hashes.add(image_hash)
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Saved to: {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred with {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A mindful tool for responsibly collecting images\n")

    urls_input = input("Please enter image URLs (separated by commas or new lines):\n")
    urls = [url.strip() for url in urls_input.replace('\n', ',').split(',') if url.strip()]

    if not urls:
        print("✗ No valid URLs provided.")
        return

    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)
    saved_hashes = set()

    for url in urls:
        fetch_image(url, saved_hashes, save_dir)

    print("\nMission complete. Ubuntu in action — safety, respect, and sharing.")

if __name__ == "__main__":
    main()
