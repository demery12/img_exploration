from __future__ import absolute_import
from PIL import Image, ImageEnhance
import io
from google.cloud import vision
from google.cloud import language
from oauth2client.client import GoogleCredentials
import argparse
import os
import pickle 

# Need to run "export GOOGLE_APPLICATION_CREDENTIALS='/path/to/your/client_secret.json'"
# in terminal
credentials = GoogleCredentials.get_application_default()

vision_client = vision.Client.from_service_account_json('icr_tool.json')

language_client = language.Client()



import argparse
import base64

import googleapiclient.discovery
# [END import_libraries]


def main(image_folder):
    """Run a label request on a single image"""

    # [START authenticate]
    service = googleapiclient.discovery.build('vision', 'v1')
    # [END authenticate]

    # [START construct_request]
    response_list = []
    for image_name in os.listdir(image_folder):
        with io.open(image_folder+image_name, 'rb') as image:
            image_content = base64.b64encode(image.read())
            service_request = service.images().annotate(body={
                'requests': [{
                    'image': {
                        'content': image_content.decode('UTF-8')
                    },
                    'features': [{
                        'type': 'LABEL_DETECTION'

                    },
                    {
                        'type': 'FACE_DETECTION'
                    },
                    #{'type': 'WEB_DETECTION'}
                    ]
                }]
            })
            # [END construct_request]
            # [START parse_response]
            response = service_request.execute()
            print(response)
            label = response['responses'][0]['labelAnnotations'][0]['description']
            response['file_name'] = image_name
            print('Found label: %s for %s' % (label, image_name))
            response_list.append(response)
            # [END parse_response]
    with open('labels.pickle', 'wb') as handle:
         pickle.dump(response_list, handle, protocol=pickle.HIGHEST_PROTOCOL)
# [START run_application]
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("image_directory", help="Location of images to be explored- it feels sad if there are other non-image files in this directory")
    args = parser.parse_args()
    main(args.image_directory)
# [END run_application]
