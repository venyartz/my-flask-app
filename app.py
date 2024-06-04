from flask import Flask, request, render_template, flash
app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    resources = None
    if request.method == 'POST':
        subjects = {
            'Matematik': min(40, int(request.form.get('Matematik', 0))),
            'Türkçe': min(40, int(request.form.get('Türkçe', 0))),
            'Kimya': int(request.form.get('Kimya', 0)),
            'Fizik': int(request.form.get('Fizik', 0)),
            'Biyoloji': int(request.form.get('Biyoloji', 0))
        }
        resources = get_resources(subjects)
    return render_template('index.html', resources=resources)

def get_resources(subjects):
    resources = {}
    
    # Matematik
    math_net = subjects['Matematik']
    if math_net < 10:
        resources['Matematik'] = {
            'Video': ['Rehber Matematik 0\'dan Geometriye', 'Kenan KARA 0\'dan Geometri', 'SML Hoca'],
            'Soru Bankası': ['Ens Matematik TYT', 'Yayın Denizi Problemler', 'Aktif Problemler', 'Karekök Tyt Mat. 0']
        }
    elif 10 <= math_net <= 22:
        resources['Matematik'] = {
            'Video': ['Rehber Matematik 49 günde TYT video', 'Mert hoca 70 günde TYT video', 'Bıyıklı Matematik 55 günde TYT', 'Erhan Ardıç', 'Rehber Matematik Geometri Kampı'],
            'Soru Bankası': ['Mikro Orijinal', 'Karekök', 'Geometri 0', 'Metin Yayınları', 'Parkur TYT']
        }
    else:
        resources['Matematik'] = {
            'Video': ['SML Hoca', 'Kenan Kara Geometri'],
            'Soru Bankası': ['3-4-5 TYT Matematik', '3D yayınları TYT Matematik', '3-4-5 Geometri', '3D TYT Geometri']
        }
    
    # Türkçe
    turkce_net = subjects['Türkçe']
    if turkce_net < 20:
        resources['Türkçe'] = {
            'Soru Bankası': ['ENS Türkçe', 'Strateji Günlük TYT Türkçe']
        }
    elif 20 <= turkce_net < 30:
        resources['Türkçe'] = {
            'Video': ['Benim Hocam TYT Türkçe video ders kitabı'],
            'Soru Bankası': ['Çap Yayınları Plus', 'Miray Yayınları TYT Türkçe']
        }
    else:
        resources['Türkçe'] = {
            'Soru Bankası': ['3-4-5 TYT Türkçe', 'Bilgi sarmal Türkçe', 'Kafa Dengi extra Türkçe', 'Limit Yayınları TYT', '3D TYT Türkçe']
        }
    
    # Kimya
    kimya_net = subjects['Kimya']
    if kimya_net < 4:
        resources['Kimya'] = {
            'Soru Bankası': ['Antrenman Yayınları', 'Aktif Öğrenme Sıfırdan', 'Okyanus 40 seansta kimya', 'Eğitim Vadisi Start Serisi']
        }
    else:
        resources['Kimya'] = {
            'Video': ['Görkem ŞAHİN video', 'Kimya Adası video'],
            'Soru Bankası': ['3D TYT Kimya', '3-4-5 Kimya', 'Bilgi Sarmal', 'Orbital(Önerilen)']
        }
    
    # Fizik
    fizik_net = subjects['Fizik']
    if fizik_net < 4:
        resources['Fizik'] = {
            'Soru Bankası': ['Aktif Öğrenme Fizik', 'Sıfırdan', 'Okyanus 40 seansta Fizik', 'Aktif Fizik', 'Eğitim Vadisi', 'Eğitim Vadisi Start serisi']
        }
    else:
        resources['Fizik'] = {
            'Video': ['Umut Öncül TYT Fizik video', 'Vip Fizik video', 'Özcan Aykın video'],
            'Soru Bankası': ['3D TYT Fizik', '3-4-5 Fizik', 'Bilgi Sarmal']
        }
    
    # Biyoloji
    biyoloji_net = subjects['Biyoloji']
    if biyoloji_net < 3:
        resources['Biyoloji'] = {
            'Soru Bankası': ['Okyanus 40 seansta Biyoloji', 'Eğitim Vadisi Starts Serisi']
        }
    else:
        resources['Biyoloji'] = {
            'Video': ['Dr. Biyoloji video', 'Betül Biyoloji video', 'Selin Hoca video'],
            'Soru Bankası': ['3D Biyoloji', '3-4-5 Biyoloji', 'Bilgi Sarmal', 'Biyotik(Önerilen)']
        }
    
    return resources

if __name__ == '__main__':
    app.run(debug=True, port=5002)
