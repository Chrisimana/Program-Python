import random

# Daftar pertanyaan dan jawaban chatbot
responses = {
    "halo": "Halo! Apa kabar?",
    "apa kabar": "Saya baik-baik saja, terima kasih! Bagaimana dengan kamu?",
    "siapa nama kamu": "Saya adalah chatbot. Kamu bisa memanggil saya ChatGPT.",
    "terima kasih": "Sama-sama! Ada yang bisa saya bantu lagi?",
    "selamat pagi": "Selamat pagi! Semoga hari kamu menyenankan.",
    "selamat malam": "Selamat malam! Semoga mimpi indah.",
    "apa yang kamu lakukan": "Saya sedang berbicara denganmu! 😊",
    "bye": "Sampai jumpa! Semoga hari kamu menyenankan.",
}

# Fungsi untuk memulai chat
def chatbot():
    print("Chatbot: Hai! Aku adalah chatbot. Ketik 'bye' untuk keluar.")
    
    while True:
        # Pengguna mengirim pesan
        user_input = input("Kamu: ").lower()
        
        # Mencari jawaban yang sesuai
        if user_input in responses:
            print("Chatbot:", responses[user_input])
        else:
            print("Chatbot: Maaf, saya tidak mengerti. Coba tanya lagi.")
        
        # Mengakhiri chat jika pengguna mengetik 'bye'
        if user_input == "bye":
            break

# Menjalankan program chatbot
chatbot()
