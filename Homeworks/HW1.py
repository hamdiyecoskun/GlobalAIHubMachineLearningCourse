
1) How would you define Machine Learning?
Bilgisayarların istatistiksel işlemler ile veriler üzerinden öğrenmesini sağlayan algoritmalardır

2) What are the differences between Supervised and Unsupervised Learning? Specify example 3 algorithms for each of these.
Denetimli öğrenmede model girdi ve çıktı değişkenleri(etiketli veri) ile eğitilir. Amaç girdi özelliklerini çıktı ile eşleştirmek için uygun fonksiyonu bulmaktır. Algoritmaları: linear regression, logistics regression, random forest. Denetimsiz öğrenmede model sadece girdi verileri(etiketsiz veri) ile eğitilir. Amaç veriler hakkında bilgi edinmek için dağılımı modellemektir. Algoritmaları: cluster algorithms, k-means, hierarchical clustering.

3) What are the test and validation set, and why would you want to use them?
Doğrulama veri seti modelin performansını değerlendirmek için, test veri seti modelin gelecekteki performansını değerlendirmek için kullanılır.

4) What are the main preprocessing steps? Explain them in detail. Why we need to prepare our data?
Modelin belirli bir veri üzerine eğilim göstermemesi için tekrarlayan (duplicate) verilerin silinmesi, sınıfların eşit dağılmadığı dengesiz veri kümeleriyle çalışıldığında azınlık sınıfına ait verileri arttırma(oversampling) ya da ağırlıklı sınıfa ait verileri veri kümesinden çıkarma(undersampling) işlemleri uygulanarak dengeli bir veri kümesi elde edilmesi, eksik değerlerin medyan veya ortalama ile doldulması veya kaldırılması, aykırı değer(genel dağılımın dışına çıkan gözlem) tespit edilmesi ve silme,ortalama ile doldurma işlemlerinin uygulanması, yanlılığın engellenmesi ve algoritmanın hızının arttırılması için değişkenlerin belirlenen aralıklara indirgenmesi(feature scaling), gürültülü verilerin etkilerini azaltmak için verinin sıralanması ve eşit frekanslarda paketlere bölünmesi(binning), verilerin bütün bir bilgi olarak değil de bu bilgiyi oluşturan vasıflardan bazılarının çıkarılması ve sistemin bu vasıflar üzerine kurulması (feature extraction), girdi kabul edilecek şekilde dönüşüm yapılması (feature encoding) İlgisiz, gereksiz, güvenilmez veriler yanıltıcı sonuçlar doğurabilir. Sonucun doğruluğunu arttırmak için veriler hazırlanmalıdır.

5) How you can explore and analyse countionus and discrete variables?
Ayrık değişken belirli sayıda değere sahip olanı ifade ederken, sürekli değişken belirli bir aralık arasında herhangi bir değeri alabilen değişkendir. Ayrık değişkenler bar chart, sürekli değişkenler histogram aracılığıyla analiz edilir.

6) Analyse the plot given below. (What is the plot and variable type, check the distribution and make comment about how you can preproccess it.)
Histogram. Sürekli değişken.
