.model small
.stack 100h
.data
    ; Data untuk input
    prompt_nama   db 13,10,'Masukkan Nama Anda         : $'
    prompt_nim    db 13,10,'Masukkan NIM Anda          : $'
    prompt_kelas  db 13,10,'Masukkan Kelompok Kelas    : $'
    prompt_alamat db 13,10,'Masukkan Alamat Rumah      : $'
    prompt_mutiara db 13,10,'Masukkan Kata-kata Mutiara: $'

    nama    db 50, ?, 50 dup('$')
    nim     db 20, ?, 20 dup('$')
    kelas   db 10, ?, 10 dup('$')
    alamat  db 100, ?, 100 dup('$')
    kata    db 100, ?, 100 dup('$')

    ; Data untuk output
    header  db 13,10,'===========Kartu Ucapan Idul Fitri===========',13,10,'$'
    label_nama  db 13,10,'Nama  : $'
    label_nim   db 13,10,'NIM   : $'
    label_kelas db 13,10,'Kelas : $'
    label_alamat db 13,10,'Alamat: $'
    label_kata  db 13,10,'Kata-kata mutiara : $'
    footer  db 13,10,13,10,'Selamat Hari Raya Idul Fitri 1446 H',13,10
            db 'Mohon Maaf Lahir dan Batin$'

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

    ; Input Kata-kata Mutiara
    lea dx, prompt_mutiara
    mov ah, 09h
    int 21h
    lea dx, kata
    mov ah, 0Ah
    int 21h

    ; Clear screen
    mov ax, 0003h
    int 10h

    ; Tampilkan Kartu Ucapan
    lea dx, header
    mov ah, 09h
    int 21h

    ; Tampilkan Nama
    lea dx, label_nama
    mov ah, 09h
    int 21h
    lea dx, nama+2
    mov ah, 09h
    int 21h

    ; Tampilkan NIM
    lea dx, label_nim
    mov ah, 09h
    int 21h
    lea dx, nim+2
    mov ah, 09h
    int 21h

    ; Tampilkan Kelas
    lea dx, label_kelas
    mov ah, 09h
    int 21h
    lea dx, kelas+2
    mov ah, 09h
    int 21h

    ; Tampilkan Alamat
    lea dx, label_alamat
    mov ah, 09h
    int 21h
    lea dx, alamat+2
    mov ah, 09h
    int 21h

    ; Tampilkan Kata-kata Mutiara
    lea dx, label_kata
    mov ah, 09h
    int 21h
    lea dx, kata+2
    mov ah, 09h
    int 21h

    ; Tampilkan Footer
    lea dx, footer
    mov ah, 09h
    int 21h

    ; Akhiri program
    mov ah, 4Ch
    int 21h
end start