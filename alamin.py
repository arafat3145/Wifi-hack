import os

def install_packages():
    print("\nInstalling required packages...")
    os.system("pkg install -y root-repo")
    os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
    print("Packages installed successfully.\n")

def clone_repository():
    print("\nCloning the Wifi_Hack repository...")
    os.system("cd ..;git clone https://github.com/AlAmin/Wifi_Hack")  # Replace with your repository if you have one
    os.system("cd ..;chmod +x Wifi_Hack/birihack.py")
    print("Repository cloned and permissions set.\n")

def show_instructions():
    print("\n\033[1;34;40mThanks.\nInstallation Done.")
    print("Now Go To Home Directory [~] And Enter This Command:")
    print("sudo python Wifi_Hack/birihack.py -i wlan0 -K\n")

def main():
    while True:
        print('''\033[1;36;40m
        Wifi_Hack Installer By Al Amin
        Your Device Must Be Rooted
        If Any Question, Contact Me On Telegram
        Tg_User:@your_telegram_handle  # Update with your Telegram handle

        Menu:
        1. Install Required Packages
        2. Clone Wifi_Hack Repository
        3. Show Instructions
        4. Exit
        ''')
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            install_packages()
        elif choice == '2':
            clone_repository()
        elif choice == '3':
            show_instructions()
        elif choice == '4':
            print("\nExiting... Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()