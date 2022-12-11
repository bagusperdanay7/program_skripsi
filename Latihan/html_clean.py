import re
# Rekomendasi hanya compile sekali saja
CLEANR = re.compile('<.*?>')

contoh_teks = '<br> </br> <br/> ini adalah contoh html <html> <b> </html> <bold>'


def clean_html(html_teks):
    '''Fungsi membersihkan html'''
    html_clean = re.sub(CLEANR, '', html_teks)

    # menghilangkan spasi lebih
    html_clean = ' '.join(
        re.sub("([@#][A-Za-z0-9]+)|(\w+:\/\/\S+)", " ", html_clean).split())
    return html_clean


print(clean_html(contoh_teks))
