import os
import time
from concurrent.futures import ThreadPoolExecutor

import yt_dlp


def download_video(url, output_path='youtube_downloads'):
    """Download a single YouTube video using yt-dlp"""
    try:
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'best',  # Download best quality
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': True,
            'extract_flat': False,
            'writethumbnail': False
        }
        
        # Create downloader instance
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            ydl.download([url])
            return True
            
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False

def main():
    # List of YouTube video URLs
    urls = [
        "https://www.youtube.com/watch?v=eUXBPf2uM6k",
        "https://www.youtube.com/embed/F-M14KmMHQ0",
        "https://www.youtube.com/embed/BM0Eno-WgUY",
        "https://www.youtube.com/embed/Ls4HaNVBIQY",
        "https://www.youtube.com/embed/3TWwsAlOwM8",
        "https://www.youtube.com/embed/K2szXXdmIbM",
        "https://www.youtube.com/embed/ElG5sO3euH8",
        "https://www.youtube.com/embed/biGm5ASMhkw",
        "https://www.youtube.com/embed/1OhdX3RwXBY",
        "https://www.youtube.com/embed/fy6j3mfaTC4",
        "https://www.youtube.com/embed/R4DQ7rUdde4",
        "https://www.youtube.com/embed/pEhAp-JXsHY",
        "https://www.youtube.com/embed/H_hsViHhXxA",
        "https://www.youtube.com/embed/vZNR4EMaj7w",
        "https://www.youtube.com/embed/dDpYYAKp-zw",
        "https://www.youtube.com/embed/QTMr7wjl7Fk",
        "https://www.youtube.com/embed/9r_PkI8GUJU",
        "https://www.youtube.com/embed/YFYIf5Gq6Ik",
        "https://www.youtube.com/embed/hTNmbc4AMbw",
        "https://www.youtube.com/embed/hjJRlhq250w",
        "https://www.youtube.com/embed/Mz0ntZmugg4",
        "https://www.youtube.com/embed/bmQJ9XhZTLo",
        "https://www.youtube.com/embed/CqEvunx40mY",
        "https://www.youtube.com/embed/DX5QCZhpqrw",
        "https://www.youtube.com/embed/EDaHxAOdeYI",
        "https://www.youtube.com/embed/4Gc6QB_SKoM",
        "https://www.youtube.com/embed/uP6T-vdhqlI",
        "https://www.youtube.com/embed/B8tyTRSWfSQ",
        "https://www.youtube.com/embed/nE8S9rHg-f8",
        "https://www.youtube.com/embed/doIZzQhJAmE",
        "https://www.youtube.com/embed/eyHGRtuqU-w",
        "https://www.youtube.com/embed/B54-efwR5c0",
        "https://www.youtube.com/embed/xQ_LckCX1pI",
        "https://www.youtube.com/embed/wktp1ycjIu4",
        "https://www.youtube.com/embed/k1VSI0kE1U8",
        "https://www.youtube.com/embed/j91IVsgYZs4",
        "https://www.youtube.com/embed/HEUMrJhVOTc",
        "https://www.youtube.com/embed/t8urx_G1Gfk",
        "https://www.youtube.com/embed/qDj1TWBOlBA",
        "https://www.youtube.com/embed/CNLKRV5EwI0"
    ]
    
    # Create output directory
    output_path = "youtube_downloads"
    os.makedirs(output_path, exist_ok=True)
    
    # Download videos using thread pool for parallel downloads
    print(f"Starting download of {len(urls)} videos...")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(lambda url: download_video(url, output_path), urls))
    
    # Print summary
    successful = sum(1 for r in results if r)
    failed = len(urls) - successful
    total_time = time.time() - start_time
    
    print("\nDownload Summary:")
    print(f"Total videos: {len(urls)}")
    print(f"Successfully downloaded: {successful}")
    print(f"Failed: {failed}")
    print(f"Total time: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()