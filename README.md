# Open multiple tiktok urls continuously

This is a small GUI application using `tkinter`, which allows you to open multiple TikTok links from a CSV file. Each run will open a certain number of links, making it easier for you to manage your link browsing.

## 📦 Library request
- `tkinter`: Create user interface.
- `csv`: Read CSV file.
- `webbrowser`: Open link in default browser.
- `messagebox` and `filedialog`: Interface interaction.
## ✨ Features
- Simple interface with `tkinter`.
- Select the `.csv` file containing the list of TikTok usernames.
- Select the starting position (`begin`) and the number of lines to open each time (`skip`).
- Each time you press **Run**, the program will open the links from the line `begin` to `end`.
- Press **Continue** to open the next group of links.
## 📦 Csv structure
The CSV file needs to be in a format where each line contains a **TikTok username**, for example:
'''
username1
username2
username3
'''
## ⚙️ How to use?
1. **Run the program:** Make sure you have Python 3 installed.
2. **Enter information:**
- `Begin`: the line to start opening the link (default is 1).
- `Skip`: the number of links to open each time (default is 5).
3. **Click “Get information”** to confirm.
4. **Select the CSV file** containing the list of TikTok usernames.
5. **Click “Run”** to open the first group of links.
6. **Click “Continue”** to open the next group.
## 📋 Notes
- The file will be opened using your computer's **default browser**.
- Use the “Continue” feature to browse through all usernames sequentially.
- If you have not entered `begin` and `skip` information, the program will open the first 5 lines by default.
