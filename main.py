import handle
import argparse, sys, os
from rich import print

def parse_arg():
    parser = argparse.ArgumentParser(description="An easy Youtube vedio downloader")
    parser.add_argument("-u", "--url", type=str, required=True ,help = "The url of video or playlist")
    parser.add_argument("-cwd", action="store_true", help="Store The music in current Directory")
    parser.add_argument("-dmd", action="store_true", help="Store the music in default music directory")
    return parser.parse_args()

def recognize(url: str, dest):
    if url.startswith("https://youtube.com/watch?v=") or url.startswith("https://youtu.be/") or url.startswith("https://www.youtube.com/watch?v="):
        handle.videohandle(url, dest)
    elif url.startswith("https://www.youtube.com/playlist?list="):
        handle.playlisthandle(url, dest)
    else:
        print("[italic red]Uncorrect URL[/italic red]", locals())
        sys.exit(1)
if __name__ == "__main__":
    args = parse_arg()
    if args.cwd:
        recognize(args.url, os.getcwd())
    elif args.dmd:
        recognize(args.url, os.path.join(os.path.expanduser("~"), "Music"))
    else:
        recognize(args.url, os.path.join(os.path.expanduser("~"), "Music"))