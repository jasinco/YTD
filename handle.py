from rich import print
from rich.prompt import Prompt

def playlisthandle(url: str, dest):
    from pytube import Playlist
    p = Playlist(url)
    for i, x in enumerate(p.videos):
        print("[italic yellow]{0}[/italic yellow]: [italic]{1}[/italic]".format(i,x.title))
    check = Prompt.ask("[red bold]Install ALL?[/red bold]", choices=["y","n"], default="y")
    if check == "y":
        for i in p.video_urls:
            videohandle(i, dest)
def videohandle(url:str, dest):
    from pytube import YouTube
    from rich.progress import Progress
    yt = YouTube(url)
    final = yt.streams.get_audio_only()
    with Progress() as progress:
        task = progress.add_task("[yellow]Downloading...[/yellow]{:10s}".format(final.title),total=final.filesize)
        def prog(_chun, _d,byt_rem):
            progress.update(task, completed=final.filesize-byt_rem, refresh=True)
        yt.register_on_progress_callback(prog)
        final.download(dest)