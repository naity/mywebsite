"""Extracts the exif data of an image."""

from datetime import datetime
import exifread


def extract(image_path):
    with open(image_path, "rb") as f:
        tags = exifread.process_file(f)

    exif = {}

    # each value in tags is an instance of a class,
    # which has the attribute printable that contains the info as string
    if tags.get("Image Model"):
        exif["camera"] = tags["Image Model"].printable

    if tags.get("EXIF LensModel"):
        exif["lens"] = tags["EXIF LensModel"].printable

    if tags.get("EXIF FocalLength"):
        exif["focal_length"] = tags["EXIF FocalLength"].printable + "mm"

    if tags.get("EXIF FNumber"):
        f_stop = tags["EXIF FNumber"].printable
        f_stop = f_stop.split("/")
        if len(f_stop) == 1:
            exif["f_stop"] = f_stop[0]
        else:
            exif["f_stop"] = str(int(f_stop[0]) / int(f_stop[1]))

    if tags.get("EXIF ExposureTime"):
        exif["shutter"] = tags["EXIF ExposureTime"].printable + "s"

    if tags.get("EXIF ISOSpeedRatings"):
        exif["iso"] = tags["EXIF ISOSpeedRatings"].printable

    if tags.get("EXIF DateTimeOriginal"):
        datetime_str = tags["EXIF DateTimeOriginal"].printable
        exif["taken_time"] = datetime.strptime(datetime_str, "%Y:%m:%d %H:%M:%S")

    return exif
