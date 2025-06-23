import os
import random
import time
import requests
from duckduckgo_search import DDGS
from duckduckgo_search.exceptions import RatelimitException


def search_and_download_images(query: str, limit: int = 5, output_dir: str = "downloads", retries=5, backoff=3):
    os.makedirs(output_dir, exist_ok=True)
    results = search_image(query, limit, retries, backoff)

    if results and len(results)>0:
        i = random.randint(0, len(results) - 1)
        result = results[i]
        url = result["image"]
        ext = os.path.splitext(url)[-1]
        print(f'ext: {ext}')
        return download_image(query, url, output_dir, i, ext)
    return None

def search_image(query, limit, retries, backoff):
    for attempt in range(retries):
        try:
            results = DDGS().images(keywords=query, max_results=limit)
            if not results:
                print("No images found.")
                return None
            return results
        except RatelimitException as e:
            wait = backoff * (2 ** attempt)
            print(f"Rate limited or failed to fetch. Retrying in {wait}s... ({e})")
            time.sleep(wait)
    else:
        print("Failed to fetch images after multiple attempts.")
        return None

def download_image(query, url, output_dir, i , ext):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            filename = os.path.join(output_dir, f"{query.replace(' ', '_')}_{i}{ext}")
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
            return filename
    except Exception as e:
        print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    img_query = input("Enter image search query: ")
    search_and_download_images(img_query)
