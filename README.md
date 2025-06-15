# Selenium Web Automation Tests

This project provides automated tests for the **Vercel site** using **Python**, **Selenium**, **pytest**, and a **Makefile** to simplify and automate the testing workflow.

It covers:
- ✅ **Navigation bar functionality** (e.g., Experiences, Skills links)
- ✅ **PDF download verification**
- ✅ **Makefile one-command automation**

![Test Flow Figure](figure/figur.png)


---

## 📂 Project Structure

├── download_testing.py  # PDF download test
├── navbar_testing.py    # Navigation bar tests
├── Makefile             # Convenient test automation
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (e.g., website URL)
├── downloads/           # Downloaded files (auto-created, git ignored)
├── report.xml           # pytest report 
├── .gitignore           # Git ignore rules


## ⚙️ Setup

### Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo>
```

### Create and activate virtual environment
```bash
python -m venv venv
# On macOS / Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Create .env file
Create a .env file in the root directory with:
```bash
test_website={Put your website}
```

## 🚀 Run Tests
Using Makefile
```bash
make test
```

## 📄 Notes
- All downloads are saved to the downloads/ directory (auto-cleaned before each run)
- The .env file lets you easily change the target website URL
- Test report is saved as report.xml

## 💡 Future improvements
- Add GitHub Actions CI integration
- Extend tests to additional navigation items or site features


## 📝 License
MIT