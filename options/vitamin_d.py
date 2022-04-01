import downloader
from registry import register

register({
    'name': 'Vitamin D',
    'url_code': 'QEHVITD',
    'handler': downloader.handle_download_url,
})
