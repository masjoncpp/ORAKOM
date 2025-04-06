.model small
.stack 100h
.data
    ; Data input
    prompt_nama      db 13,10,'Masukkan Nama Anda       : $'
    prompt_nim       db 13,10,'Masukkan NIM Anda        : $'
    prompt_kelas     db 13,10,'Masukkan Kelompok Kelas  : $'
    prompt_alamat    db 13,10,'Masukkan Alamat Rumah    : $'
    
    nama    db 50, ?, 50 dup('$')
    nim     db 20, ?, 20 dup('$')
    kelas   db 10, ?, 10 dup('$')
    alamat  db 100, ?, 100 dup('$')
    
    ; Data output
    header  db 13,10,'===== KARTU UCAPAN IDUL FITRI =====',13,10,'$'
    selamat db 'Selamat Hari Raya Idul Fitri 1446 H$'
    mohon   db 'Mohon Maaf Lahir dan Batin$'
    mutiara db 13,10,13,10,'Kata Mutiara:',13,10
            db '"Kemenangan sejati adalah ketika kita bisa memaafkan"$'
            
    label_nama db 13,10,'Nama  : $'
    label_nim  db 13,10,'NIM   : $'
    label_kelas db 13,10,'Kelas : $'
    label_alamat db 13,10,'Alamat: $'
    
    ; Warna pelangi (blinking + warna)
    rainbow db 8Ch,8Eh,8Ah,8Bh,89h,8Dh  ; Attribute bytes
    color_len equ $ - rainbow
    
    baris_selamat db 10   ; Baris di bagian bawah layar
    kolom_selamat db 15  ; Kolom di tengah layar
    
.code
start:
    ; Inisialisasi
    mov ax, @data
    mov ds, ax
    mov es, ax
    
    ; Clear screen
    mov ax, 0003h
    int 10h
    
    ; Input data pengguna
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
    mov ah, 09h
    lea dx, header
    int 21h
    
    ; Tampilkan data user dengan format label
    lea dx, label_nama
    mov ah, 09h
    int 21h
    
    lea dx, nama+2
    mov ah, 09h
    int 21h
    
    lea dx, label_nim
    mov ah, 09h
    int 21h
    
    lea dx, nim+2
    mov ah, 09h
    int 21h
    
    lea dx, label_kelas
    mov ah, 09h
    int 21h
    
    lea dx, kelas+2
    mov ah, 09h
    int 21h
    
    lea dx, label_alamat
    mov ah, 09h
    int 21h
    
    lea dx, alamat+2
    mov ah, 09h
    int 21h
    
    ; Tampilkan teks berkedip warna-warni
    mov dl, kolom_selamat   ; Posisi kolom awal
    mov dh, baris_selamat   ; Posisi baris untuk teks selamat
    call show_rainbow
    
    ; Tampilkan kata mutiara
    mov ah, 09h
    lea dx, mutiara
    int 21h
    
    ; Exit
    mov ax, 4C00h
    int 21h

show_rainbow proc near
    push ax
    push bx
    push cx
    push dx
    push si
    push di
    push bp
    
    ; Atur posisi kursor untuk 'Selamat...'
    mov bh, 0
    mov ah, 02h
    mov dl, kolom_selamat  ; Kolom tengah
    mov dh, baris_selamat  ; Baris
    int 10h
    
    ; Tampilkan 'Selamat...' dengan efek
    lea si, selamat
    call rainbow_text
    
    ; Atur posisi kursor untuk 'Mohon...'
    mov ah, 02h
    inc dh     ; Baris berikutnya
    mov kolom_selamat, 15
    mov baris_selamat, dh
    int 10h
    
    ; Tampilkan 'Mohon...' dengan efek
    lea si, mohon
    call rainbow_text
    
    pop bp
    pop di
    pop si
    pop dx
    pop cx
    pop bx
    pop ax
    ret
show_rainbow endp

rainbow_text proc near
    push ax
    push bx
    push cx
    push dx
    push si
    push di
    push bp
    
    xor bx, bx  ; Index warna
    cld         ; Arah pembacaan string
    
print_char:
    lodsb       ; Baca karakter dari [SI]
    cmp al, '$'
    je done
    
    ; Tampilkan karakter dengan warna
    push ax
    push bx
    push cx
    push dx
    
    mov ah, 09h
    mov bl, rainbow[bx]
    mov bh, 0
    mov cx, 1
    int 10h
    
    pop dx
    pop cx
    pop bx
    pop ax
    
    ; Geser kursor ke kanan
    inc kolom_selamat
    mov ah, 02
    mov bh, 0
    mov dl, kolom_selamat
    mov dh, baris_selamat
    int 10h
    
    ; Update index warna
    inc bx
    cmp bx, color_len
    jb next_char
    xor bx, bx
    
next_char:
    jmp print_char
    
done:
    pop bp
    pop di
    pop si
    pop dx
    pop cx
    pop bx
    pop ax
    ret
rainbow_text endp

end start
