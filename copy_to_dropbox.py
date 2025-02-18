import os
import shutil
import datetime

dtime = str(datetime.datetime.now().date())
dest_folder = "/Users/liamrobinson/Library/CloudStorage/Dropbox/progress_PhD/papers/for-review/"
dest_path = os.path.join(dest_folder, f"sdc-attitude-{dtime}.pdf")
shutil.copy("final/paper-final.pdf", dest_path)