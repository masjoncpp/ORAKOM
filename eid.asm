.model small
.stack 100h
.data
    ; Data untuk input
    prompt_nama      db 13,10,'Masukkan Nama Anda       : $'
    prompt_nim       db 13,10,'Masukkan NIM Anda        : $'
    prompt_kelas     db 13,10,'Masukkan Kelompok Kelas  : $'
    prompt_alamat    db 13,10,'Masukkan Alamat Rumah    : $'
    
    nama    db 50, ?, 50 dup('$')
    nim     db 20, ?, 20 dup('$')
    kelas   db 10, ?, 10 dup('$')
    alamat  db 100, ?, 100 dup('$')
    
    ; Data untuk output
    header  db 13,10,'===== KARTU UCAPAN IDUL FITRI =====',13,10,'$'
    footer  db 13,10,13,10,'Selamat Hari Raya Idul Fitri 1446 H',13,10
            db 'Mohon Maaf Lahir dan Batin$'
    mutiara db 13,10,13,10,'Kata Mutiara:',13,10
            db '"Kemenangan sejati adalah ketika kita bisa memaafkan"$'
    
.code
start:
    ; Inisialisasi
    mov ax, @data
    mov ds, ax
    
    ; Clear screen
    mov ax, 0003h
    int 10h
    
    ; Mode input
    ; Input Nama
    lea dx, prompt_nama
    mov ah, 09h
    int 21h
    
    lea dx, nama
    mov ah, 0Ah
    int 21h
    
    ; Input NIM
    lea dx, prompt_nim
    mov ah, 09h
    int 21h
    
    lea dx, nim
    mov ah, 0Ah
    int 21h
    
    ; Input Kelas
    lea dx, prompt_kelas
    mov ah, 09h
    int 21h
    
    lea dx, kelas
    mov ah, 0Ah
    int 21h
    
    ; Input Alamat
    lea dx, prompt_alamat
    mov ah, 09h
    int 21h
    
    lea dx, alamat
    mov ah, 0Ah
    int 21h
    
    ; Clear screen
    mov ax, 0003h
    int 10h
    
    ; Tampilkan header
    lea dx, header
    mov ah, 09h
    int 21h
    
    ; Tampilkan data yang diinput
    ; Tampilkan Nama
    mov ah, 09h
    lea dx, nama+2
    int 21h
    
    ; Pindah baris
    mov dl, 13
    mov ah, 02h
    int 21h
    mov dl, 10
    int 21h
    
    ; Tampilkan NIM
    lea dx, nim+2
    mov ah, 09h
    int 21h
    
    mov dl, 13
    mov ah, 02h
    int 21h
    mov dl, 10
    int 21h
    
    ; Tampilkan Kelas
    lea dx, kelas+2
    mov ah, 09h
    int 21h
    
    mov dl, 13
    mov ah, 02h
    int 21h
    mov dl, 10
    int 21h
    
    ; Tampilkan Alamat
    lea dx, alamat+2
    mov ah, 09h
    int 21h
    
    ; Tampilkan footer dan kata mutiara
    lea dx, footer
    mov ah, 09h
    int 21h
    
    lea dx, mutiara
    mov ah, 09h
    int 21h
    
    ; Akhiri program
    mov ah, 4Ch
    int 21h
end start
