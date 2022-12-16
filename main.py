from fastapi import FastAPI
from images_manip.compression import Compression

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/compress/base64/{data}")
async def compress_base64():
    test = Compression('images/Large-Sample-Image-download-for-Testing.jpg')
    return {"message": f"{test.get_base64()}"}


@app.get("/compress/zlib/{data}")
async def compress_zlib():
    test = Compression('images/Large-Sample-Image-download-for-Testing.jpg')
    return {"message": f"{test.get_zlib()}"}


@app.get("/compress/bz2/{data}")
async def compress_bz2():
    test = Compression('images/Large-Sample-Image-download-for-Testing.jpg')
    return {"message": f"{test.get_bz2()}"}


@app.get("/compress/gzip/{data}")
async def compress_gzip():
    test = Compression('images/Large-Sample-Image-download-for-Testing.jpg')
    return {"message": f"{test.get_gzip()}"}

