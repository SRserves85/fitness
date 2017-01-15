from __future__ import print_function
import argparse
import os

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools


def _pull_google_workout_data():
    """Accesses google workout sheet and writes to csv file.

    Always saves to local at: data/ in directory

    aargs:
        None

    returns:
        None
    """

    # get credentials
    SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store, flags)
    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

    # search for files
    FILENAME = 'workouts'
    SRC_MIMETYPE = 'application/vnd.google-apps.spreadsheet'
    DST_MIMETYPE = 'text/csv'

    files = DRIVE.files().list(
        q='name="%s" and mimeType="%s"' % (FILENAME, SRC_MIMETYPE),
        orderBy='modifiedTime desc,name').execute().get('files', [])

    # export files to correct directory
    if files:
        fn = 'data/%s.csv' % os.path.splitext(files[0]['name'].replace(' ', '_'))[0]
        print('Exporting "%s" as "%s"... ' % (files[0]['name'], fn), end='')
        data = DRIVE.files().export(fileId=files[0]['id'], mimeType=DST_MIMETYPE).execute()
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
