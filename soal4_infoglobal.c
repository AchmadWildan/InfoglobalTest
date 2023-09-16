#include <stdio.h>
#include <stdlib.h>

// Fungsi untuk mengambil sampel dari microphone
int getMicrophoneSample() {
    // Simulasikan pengambilan sampel dari microphone
    int sample = rand() % 256; // Nilai acak antara 0 hingga 255
    return sample;
}

// Fungsi untuk menghitung hasil DSP
int calculateDSP(int *samples) {
    // Implementasikan algoritma DSP di sini, sesuai dengan persyaratan Anda
    int result = 0;

    // Contoh sederhana: jumlahkan semua sampel
    for (int i = 0; i < 4; i++) {
        result += samples[i];
    }

    return result;
}

// Fungsi utama
int main() {
    int samples[4];

    // Ambil sampel dari microphone
    for (int i = 0; i < 4; i++) {
        samples[i] = getMicrophoneSample();
    }

    // Hitung hasil DSP
    int result = calculateDSP(samples);

    // Output hasil
    printf("Hasil DSP: %d\n", result);

    return 0;
}
