from __future__ import print_function
import argparse
import os

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools


def pull_google_workout_data():
    """Accesses google workout sheet and writes to csv file.

    Always saves to local at: data/ in directory

    aargs:
        None

    returns:
        None
    """

    # get credentials
    scopes = 'https://www.googleapis.com/auth/drive.readonly'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        flow = client.flow_from_clientsecrets('client_id.json', scopes)
        creds = tools.run_flow(flow, store, flags)
    drive = discovery.build('drive', 'v3', http=creds.authorize(Http()))

    # search for files
    filename = 'workouts'
    src_mimetype = 'application/vnd.google-apps.spreadsheet'
    dst_mimetype = 'text/csv'

    files = drive.files().list(
        q='name="%s" and mimeType="%s"' % (filename, src_mimetype),
        orderBy='modifiedTime desc,name').execute().get('files', [])

    # export files to correct directory
    if files:
        fn = 'data/%s.csv' % os.path.splitext(files[0]['name'].replace(' ', '_'))[0]
        print('Exporting "%s" as "%s"... ' % (files[0]['name'], fn), end='')
        data = drive.files().export(fileId=files[0]['id'], mimeType=dst_mimetype).execute()
        if data:
            with open(fn, 'wb') as f:
                f.write(data)
            print('DONE')
        else:
            print('ERROR (could not download file)')
    else:
        print('!!! ERROR: File not found')

if __name__ == '__main__':
    _pull_google_workout_data()
