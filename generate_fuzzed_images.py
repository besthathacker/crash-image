import os
import random

def random_bytes(size):
    return os.urandom(size)

def write_jpeg(path):
    with open(path, "wb") as f:
        f.write(b"\xFF\xD8\xFF\xE0")
        f.write(random_bytes(4096))
        f.write(b"\xFF\xD9")

def write_png(path):
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(random_bytes(4096))
        f.write(b"BADFOOTER")

def write_gif(path):
    with open(path, "wb") as f:
        f.write(b"GIF89a")
        f.write(random_bytes(4096))
        f.write(b"\x00\x3B")

def write_bmp(path):
    with open(path, "wb") as f:
        f.write(b"BM")
        f.write(random_bytes(4096))

def write_tiff(path):
    with open(path, "wb") as f:
        f.write(b"II*\x00")
        f.write(random_bytes(4096))

def write_webp(path):
    with open(path, "wb") as f:
        f.write(b"RIFF")
        f.write(random_bytes(4096))
        f.write(b"WEBP")

def main():
    os.makedirs("fuzzed_images", exist_ok=True)
    write_jpeg("fuzzed_images/fuzzed.jpg")
    write_png("fuzzed_images/fuzzed.png")
    write_gif("fuzzed_images/fuzzed.gif")
    write_bmp("fuzzed_images/fuzzed.bmp")
    write_tiff("fuzzed_images/fuzzed.tiff")
    write_webp("fuzzed_images/fuzzed.webp")
    print("Fuzzed image files generated in ./fuzzed_images/")

if __name__ == "__main__":
    main()
