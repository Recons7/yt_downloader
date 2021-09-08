import pafy
import os, sys, time
from normal import decoration_work, down_dec, done, banner
import pyfiglet
from termcolor import colored, cprint

def song_dload():
	try:
		os.system('clear')
		print(colored(banner, "red"))
		url = input(colored("\n\nEnter Url Of Video : ", 'cyan', attrs=['dark', 'bold']))
		
		video = pafy.new(url) 
		
		print(decoration_work)
		
		print(colored(f"{video}", "magenta"))
		
		print(decoration_work)
		
		for downloading in down_dec:
			sys.stdout.write(downloading)
			sys.stdout.flush()
			time.sleep(0.1)
			
		bestaudio = video.getbestaudio() 
		bestaudio.download() 
		
		if 'm4a' in str(bestaudio):
			file_rename = os.rename(f'{video.title}.m4a', f'{video.title}.mp3')
		elif 'webm.part' in str(bestaudio):
			file_rename = os.rename(f'{video.title}.webm.part', f'{video.title}.mp3')
		else:
			file_rename = os.rename(f'{video.title}.webm', f'{video.title}.mp3')
		
		for downloaded in done:
			sys.stdout.write(downloaded)
			sys.stdout.flush()
			time.sleep(0.1)
	except Exception as error:
		print(colored(f'[ - ] {error}\n\n', 'red'))
		
		time.sleep(5)
		
	song_dload()
song_dload()
		
