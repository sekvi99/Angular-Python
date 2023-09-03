import logging
from dataclasses import dataclass, field

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from application.external_resources.abstract_api_connector import \
    ExternalResourceApiHandler
from application.responses.external_responses.yt_stats_response import \
    YouTubeStatsResponse
import urllib.parse

@dataclass
class YouTubeStatsApiHandler(ExternalResourceApiHandler):
    
    video_id: str = field(init=False)
    
    def __post_init__(self) -> None:
        self.video_id = urllib.parse.parse_qs(urllib.parse.urlsplit(self.url).query).get('v')

    
    def get_api_response(self) -> int:
        """
        Method for processing youtube api response if response was sucessfull data is saved to obtained_data prop.

        Returns:
            int: Response status code.
        """
        youtube = build("youtube", "v3", developerKey=self.api_key)
        
        try:
            response = youtube.videos().list(
                part="statistics",
                id=self.video_id
            ).execute()
            
            self.obtained_data = response['items'][0]
            return 200
    
        except HttpError as e:
            # Handle HTTP errors, including checking the status code
            status_code = e.resp.status
            error_message = e.content.decode('utf-8')
            logging.info(f"HTTP Error {status_code}: {error_message}")
            return status_code
        
    def transform_api_response_to_desired_format(self) -> YouTubeStatsResponse:
        """
        Transforms api response described below to YouTubeStatsResponse model.
        https://developers.google.com/youtube/v3/getting-started?hl=pl

        Returns:
            YouTubeStatsResponse: YouTubeStatsResponse object.
        """
        statistics = self.obtained_data['statistics']
        
        return YouTubeStatsResponse(
            views=statistics['viewCount'],
            likes=statistics['likeCount'],
            favourites=statistics['favoriteCount'],
            comments=statistics['commentCount']
        )