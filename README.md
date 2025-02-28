time kütüphanesi sınırlı limit durumunda bekleme süresi ayarlamak için kullanılır.
tweepy kütüphanesi, twitter API bağlayarak tweet çekmede kullanılır.
pandas kütüphanesi tweetleri tablo formatına getirebilmek için kullanılır.
matplotlib.pyplot grafikleri oluştırmak için kullanılır.
seaborn kütüphanesi daah estetik görünümlü görselleştirme için kullanılır.
TextBlob kütüphanesi tweetlerin duygu analizini yapmak için kullanılır.
bearer_token twitter API v2'ye bağlanmak için gerekli olan kimlik doğrulama anaharının yazıldığı yerdir.
tweepy.Client(bearer_token=bearer_token) kullanılarak API istemcisi oluşturulur.
hastag ile aranacak hastag ne olacak ona karar verilir.
num_tweets ile çekilecek maksimum tweet sayısı atanır. API sınırlarına takılmamak için bu değer düşük tutulur ama ücretsiz kullanımda aylık maksimum 100 çekim yapılabilir.
tweets = [] ile bir tweets listesi oluşturulur ve çekilen tweetler burada saklanır.
def ile fetch_tweets adında bir fonksiyon oluşturulur.
global tweets denilerek tanımlanan tweets listesi fonksiyon içerisinde değiştirilebilir hale getirilir.
wait_time ile ilk bekleme süresi belirlenir. Eğer rate limiti aşılırsa ilk olarak 20 saniye beklenir.
max_wait ile maksimum bekleme süresi 180 saniye olarak alınır. Bu şekilde eğer API 3 dakikadan uzun süre bekleme gerektirirse işlem durdurulur.
while True: sürekli tweet çekmeye çalışır. Yanıt alınırsa döngü break ile sonlandırılır.
tweepy.Paginator ile search_recent_tweets fonksiyonu kullanılarak tweet çekimi sağlanır.
query=hashtag sadece belli bir hashtag içeren tweetleri aramada kullanılır.
max_results ile tek seferde çekilecek tweet sayısı belirlenir.
flatten(limit=num_tweets) düz listeye çevirme ve maksimum num_tweets kada tweet çekmek için kullanılır.
tweets.append(tweet.text) kullanılarak çekilen tweetlerin sadece metni listeye eklenir.
time.sleep(2) twitter API'ye aşırı istek görndermemek için her çekme işleminden sonra 2 saniye beklenmesini sağlar.
except tweepy.errors.TooManyRequests as e: except ile API istek limit aşılırsa TooManyRequests hatası döndürülür.
x-rate-limit-reset başlığı içinde rate limit aşıldığında ne zaman tekrar istek gönderilebileceğini döndürür.
reset_time değişkeni ile Twitter'ın verdiği bilgi okunur.
wait_time ile yeniden deneme süresi hesaplanır.
time.sleep(wait_time) ile konsola rate limiti aşıldı yazdırıldıktan sonra bekleme süresi kadar  beklenmesi sağlanır.
if wait_time >= max_wait: döngüsünde bekleme süresi 5 dakikadan fazlaysa API'nın geçici olarak bizi engellediği varsayılıp işlem durdurulur.
fetch_tweets() ile tweet çekilir.
df = pd.DataFrame(tweets, columns=["Tweet"]) verinin DataFrame'e aktarımını sağlar.
def get_sentiment(text) ile get_sentiment fonksiyonu tanımlanır.
TextBlob(text) ile tweetin duygu analizi yapılır.
sentiment.polarity tweetin duygu skorunu belirler ve bu skor 1 ve -1 arası değişir.
df["Sentiment"] = df["Tweet"].apply(get_sentiment) içinde apply(get_sentiment) kullanılarak her tweet için duygu analizi yapılır ve Sentiment sütununa eklenir.
plt.figure(figsize=(6, 4)) grafik için ideal boyut ayarlanır. Genişlik için 6, yükseklik için 4 değeri verilir.
sns.countplot(x=df["Sentiment"], palette=["red", "blue", "green"]) içinde sns.countplot seaborn kütüphanesini kullanarak çubuk grafik oluşturur. x=df["Sentiment"] kısmında x ekseninde tweetlerin duygu durumları yer alır. Palettte ile grafik renkleri belirlenir.
plt.title ile grafiğe başlık eklenir.
plt.xlabel x eksenine etiket eklemek için kullanılır.
plt.ylabel y eksenine etiket eklemek için kullanılır.
En son grafiği ekrana çizdirmek için plt.show() kullanılır.
