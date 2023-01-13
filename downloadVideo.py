from TikTokApi import TikTokApi

with TikTokApi() as api:
    ID = "7185354125507349806"
    FILE_NAME = "VideosFolder/", ID
    video = api.video(id=ID)

    # Bytes of the TikTok video
    video_data = video.bytes()

    with open("out.mp4", "wb") as out_file:
        out_file.write(video_data)