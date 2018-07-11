

# Functions for downloading and extracting data-files from the internet. 

import sys
import os
import urllib.request
import tarfile
import zipfile

def _print_download_progress(count, block_size, total_size):
    pct_complete = float(count*block_size)/total_size
    
    msg = "\r- Download progress: {0:.1%}".format(pct_complete)
    
    sys.stdout.write(msg)
    sys.stdout.flush()

def download_and_extract(url, download_dir):
    filename = url.split('/')[-1]
    file_path = os.path.join(download_dir, filename)
    
    if not os.path.exists(file_path):
        if not os.path.exists(download_dir):
            os.mkdirs(download_dir)
        file_path, _ = urllib.request.urlretrieve(url=url,filename=file_path,
                                                 reporthook=_print_download_progress)
        print()
        print("Download finished. Extracting files.")
        if file_path.endswith(".zip"):
            zipfile.ZipFile(file=file_path, mode="r").extractall(download_dir)
        elif file_path.endswith((".tar.gz", ".tgz")):
            tarfile.open(name=file_path, mode="r:gz").extractall(download_dir)

        print("Done.")
    
    else:
        print("Data has apparently already been downloaded and unpacked.")

