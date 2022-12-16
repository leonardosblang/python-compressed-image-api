# python-compressed-image-api 

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="100" />
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains an API for compressing and sending images using FastAPI written in Python. The API converts a selected image to webpm and them compresses it further by encoding it with base64, while also having the option to apply extra compression methods such as making use of algorithms like zlib.

## 📊 Comparison

We compare the original image (in png and jpeg format) to the webp format, which is a modern image format that provides superior compression for image files while still maintaining quality.

            | PNG           | WEBP            |
|-----------|---------------|-----------------|
| Size      | 114KB         | 58KB            |

            | JPG           | Compressed WEBP |
|-----------|---------------|-----------------|
| Size      | 14.7MB        | 791KB           |

(Normal files are stored in images/ , compressed ones are in results/ )

## 🏁 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### 📋 Prerequisites

You will need to have Python 3.7+ installed.

### 🔧 Installing

Create a new virtual environment and activate it:

```bash
python -m venv venv
. venv/bin/activate
```
install dependencies with:

```bash
pip install -r requirements.txt
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Made  by [Leonardo Lang](https://github.com/leonardosblang)
