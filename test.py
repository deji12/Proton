

url = 'https://res.cloudinary.com/dxojb4izx/video/upload/v1652735982/Colliding_Particles_Logo_Reveal_free_lwnbic.mp4'

import progressbar
import urllib.request


pbar = None


def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None


urllib.request.urlretrieve(url, 'proton.mp4', show_progress)