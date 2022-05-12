import os
from googleapiclient.discovery import build

#api_key = os.environ.get('AIzaSyBwNK7uOPd4ygHqEkslmb1mLwTeKXNQod4')
api_key = 'AIzaSyBwNK7uOPd4ygHqEkslmb1mLwTeKXNQod4'

youtube = build('youtube', 'v3', developerKey=api_key)

#playlist_id = 'PL8uoeex94UhHFRew8gzfFJHIpRFWyY4YW'
#playlist_id = 'RDGMEMHDXYb1_DDSgDsobPsOFxpA'
playlist_id = 'PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj'

#https://www.youtube.com/watch?v=GUqYdsBjZxg&list=RDGMEMHDXYb1_DDSgDsobPsOFxpA&start_radio=1&rv=vqPIvA9ATO4&ab_channel=JackHarlow

#https://www.youtube.com/watch?v=o3bCFdwOH1Q&ab_channel=Arrow
#https://www.youtube.com/watch?v=_UCGiDVxBR8&list=RD_UCGiDVxBR8&start_radio=1&ab_channel=WestonEstateVEVO
#https://www.youtube.com/watch?v=HpYdA-06jTc&list=RDHpYdA-06jTc&start_radio=1&ab_channel=WILLIS-Topic
#https://www.youtube.com/watch?v=NHZ64-Cfhuw&list=RDMM&start_radio=1&rv=AMjl2dCrpyc&ab_channel=WestonEstateVEVO

#https://www.youtube.com/watch?v=mRD0-GxqHVo&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj&ab_channel=GlassAnimalsVEVO
#https://www.youtube.com/watch?v=AMjl2dCrpyc&list=PLJV5ZVu94Y8rFSKy8Y2gdovILow434IOd&ab_channel=WILLIS-Topic

videos = []

nextPageToken = None
while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=nextPageToken
    )

    pl_response = pl_request.execute()

    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    vid_request = youtube.videos().list(
        part="statistics",
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()

    for item in vid_response['items']:
        vid_views = item['statistics']['viewCount']

        vid_id = item['id']
        yt_link = f'https://youtu.be/{vid_id}'

        videos.append(
            {
                'views': int(vid_views),
                'url': yt_link
            }
        )

    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

#videos.sort(key=lambda vid: vid['views'], reverse=True)

i = 0
for video in videos[:10]:
    i += 1
    print(i, video['url'], video['views'])