from termcolor import colored
import pyfiglet
banner = pyfiglet.figlet_format("YT LOAD")
about = colored("About", "blue")
decorate = colored("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈", "yellow")

decoration_work = (colored(f"\n\n≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ {about} {decorate}\n\n", "yellow"))

down_dec = colored("\t\tPLEASE WAIT DOWNLODING....", "green")

done = colored("\n\n[+] SUCCESFULLY DOWNLOADED AND SAVED IN CURRENT DIRECTORY\n\n", "green")
