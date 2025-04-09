import sqlite3

connection = sqlite3.connect('blogs.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO blogs (title, published, content) VALUES (?, ?, ?)",
              ('Power of Yoga',
               'April 12, 2023',
               '''Yoga is an ancient practice that originated in India over 5,000 years ago. The word "yoga" comes from the Sanskrit word "yuj," which means to yoke or unite, and refers to the union of the body, mind, and spirit.
The practice of yoga began as a way to achieve spiritual enlightenment and liberation, with the earliest known text on yoga being the Yoga Sutras, written by the sage Patanjali in the 2nd century BCE. These teachings outlined the Eight Limbs of Yoga, a set of practices that guide the yogi towards union with the divine.

Over time, yoga evolved into a more physical practice, with various postures or asanas being developed to help prepare the body for meditation and spiritual practice. In the 20th century, yoga began to spread to the West and has since become popular as a form of exercise and stress relief.

Today, yoga is practiced in many different forms, including Hatha, Vinyasa, Ashtanga, and Kundalini, among others. It continues to be a popular practice for both physical and mental well-being.

Here are some of the benefits of practicing yoga regularly:
Improved flexibility and balance: Yoga involves stretching and holding different poses that can help to increase flexibility and improve balance.

Increased strength: Many yoga poses require you to hold your own body weight, which can help to build strength in various muscle groups.

Reduced stress and anxiety: Yoga incorporates breathing techniques and meditation that can help to calm the mind and reduce stress and anxiety levels.

Better sleep: Practicing yoga can help to improve the quality of your sleep, making you feel more rested and energized.

Lowered blood pressure: Studies have shown that regular yoga practice can help to reduce blood pressure levels in individuals with hypertension.

Improved immune function: Yoga can help to boost the immune system by increasing blood flow, reducing stress hormones, and stimulating the lymphatic system.

Pain relief: Certain yoga poses and movements can help to alleviate pain in the back, neck, shoulders, and other areas of the body.

Increased mindfulness and focus: Yoga can help to increase mindfulness and focus by improving the connection between the mind and body.

Improved respiratory function: Practicing yoga can help to improve lung capacity and respiratory function, making it easier to breathe deeply and fully.

These are just a few of the many benefits of practicing yoga regularly. It is a holistic practice that can improve overall physical, mental, and emotional well-being.

Here's a plan I suggest for someone looking to experience the health benefits of practicing yoga regularly:
Assess your current fitness level: Before starting any new exercise program, it's important to assess your current fitness level to identify any limitations or restrictions. Talk to your doctor if you have any medical concerns or limitations.

Determine your goals: What are you hoping to achieve by practicing yoga regularly? Do you want to improve flexibility, strength, balance, or reduce stress? Identifying your goals will help you tailor your yoga practice to your needs.

Find a class or instructor: If you're new to yoga, consider taking a class or working with a qualified instructor to learn the proper form and technique. They can help you modify poses to suit your needs and guide you through a safe and effective practice.

Start slow and be consistent: It's important to start slowly and gradually build up your practice. Consistency is key, so aim to practice yoga regularly, even if it's just a few minutes each day. Over time, you can increase the duration and intensity of your practice.

Choose the right type of yoga: There are many different styles of yoga, each with their own benefits and challenges. Hatha, Vinyasa, and Restorative yoga are great options for beginners, while more advanced practitioners may enjoy Ashtanga or Bikram yoga.

Focus on breath and mindfulness: One of the key benefits of yoga is its emphasis on breath work and mindfulness. By focusing on your breath and staying present in the moment, you can reduce stress and improve mental clarity.

Combine with a healthy diet: While yoga is a great way to improve your physical and mental health, it's important to combine it with a healthy diet for maximum benefits. Eating a balanced diet that's rich in whole foods, fruits, and vegetables can help you feel more energized and support your overall health.'''))

