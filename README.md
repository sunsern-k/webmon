# Website Monitoring tool

## Overview 
The `webmon` is a simple Python-based program for monitoring network connectivity to a set of websites. 
It provides an interactive prompt so that the following operations can be performed: 

- Add a new website to a list of monitoring websites
- Remove a website from a list of monitoring websites
- Check network connectivity to each website from a list of monitoring websites. 
- List all of monitoring websites in the list
- Save all of monitoring websites in the configuration file
- Quite the monitoring tool 

## Prerequisites 
- Python 3.8+

## Installation 

1. Clone the source files

> git clone https://github.com/sunsern-k/webmon.git

2. Install dependencies

> pip install -r requirements.txt  

3. Run the monitoring tool 

> python webmonctl.py


## Usage 

Once run the monitoring tool, the `(webmon)` interactive prompt will be shown as an example below:

```
$python webmonctl.py 

#### Website Monitoring ####

(webmon)
```

### Get help? 

Press any key such as `h` to show a short description of all subcommands

```
(webmon)h

Website Monitoring Tool

Usage:

  add <Website URL>          Add a website to a list of monitoring websites

  remove <Website URL>       Remove a website from a list of monitoring websites

  list                       Show a list of monitoring websites

  save                       Save a list of monitoring websites

  quit                       Exit this tool
```

### Add a website to the monitoring tool 

Use the `add <Website URL>` in order to add a website to a list of the monitoring tool.

You can also enter `help add` to see a brief description. 

```
(webmon)help add
Add a website to a list of monitoring websites

Usage:
  add <Website URL>
Examples:
  add https://www.google.com   add the Google website to a list of the monitoring websites
  add http://httpforever.com   add the HTTP Forever website to a list of the monitoring websites
```

**Example:**

```
(webmon)add https://www.google.com
Website https://www.google.com added to the monitoring list
(webmon)add http://httpforever.com
Website http://httpforever.com added to the monitoring list
```

### Show websites from the monitoring tool 

Use the `list` subcommand to show current websites in the monitoring list. 

You can enter `help list` to see a short description.

```
(webmon)help list
Show a list of monitoring websites

Usage:
  list
```

**Examples:**

```
(webmon)list
https://www.google.com
http://httpforever.com
```

### Check network connectivity to each website from the monitoring tool

Use the `check` subcommand to monitor network connectivity to monitoring websites. 

```
(webmon)help check
Check the network connectivity from a list of monitoring websites

Usage:
  check
Examples:
  check
  https://www.google.com: connected
  https://this-web-is-down.com: disconnected

```

**Examples:**

```
(webmon)check
https://www.google.com: connected
http://httpforever.com: connected
```
### Remove a website from from the monitoring websites 

Use `remove <Website URL>` to remove an added website from monitoring websites.

```
(webmon)help remove
Remove a website from a list of monitoring websites

Usage:
  remove <Website URL>
Examples:
  remove https://www.google.com   remove the Google website from a list of the monitoring websites
```

**Examples:**

```
(webmon)list
https://www.google.com
http://httpforever.com
(webmon)remove https://www.google.com
Website https://www.google.com removed from the monitoring list
(webmon)list
http://httpforever.com
(webmon)check
http://httpforever.com: connected
(webmon)
```
### Save monitoring websites in the configuration file.

Enter the `save` subcommand in order to save a list of monitoring websites
in a configuration file - default: `webmon.conf`. 

```
(webmon)help save
Save a list of websites in the configuration file

Usage:
```

**Examples:**

```
(webmon)save
Saved all in a list of monitoring websites: webmon.conf
```

The content in the configuration file is a simple text file which records each monitoring website line-by-line.

**Examples**

```
$cat webmon.conf
http://httpforever.com
```

## Exit the monitoring tool
Enter `quit` in order to exit the tool

```
(webmon)help quit
Exit the website monitoring

Usage:
  quit
```

**Examples:**

```
(webmon)quit

Happy to help! Bye

```