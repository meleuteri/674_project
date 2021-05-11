from google_drive_downloader import GoogleDriveDownloader as drvdl
import tarfile

# Download the las file tar and places it into the zips folder

fid = "1VKm05i-4fIi7xtws668LSmECbZTbvbEm"
fname = "dales_semantic_segmentation_las.tar.gz"
pth = "./zips/" + fname

# Calling a function that pulls data from a drive link.  Built in unzipper does not work for tar.gz
drvdl.download_file_from_google_drive(file_id=fid,
                                    dest_path=pth,
                                    unzip=False)

# Extracts the file in the zips folder and adds it to the
tar = tarfile.open(pth, "r:gz")
tar.extractall()
tar.close()

# Download the txt file tar and places it into the zips folder

fid = "1dCYRFBwxsi7c8SZRHyZIObfyEzdl9sVS"
fname = "dales_semantic_segmentation_txt.tar.gz"
pth = "./zips/" + fname

# Calling a function that pulls data from a drive link.  Built in unzipper does not work for tar.gz
drvdl.download_file_from_google_drive(file_id=fid,
                                    dest_path=pth,
                                    unzip=False)

# Extracts the file in the zips folder and adds it to the
tar = tarfile.open(pth, "r:gz")
tar.extractall()
tar.close()

# Download the las file tar and places it into the zips folder

fid = "1kNQygxgOABrxQXDlxpv5poHTkXkhKrAn"
fname = "dales_semantic_segmentation_ply.tar.gz"
pth = "./zips/" + fname

# Calling a function that pulls data from a drive link.  Built in unzipper does not work for tar.gz
drvdl.download_file_from_google_drive(file_id=fid,
                                    dest_path=pth,
                                    unzip=False)

# Extracts the file in the zips folder and adds it to the
tar = tarfile.open(pth, "r:gz")
tar.extractall()
tar.close()
