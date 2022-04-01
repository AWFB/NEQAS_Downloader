import downloader
from registry import register

register({
    'name': 'Sweat Tests',
    'url_code': 'QEHSWT',
    'handler': downloader.handle_download_url,
})