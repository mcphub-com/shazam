import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apidojo/api/shazam'

mcp = FastMCP('shazam')

@mcp.tool()
def shazam_events_list(artistId: Annotated[str, Field(description="The value of 'artist->adamid' field returned in …/search OR …/songs/v2/detect OR …/songs/get-details endpoint The value of 'artists->id' field returned in …/shazam-songs/get-details OR …/albums/get-details OR …/albums/get-related-artist")],
                       l: Annotated[Union[str, None], Field(description='The language code')] = None,
                       _from: Annotated[Union[str, None], Field(description='The date to list events from')] = None,
                       to: Annotated[Union[str, None], Field(description='The date to list events to. Ex : 2023-01-15')] = None,
                       limit: Annotated[Union[int, float, None], Field(description='The number of items per page, for paging purpose Default: 50')] = None,
                       offset: Annotated[Union[int, float, None], Field(description='The page index, for paging purpose Default: 0')] = None) -> dict: 
    '''List future events'''
    url = 'https://shazam.p.rapidapi.com/shazam-events/list'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'artistId': artistId,
        'l': l,
        'from': _from,
        'to': to,
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(term: Annotated[str, Field(description='Full name of songs or artists')],
           locale: Annotated[Union[str, None], Field(description='The language code')] = None,
           offset: Annotated[Union[int, float, None], Field(description='For paging purpose Default: 0')] = None,
           limit: Annotated[Union[int, float, None], Field(description='For paging purpose, maximum is fixed at 5 items per response Default: 5')] = None) -> dict: 
    '''Search for songs, artists that match input term'''
    url = 'https://shazam.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'term': term,
        'locale': locale,
        'offset': offset,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def auto_complete(term: Annotated[str, Field(description='Any word or phrase of song, artist, etc... that you are familiar with')],
                  locale: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict: 
    '''Get suggestions by word or phrase'''
    url = 'https://shazam.p.rapidapi.com/auto-complete'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'term': term,
        'locale': locale,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def charts_track(locale: Annotated[Union[str, None], Field(description='The language code')] = None,
                 listId: Annotated[Union[str, None], Field(description='The value of listId field returned in .../charts/list endpoint')] = None,
                 pageSize: Annotated[Union[int, float, None], Field(description='Used for paging purpose, 20 items per response is maximum. Default: 20')] = None,
                 startFrom: Annotated[Union[int, float, None], Field(description='Used for paging purpose. Default: 0')] = None) -> dict: 
    '''Get all popular songs in specific chart'''
    url = 'https://shazam.p.rapidapi.com/charts/track'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'locale': locale,
        'listId': listId,
        'pageSize': pageSize,
        'startFrom': startFrom,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def charts_list() -> dict: 
    '''List all available charts by cities, countries, and genres'''
    url = 'https://shazam.p.rapidapi.com/charts/list'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artists_get_details(id: Annotated[str, Field(description="The value of 'artist->adamid' field returned in .../search OR .../songs/v2/detect OR .../songs/get-details endpoint The value of 'artists->id' field returned in .../shazam-songs/get-details OR .../albums/get-details OR .../albums/get-related-artist")],
                        l: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict: 
    '''Get detailed information of an artist'''
    url = 'https://shazam.p.rapidapi.com/artists/get-details'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'l': l,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artists_get_top_songs(id: Annotated[str, Field(description="The value of 'artist->adamid' field returned in .../search OR .../songs/v2/detect OR .../songs/get-details endpoint The value of 'artists->id' field returned in .../shazam-songs/get-details OR .../albums/get-details OR .../albums/get-related-artist")],
                          l: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict: 
    '''Get top songs of an artist'''
    url = 'https://shazam.p.rapidapi.com/artists/get-top-songs'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'l': l,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artists_get_latest_release(id: Annotated[str, Field(description="The value of 'artist->adamid' field returned in .../search OR .../songs/v2/detect OR .../songs/get-details endpoint The value of 'artists->id' field returned in .../shazam-songs/get-details OR .../albums/get-details OR .../albums/get-related-artist")],
                               l: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict: 
    '''Get latest release of an artist'''
    url = 'https://shazam.p.rapidapi.com/artists/get-latest-release'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'l': l,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artists_get_summary(id: Annotated[str, Field(description="The value of 'artist->adamid' field returned in .../search OR .../songs/v2/detect OR .../songs/get-details endpoint The value of 'artists->id' field returned in .../shazam-songs/get-details OR .../albums/get-details OR .../albums/get-related-artist")],
                        l: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict: 
    '''Get summary information related to an artist'''
    url = 'https://shazam.p.rapidapi.com/artists/get-summary'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'l': l,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def shazam_songs_get_details(id: Annotated[str, Field(description="The value of 'id' field returned in .../search endpoint")],
                             locale: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict: 
    '''Get mapping id information between systems to use with other endpoints.'''
    url = 'https://shazam.p.rapidapi.com/shazam-songs/get-details'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'locale': locale,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def shazam_songs_list_similarities(id: Annotated[str, Field(description="The value of 'related-tracks->id' field returned in .../shazam-songs/get-details endpoint")],
                                   locale: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict: 
    '''Get similar (You may also like) songs'''
    url = 'https://shazam.p.rapidapi.com/shazam-songs/list-similarities'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'locale': locale,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def albums_get_details(id: Annotated[str, Field(description="The value of 'albums->id' field returned in .../shazam-songs/get-details OR .../artists/get-albums OR .../artists/get-summary The value of 'id' field returned in .../artists/get-albums OR .../artists/get-latest-release endpoint The value of 'albumadamid' field returned in .../songs/v2/detect OR .../songs/detect endpoint")],
                       l: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict: 
    '''Get detailed album of an album'''
    url = 'https://shazam.p.rapidapi.com/albums/get-details'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'l': l,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def albums_get_related_artist(id: Annotated[str, Field(description="The value of 'albums->id' field returned in .../shazam-songs/get-details OR .../artists/get-albums OR .../artists/get-summary The value of 'id' field returned in .../artists/get-albums OR .../artists/get-latest-release endpoint The value of 'albumadamid' field returned in .../songs/v2/detect OR .../songs/detect endpoint")],
                              l: Annotated[Union[str, None], Field(description='The language code')] = None) -> dict: 
    '''Get artist related to an album'''
    url = 'https://shazam.p.rapidapi.com/albums/get-related-artist'
    headers = {'x-rapidapi-host': 'shazam.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'l': l,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