cursor.execute("INSERT INTO blogs (title, published, content) VALUES (?, ?, ?)",
      ('Unlocking the World of NFTs',
       'Jan 07, 2024',
       '''What are NFTs?
NFTs, or Non-Fungible Tokens, are unique digital assets that are verified using blockchain technology. They can be anything from artwork and music to virtual real estate and even tweets. NFTs are designed to provide proof of ownership and authenticity, making them valuable to collectors and creators alike.

The History of NFTs: From Concept to Reality
The concept of NFTs has been around for several years, but it wasn't until 2017 that they began gaining widespread attention. The first NFT project was called CryptoKitties, a blockchain-based game that allowed users to breed and trade virtual cats. Since then, the popularity of NFTs has exploded, with major artists, musicians, and sports leagues all jumping on board.

How NFTs Work: Understanding the Technology Behind It
NFTs are built on blockchain technology, which is essentially a digital ledger that records every transaction made with a particular asset. In the case of NFTs, this means that ownership and authenticity of the asset are permanently recorded on the blockchain. This allows for transparency and security, ensuring that each NFT is unique and cannot be replicated or duplicated.

The Value of NFTs: What Makes Them So Attractive to Collectors
One of the main attractions of NFTs is their rarity and uniqueness. Since each NFT is one-of-a-kind, collectors are willing to pay high prices to own them. Additionally, the blockchain technology used to verify and authenticate NFTs adds an extra layer of security and exclusivity. NFTs also have the potential to appreciate in value over time, making them a potentially lucrative investment.

NFTs in the Art World: Transforming the Way We View and Buy Art
NFTs have the potential to revolutionize the art world by allowing artists to sell their digital art as unique, one-of-a-kind pieces. This means that digital art can now be owned and displayed just like traditional art, and collectors can have proof of ownership and authenticity. NFTs have already sold for millions of dollars at major art auctions.

Here are some of the most valuable NFTs sold to date:

Beeple's "Everydays: The First 5000 Days" - Sold for $69.3 million in March 2021
CryptoPunk #3100 - Sold for $7.57 million in May 2021
CryptoPunk #7804 - Sold for $7.57 million in June 2021
CryptoPunk #6965 - Sold for $5.41 million in March 2021
Beeple's "Crossroads" - Sold for $6.6 million in February 2021
CryptoPunk #8888 - Sold for $1.5 million in March 2021
CryptoPunk #4156 - Sold for $1.4 million in February 2021
CryptoPunk #3100 - Sold for $1.23 million in June 2021
CryptoPunk #7804 - Sold for $1.19 million in June 2021
CryptoPunk #6487 - Sold for $1.15 million in March 2021'''))

cursor.execute("INSERT INTO blogs (title, published, content) VALUES (?, ?, ?)",
           ('Covid-19: Global Outbreak Update and Vaccination Progress',
            'March 17, 2023',
            '''The Ongoing Situation of COVID-19: Most Affected Countries, Safety Protocols and Vaccination Updates
    The COVID-19 pandemic has impacted the entire world, with many countries seeing an increase in cases and deaths in recent months. It is important to stay informed about the situation in different countries and take proper safety measures to prevent the spread of the virus. In this blog post, we will discuss the most affected countries, safety protocols, and vaccination updates.

    Most Affected Countries
    As of now, the most affected countries in terms of total cases and deaths are the United States, India, Brazil, and Russia. However, many other countries are also experiencing a surge in cases, including countries in Europe and Southeast Asia.

    In the United States, there have been over 32 million confirmed cases and over 580,000 deaths. India has recorded over 25 million cases and over 280,000 deaths. Brazil has seen over 15 million cases and over 400,000 deaths, while Russia has reported over 5 million cases and over 120,000 deaths. These numbers are constantly changing, so it is important to stay up to date with the latest information.

    Safety Protocols
    It is essential to take precautions and follow safety protocols to protect yourself and those around you from COVID-19. Some of the recommended safety protocols include:

    1. Wearing a mask in public spaces.
    2. Maintaining physical distance of at least 6 feet from others.
    3. Washing your hands regularly with soap and water for at least 20 seconds.
    4. Avoiding large gatherings and crowded places.
    5. Staying home if you feel sick.

    Additionally, many countries have implemented lockdowns and other restrictions to slow the spread of the virus. These restrictions vary depending on the country and local situation, but may include limits on public gatherings, closures of non-essential businesses, and travel restrictions.

    Vaccination Updates
    Vaccines are one of the most effective tools in combating COVID-19. As of now, there are several vaccines approved for use around the world, including those from Pfizer-BioNTech, Moderna, AstraZeneca, Johnson & Johnson, and Sinovac.

    Many countries have launched vaccination campaigns to vaccinate their populations. However, the distribution of vaccines has been unequal, with some countries having better access to vaccines than others. This has led to calls for more equitable distribution of vaccines to ensure that everyone has access to them.

    It is also important to note that vaccines are not a silver bullet, and it is still necessary to follow safety protocols even after getting vaccinated. Vaccines can greatly reduce the risk of severe illness and death from COVID-19, but they may not prevent all cases of the virus.''' ))


connection.commit()
connection.close()
