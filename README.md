# Scratch User Info Analysis Tool 🎮📊

Welcome to the **Scratch User Info Analysis Tool**! 🎉 This tool allows you to gather and analyze detailed information about Scratch user profiles and generate a comprehensive report. Whether you want to check user favorites, followers, projects, or other profile details, this tool does it all! 🌟

---

## Features ✨

- **User Information Analysis** 🔍  
  Analyze various aspects of a Scratch user's profile such as their:
  - Username
  - Favorites 💖
  - Followers 👥
  - Following 🔄
  - Projects 📂
  - Messages 💬
  - Studios 🏢
  
- **Progress Bar** ⏳  
  Monitor the progress of the analysis with a visual progress bar.

- **ASCII Art** 🎨  
  Enjoy a colorful ASCII art display when you start the tool.

- **Save Results** 💾  
  After the analysis, the results will be saved to a text file named `analysis_{username}.txt`.

---

## How to Use 🚀

1. **Clone the repository** or download the tool:
   ```bash
   git clone https://github.com/kyrazzx/deepscratch.git
   cd scratch-user-info-analysis
   ```

2. **Install Dependencies**:  
   Make sure you have Python 3 installed. Install the required packages by running:
   ```bash
   pip install requests colorama
   ```

3. **Run the Tool**:  
   Start the tool by executing the Python script:
   ```bash
   python main.py
   ```

4. **Follow the Interactive Menu**:  
   - Choose the option to start the user info analysis.
   - Enter the Scratch username you'd like to analyze.
   - The tool will process the information and generate a detailed report in the form of a `.txt` file.
  
---

## Customization 🔧

- **Add More Options**: Feel free to extend the tool to analyze additional user data or add new features.

---

## Example Output 📄

Once the analysis is complete, the result will be saved in a file named `analysis_{username}.txt`. Example contents:

```
Analysis of ScratchUser123's Scratch Profile
================================================================================

Username: ScratchUser123

--------------------------------------------------------------------------------
User Info:
================================================================================
{
    "id": "123456789",
    "username": "ScratchUser123",
    "profile": {
        "bio": "Just another Scratch enthusiast!",
        "location": "Internet",
        "joined": "2020-01-01"
    }
}

--------------------------------------------------------------------------------
Favorites:
================================================================================
[
    "Project A",
    "Project B",
    "Project C"
]

...
```

---

## Credits 🙌

This tool was created by **Kyra** 🦸‍♂️.  
If you have any questions or suggestions, feel free to reach out! 😄

---

## License 📝

This tool is open-source under the MIT License. You can freely modify and distribute it as per your needs.

---

Let the analysis begin! 🚀🎉
