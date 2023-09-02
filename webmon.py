import os
import cmd
import requests
import validators

class Webmon(cmd.Cmd):

    intro = "\n#### Website Monitoring ####\n"
    prompt = '(webmon)'

    def __init__(self, config_file='webmon.conf', max_url_length=1000):      
        
        super().__init__()
        self.monctl_config_file = config_file
        self.max_url_length = 1000

        self.fp_config_file = ''
        self.monitored_items = []
        
        self._load_config()
        
    def config(self):
        return str(self.monctl_config_file)
    
    def _load_config(self):

        if os.path.isfile(self.monctl_config_file):
            try:
                self.fp_config_file = open(self.config(), 'r')
                self.monitored_items = list(map(str.strip, self.fp_config_file.readlines()))
                self.fp_config_file.close()
            
            except FileNotFoundError:
                print("[Error]: The file " + self.config() + " does not exist.")

            except IOError as e:
                print(f"[Error]: An error occurred while reading the file - {e}")

            except Exception as e:
                # Handle any other unexpected errors
                print(f"[Error]: An unexpected error occurred: {e}")

    def _save(self):
        
        try: 
            self.fp_config_file = open(self.config(), "w")

            if len(self.monitored_items) > 0:
                for i, d in enumerate(self.monitored_items):
                    if i == len(self.monitored_items) - 1:
                        self.fp_config_file.write(d)
                    else:
                        self.fp_config_file.write(d + "\n")
                
                print("Saved all in a list of monitoring websites: " + self.config())
            else:
                print("No websistes in the monitoring list")
            
            self.fp_config_file.close()

        except FileNotFoundError:
            print("[Error]: The file " + self.config() + " does not exist.")

        except IOError as e:
            print(f"Error: An error occurred while writing the file - {e}")

        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")

    def do_save(self, arg):
        self._save()
    
    def help_save(self):
        print("Save a list of websites in the configuration file\n")
        print('Usage:')
        print('  save')
       
    def _bye(self):
        print("\nHappy to help! Bye\n")

    def do_list(self, arg):
        if len(self.monitored_items) > 0:
            for item in self.monitored_items: 
                print(item)
        else:
            print("No websites in the monitoring list")

    def help_list(self):
        print("Show a list of monitoring websites\n")
        print('Usage:')
        print('  list')

    def do_add(self, arg): 

        if not arg:
            print("Usage: add <Website URL>\n")
            print("Please specify a website (ex: https://www.google.com)")
        elif not validators.url(arg):
            print("Please verify that your enter a valid website (example: https://www.google.com)")
        elif arg in self.monitored_items:
            print("Website " + arg + " has been already in the monitoring list, so skipped to add it.")
        elif len(arg) > int(self.max_url_length): 
            print("The maximum length is " + str(self.max_url_length) + " characters. Please verify and try again")    
        else:
            print("Website " + str(arg) + " added to the monitoring list")
            self.monitored_items.append(arg)

    def help_add(self):

        print("Add a website to a list of monitoring websites\n")
        print('Usage:')
        print('  add <Website URL>')
        print('Examples:')
        print('  add https://www.google.com   add the Google website to a list of the monitoring websites')
        print('  add http://httpforever.com   add the HTTP Forever website to a list of the monitoring websites')

    def do_remove(self, arg):

        if not arg:
            print("Usage: remove <Website URL>\n")
            print("Please specify a website to delete from a list of monitoring websites")
        elif arg not in self.monitored_items:
            print("Website " + arg + " not found in the monitoring list")
        else:
            self.monitored_items.remove(arg)
            print("Website " + arg + " removed from the monitoring list")

    def help_remove(self):

        print("Remove a website from a list of monitoring websites\n")
        print('Usage:')
        print('  remove <Website URL>')
        print('Examples:')
        print('  remove https://www.google.com   remove the Google website from a list of the monitoring websites')

    def do_check(self, arg):

        if len(self.monitored_items) == 0:
            print("No websites in the monitoring list")
        else:
            
                for website in self.monitored_items:
                    
                    if website:
                        try:
                            if validators.url(website):
                                response = requests.get(website, timeout=5)

                                if response.status_code == 200:
                                    print(website + ": connected")
                                else:
                                    print(website + ": disconnected")
                            else:
                                continue

                        except requests.ConnectionError:
                            print(website + ": disconnected") 
                        except Exception as e:
                            print(website + ": disconnected") 
                    else:
                        continue

    def help_check(self):
        print("Check the network connectivity from a list of monitoring websites\n")
        print('Usage:')
        print('  check')
        print('Examples:')
        print('  check')
        print('  https://www.google.com: connected')
        print('  https://this-web-is-down.com: disconnected')

    def do_quit(self, arg):
        self._bye()
        exit(0)

    def help_quit(self):
        print("Exit the website monitoring\n")
        print('Usage:')
        print('  quit')
        
    def do_EOF(self, line):
        self._bye()
        exit(0)
    
    def help_EOF(self):
        print("Exit the website monitorin by the Ctrl + D\n")
        print('Usage:')
        print('  Press the Ctrl + D key')

    def default(self, line):
        print("\nWebsite Monitoring Tool\n")
        print("Usage:\n")
        print("  add <Website URL>          Add a website to a list of monitoring websites\n")
        print("  remove <Website URL>       Remove a website from a list of monitoring websites\n")
        print("  list                       Show a list of monitoring websites\n")
        print("  save                       Save a list of monitoring websites\n")
        print("  quit                       Exit this tool\n")
