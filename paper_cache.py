import os
import shutil
import glob


def cache_file(start_path: str, end_dir: str = "cache"):
    if not os.path.exists(end_dir):
        os.mkdir(end_dir)
    im_name = os.path.split(start_path)[1]
    end_path = os.path.join(end_dir, im_name)
    if not os.path.exists(start_path):
        raise ValueError(f"{start_path} does not exist!")
    shutil.copy(start_path, end_path)


imgs = {
    "/Users/liamrobinson/Documents/maintained-research/mirage/docs/build/html/_images": [
        'sphx_glr_plot_models_001.png',
        'sphx_glr_plot_models_002.png',
        'sphx_glr_plot_lcs_001_2_00x.png',
        'sphx_glr_plot_lcs_002_2_00x.png',
    ],
    "/Users/liamrobinson/Documents/presentations-papers/msthesis/static_images": [
    ],
    "/Users/liamrobinson/Documents/maintained-research/mirage/docs/source/_static": [
        "refs.bib"
    ],
    '/Users/liamrobinson/Documents/maintained-research/mirage/examples/13-attitude-2024/figs':
    glob.glob('/Users/liamrobinson/Documents/maintained-research/mirage/examples/13-attitude-2024/figs/*.png'),
    '/Users/liamrobinson/Documents/maintained-research/mirage/examples/15-attitude-sdc-2025/figs':
    glob.glob('/Users/liamrobinson/Documents/maintained-research/mirage/examples/15-attitude-sdc-2025/figs/*'),
}

for im_dir, im_names in imgs.items():
    for im_name in im_names:
        im_path = os.path.join(im_dir, im_name)
        globs = glob.glob(im_path)
        if not globs:
            raise ValueError(f"Nothing found for pattern {im_name}")
        for f in globs:
            cache_file(start_path=f)
