from pytube import YouTube 
import os, time, sys
import pyfiglet

from termcolor import colored

os.system('clear')

print(colored(pyfiglet.figlet_format("\tYo Music"), "red"))

print(colored("\n\n>> Developed By Suraj Sharma <<\n\n", "green"))

def audio_downloader():
	
	try:
		
		yt = YouTube(
		
		str(input(colored("\n\nEnter the URL of the video you want to download: \n\n>> ", "magenta"))))
		
		status = colored("\n\n\n\t      Please Wait Downloading....\n\n", "green")
		
		for stats in status:
		    sys.stdout.write(stats)
		    sys.stdout.flush()
		    time.sleep(0.1)
		
	

		
		video = yt.streams.filter(only_audio=True).first() 
		
		
		
		print(colored("\n\nEnter the destination (leave blank for current directory)", "blue"))
		
		destination = str(input(colored("\n>> ", "yellow")))or '.'
		
		
		out_file = video.download(output_path=destination) 
		
		
		
		base, ext = os.path.splitext(out_file) 
		
		new_file = base + '.mp3'
		os.rename(out_file, new_file) 
		
		
		
		print(colored("\n\n"+yt.title + " has been successfully downloaded And Saved ✓", "green"))
	
	except Exception as Error:
		print(colored("\n\nSomething Error Has Occured ! Please Check your internet Connection. And the link You have Entered !\n\n", "red"))
		
	audio_downloader()
	
audio_downloader()
