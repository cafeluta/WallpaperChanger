# WallpaperChanger

🖼️ **Python App that automatically downloads a random wallpaper from UNSPLASH to keep your desktop cool**

## 📋 What this project does

* **Downloads random images** from Unsplash based on a custom query
* **Sets random wallpaper** from downloaded images on Windows system
* **Automatically manages** local wallpaper collection
* **Periodically changes** wallpaper to keep your desktop always fresh

## 🔑 Getting Unsplash API Key

To use the application, you need a free API key from Unsplash:

1. **Create account** on [Unsplash Developers](https://unsplash.com/developers)
2. **Login** and access [your applications](https://unsplash.com/oauth/applications)
3. **Click "New Application"**
4. **Accept terms** of service
5. **Fill out the form:**
   - Application name: `WallpaperChanger`
   - Description: `Personal wallpaper changer app`
6. **Copy the generated Access Key**
7. **In parent folder create a `secretAPI.py` file and inside write `id_key = YOUR_UNSPLASH_API_KEY`**

## 🚀 Installation and Setup

### Cloning the project
```bash
git clone https://github.com/cafeluta/WallpaperChanger.git
cd WallpaperChanger
```

### Installing dependencies
```bash
# Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

## 🛠️ Usage

### Running the application
```bash
python3 wallpaper_changer.py
```

## 📦 Creating Windows Application with PyInstaller

### Installing PyInstaller
```bash
pip install pyinstaller
```

### Creating the executable
```bash
# Single window application (recommended)
pyinstaller --onefile --windowed wallpaper_changer.py
```

### Debug PyInstaller
```bash
# Run with console to see errors
pyinstaller --onefile wallpaper_changer.py
```

## 📄 License

This project is licensed under [MIT License](LICENSE).

## 👨‍💻 Author

**Sebastian Ionita** - [@cafeluta](https://github.com/cafeluta)

---