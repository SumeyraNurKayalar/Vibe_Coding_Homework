time kütüphanesi sınırlı limit durumunda bekleme süresi ayarlamak için kullanılır.
tweepy kütüphanesi, twitter API bağlayarak tweet çekmede kullanılır.
pandas kütüphanesi tweetleri tablo formatına getirebilmek için kullanılır.
matplotlib.pyplot grafikleri oluştırmak için kullanılır.
seaborn kütüphanesi daah estetik görünümlü görselleştirme için kullanılır.
TextBlob kütüphanesi tweetlerin duygu analizini yapmak için kullanılır.
bearer_token twitter API v2'ye bağlanmaj için gerekli olan kimlik doğrulama anaharının yazıldığı yerdir.
tweepy.Client(bearer_token=bearer_token) kullanılarak API istemcisi oluşturulur.
hastag ile aranacak hastag ne olacak ona karar verilir.
num_tweets ile çekilecek maksimum tweet sayısı atanır. API sınırlarına takılmamak için bu düşük tutulur ama ücretsiz kısımda aylık maksimum 100 çekim yapılabilir.
