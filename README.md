
# 🌐 Ubuntu Image Fetcher

A mindful and respectful Python tool for downloading images from the web, inspired by the Ubuntu philosophy of community and safety.

## ✨ Features

- 🖼️ **Download Multiple Images** – Enter multiple image URLs (comma- or newline-separated).
- 🔐 **Safe Downloading** – Checks file size and content type before saving.
- 🔁 **Duplicate Detection** – Skips duplicate images using SHA-256 hashing.
- 📁 **Organized Storage** – Images are saved neatly into a `Fetched_Images` folder.
- 🧠 **Ubuntu Values** – Built with safety, sharing, and community principles in mind.

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.6+
- `requests` library

Install requirements (if needed):

```bash
pip install requests
````

### ▶️ Running the Program

```bash
python pylib.py
```

You will be prompted to enter image URLs:

```
Please enter image URLs (separated by commas or new lines):
https://example.com/image1.jpg,
https://example.com/image2.png
```

The program will:

* Validate each URL
* Download the image only if it's safe and non-duplicate
* Save it to the `Fetched_Images/` directory

---

## ✅ Safety Features

| Feature            | Description                                         |
| ------------------ | --------------------------------------------------- |
| Content Type Check | Accepts only image MIME types (`jpeg`, `png`, etc.) |
| File Size Limit    | Skips files larger than 10 MB                       |
| Hash Matching      | Prevents saving duplicate images                    |
| Timeout & Headers  | Uses timeout and user-agent for safe requests       |

---

## 📂 Folder Structure

```
.
├── ubuntu_image_fetcher.py
└── Fetched_Images/
    ├── image1.jpg
    └── image2.png
```

---

## 🧭 Philosophy

This tool is built in the spirit of **Ubuntu** — "I am because we are."
It promotes:

* 🛡️ **Respectful Use** – Avoid unnecessary strain on servers.
* ♻️ **Reuse and Efficiency** – Skip duplicates, save bandwidth.
* 🌱 **Mindful Coding** – Code with consideration for safety and others.

> “Ubuntu is not just a philosophy. It's a practice. It’s how we build community with code.”

---

## 🤝 Contributions

Feel free to fork and improve this project. Whether it's better error handling, support for more formats, or a GUI — all are welcome.

