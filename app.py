from app import create_app

app = create_app()

if __name__ == '__main__':
    # Menjalankan aplikasi di port 8000 dengan reload otomatis saat ada perubahan kode
    app.run(host='127.0.0.1', port=8000, debug=True, use_reloader=True)
