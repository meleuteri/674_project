from google_drive_downloader import GoogleDriveDownloader as drvdl
import tarfile
import argparse

def dl_las(unzip):
    print("Downloading las files... ")
    # Download the las file tar and places it into the zips folder

    fid = "1VKm05i-4fIi7xtws668LSmECbZTbvbEm"
    fname = "dales_semantic_segmentation_las.tar.gz"
    pth = "./zips/" + fname

    # Calling a function that pulls data from a drive link.  Built in unzipper does not work for tar.gz
    drvdl.download_file_from_google_drive(file_id=fid,
                                        dest_path=pth,
                                        unzip=False)

    if(unzip):
        # Extracts the file in the zips folder and adds it to the
        print("Unzipping...")
        tar = tarfile.open(pth, "r:gz")
        tar.extractall()
        tar.close()

def dl_txt(unzip):
    print("Downloading txt files... ")
    # Download the txt file tar and places it into the zips folder

    fid = "1dCYRFBwxsi7c8SZRHyZIObfyEzdl9sVS"
    fname = "dales_semantic_segmentation_txt.tar.gz"
    pth = "./zips/" + fname

    # Calling a function that pulls data from a drive link.  Built in unzipper does not work for tar.gz
    drvdl.download_file_from_google_drive(file_id=fid,
                                        dest_path=pth,
                                        unzip=False)

    if(unzip):
        # Extracts the file in the zips folder and adds it to the
        print("Unzipping...")
        tar = tarfile.open(pth, "r:gz")
        tar.extractall()
        tar.close()

def dl_ply(unzip):
    print("Downloading ply files... ")

    # Download the ply file tar and places it into the zips folder

    fid = "1kNQygxgOABrxQXDlxpv5poHTkXkhKrAn"
    fname = "dales_semantic_segmentation_ply.tar.gz"
    pth = "./zips/" + fname

    # Calling a function that pulls data from a drive link.  Built in unzipper does not work for tar.gz
    drvdl.download_file_from_google_drive(file_id=fid,
                                        dest_path=pth,
                                        unzip=False)

    if(unzip):
        # Extracts the file in the zips folder and adds it to the
        print("Unzipping...")
        tar = tarfile.open(pth, "r:gz")
        tar.extractall()
        tar.close()

def main(args):
    if args.all:
        print("Downloading all files")
        dl_las(args.unzip)
        dl_txt(args.unzip)
        dl_ply(args.unzip)
    else:
        if args.dl_las:
            dl_las(args.unzip)
        if args.dl_txt:
            dl_txt(args.unzip)
        if args.dl_ply:
            dl_ply(args.unzip)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DeepSDF')

    parser.add_argument("-a", "--all", action="store_true", help="Use tag to download everything at once")

    # paths you may want to adjust, but it's better to keep the defaults
    parser.add_argument("--unzip", default=True, type=str, help="Unziping the downloads or not.  ")
    parser.add_argument("--dl_las", default=False, type=str, help="Whether or not we download the las files")
    parser.add_argument("--dl_txt", default=False, type=str, help="Whether or not we download the txt files")
    parser.add_argument("--dl_ply", default=False, type=str, help="Whether or not we download the ply files")

    print(parser.parse_args())
    main(parser.parse_args())
