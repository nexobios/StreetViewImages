#!/usr/bin/python

# Imports
import urllib2
import cStringIO as sIO
import argparse
from PIL import Image


def generate_request_to_gmaps(gps_location, image_angle, image_size, user_key):
    # Get sub-strings
    image_parameters_str = []
    base_url = 'https://maps.googleapis.com/maps/api/streetview?'
    size_str = 'size=' + str(image_size[0]) + 'x' + str(image_size[1])
    image_parameters_str.append(size_str)
    location_str = '&location=' + str(gps_location[0]) + ',' + str(gps_location[1])
    image_parameters_str.append(location_str)
    if image_angle[0] is not None:
        heading_str = '&heading=' + str(image_angle[0])
        image_parameters_str.append(heading_str)
    if image_angle[1] is not None:
        fov_str = '&fov=' + str(image_angle[1])
        image_parameters_str.append(fov_str)
    if image_angle[2] is not None:
        pitch_str = '&pitch=' + str(image_angle[2])
        image_parameters_str.append(pitch_str)
    key_str = '&key=' + user_key
    image_parameters_str.append(key_str)
    # Create request string
    request_url = base_url
    for parameter in image_parameters_str:
        request_url += parameter
    return request_url


def get_images_from_gmaps(key):
    # Key comes from the Google Apps interface
    user_key = str(key.googleKey)
    # TODO (FrAg): The following information must be automatically obtained from the traced path
    # Start Cfg
    gps_location = [20.6162962, -103.2518853]
    # Size = [Width, Height]
    image_size = [640, 480]
    # Angle = [Heading, FOV, Pitch]
    image_angle = [None, 40, 0]
    # End of Cfg
    # Get the Image from GMaps
    url_API = generate_request_to_gmaps(gps_location, image_angle, image_size, user_key)

    file_handler = sIO.StringIO(urllib2.urlopen(url_API).read())
    img_from_web = Image.open(file_handler)
    return img_from_web


def main():
    # Argument Getter
    arguments = argparse.ArgumentParser(description="Street View Image Getter for some project")
    arguments.add_argument('-k', '--googleKey', required=True, help="Google API Key")
    arg = arguments.parse_args()

    image_test = get_images_from_gmaps(arg)
    Image._show(image_test)

if __name__ == '__main__':
    main()